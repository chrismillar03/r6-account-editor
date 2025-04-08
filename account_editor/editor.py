import base64, os, re
from .account import Account
from siegeapi import Auth
from typing import Optional

class Editor:
	def __init__(self, email: str, password: str, game_dir: Optional[str] = None):
		self.token: str = base64.b64encode(f"{email}:{password}".encode("utf-8")).decode("utf-8")
		self.game_dir: str = game_dir or os.path.join(os.getenv("USERPROFILE"), "Documents", "My Games", "Rainbow Six - Siege")
		self.accounts: dict = {}

	async def load_accounts(self) -> None:
		if len(self.accounts) > 0:
			raise Exception("Accounts already loaded!")

		auth: Auth = Auth(token=self.token)
		uuid_list: list = [f.path.split("\\")[-1] for f in os.scandir(self.game_dir) if f.is_dir()]
		player_list: list = await auth.get_player_batch(uids=uuid_list)

		await auth.close()

		for i in player_list.values():
			account: Account = Account(i.id, i.name)
			settings_file: str = os.path.join(self.game_dir, i.id, "GameSettings.ini")
			current_group: str = "[UNKNOWN]"

			with open(settings_file, "r") as file:
				for line in file:
					line = line.rstrip()

					if re.search("\[\w+\]", line):
						current_group = line
					elif re.search("\w+=\w+", line):
						account.set_group_value(current_group, *line.split("=", 1))

			self.accounts[account.id] = account

	async def save_account(self, id):
		account: Account = self.accounts[id]
		settings_file: str = os.path.join(self.game_dir, account.id, "GameSettings.ini")

		with open(settings_file, "w") as file:
			for group, settings in account.settings.items():
				file.write(f"{group}\n")

				for k, v in settings.items():
					file.write(f"{k}={v}\n")

				file.write("\n")

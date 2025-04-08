import asyncio, os, time
from dotenv import load_dotenv
from account_editor import Account, Editor, DATACENTERS

def array_selector(arr: list):
	for i, j in enumerate(arr):
		print(f"{i + 1}\t-\t{j}")

	while True:
		selection: str = input("\n=> ")

		if not selection.isnumeric():
			print("\nSelection must be numerical!")
			continue

		selection: int = int(selection)

		if selection < 1 or selection > len(arr):
			print("\nSelection out of bounds!")
			continue

		print()

		return arr[selection - 1]

async def main() -> None:
	os.system("cls" if os.name == "nt" else "clear")
	load_dotenv()

	account_editor: Editor = Editor(os.getenv("EMAIL"), os.getenv("PASSWORD"))

	await account_editor.load_accounts()

	account: Account = array_selector(list(account_editor.accounts.values()))
	datacenter: str = array_selector(DATACENTERS)

	account.set_group_value("[DISPLAY]", "Console", "1")
	account.set_group_value("[ONLINE]", "DataCenterHint", datacenter)

	await account_editor.save_account(account.id)

	print(f"Successfully changed datacenter for {account.name} to {datacenter} ({account.id})")

	time.sleep(5)

if __name__ == "__main__":
	asyncio.run(main())

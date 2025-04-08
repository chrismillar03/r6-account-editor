class Account:
	def __init__(self, id: str, name: str):
		self.id: str = id
		self.name: str = name
		self.settings: dict = {}

	def get_group(self, group: str) -> dict:
		if not group in self.settings:
			self.settings[group] = {}

		return self.settings[group]

	def set_group_value(self, group: str, key: str, value: str) -> None:
		if not group in self.settings:
			self.settings[group] = {}

		self.settings[group][key] = value

	def __str__(self) -> str:
		return self.name

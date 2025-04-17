import json, os
from typing import Optional

class Config:
    def __init__(self, path: str, struct: Optional[dict]):
        self.path: str = path
        self.data: dict = struct if struct else {}

        if struct:
            self.safe_save()

    def save(self):
        with open(self.path, "w") as file:
            file.write(json.dumps(self.data, sort_keys=True, indent=4, separators=(",", ": ")))

    def safe_save(self):
        if not os.path.exists(self.path):
            self.save()

    def load(self):
        with open(self.path, "r") as file:
            self.data = json.loads(file.read())

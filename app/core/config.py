
from __future__ import annotations

import json
from pathlib import Path


class Config:

    def __init__(self):

        self.settings = self._load("config/settings.json")

    @staticmethod
    def _load(filename: str):

        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(filename)

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @property
    def image_size(self) -> str:
        return self.settings.get("image_size", "1024x1024")

    @property
    def output_folder(self) -> str:
        return self.settings.get("output_folder", "output")

    @property
    def model(self) -> str:
        return self.settings.get("model", "gpt-image-1")

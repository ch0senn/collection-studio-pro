
from __future__ import annotations

import base64
from pathlib import Path

from openai import OpenAI


class OpenAIImageClient:
    """
    Wrapper around the OpenAI Images API.

    Generates an image from a prompt and saves it to disk.
    """

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate(
        self,
        prompt: str,
        output_file: Path,
        size: str = "1024x1024",
        model: str = "gpt-image-1",
    ) -> Path:
        """
        Generate an image and save it.

        Returns the path to the saved PNG.
        """

        output_file.parent.mkdir(parents=True, exist_ok=True)

        result = self.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
        )

        image_bytes = base64.b64decode(result.data[0].b64_json)

        with open(output_file, "wb") as f:
            f.write(image_bytes)

        return output_file

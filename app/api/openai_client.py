from __future__ import annotations

import base64
from pathlib import Path

from openai import OpenAI


class OpenAIImageClient:
    """
    Collection Studio Pro OpenAI Images client.
    """

    def __init__(self, api_key: str):

        if not api_key:
            raise ValueError("API key missing")

        self.client = OpenAI(api_key=api_key)

    def generate_image(
        self,
        prompt: str,
        output_file: str,
        model: str = "gpt-image-1",
        size: str = "1024x1024",
    ) -> Path:

        path = Path(output_file)

        path.parent.mkdir(parents=True, exist_ok=True)

        result = self.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
        )

        image_data = result.data[0].b64_json

        with open(path, "wb") as f:
            f.write(base64.b64decode(image_data))

        return path
        return output_file

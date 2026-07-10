from pathlib import Path

from app.api.openai_client import OpenAIImageClient
from app.core.prompt_builder import PromptBuilder, RobotPrompt
from app.core.config import Config


class CollectionGenerator:

    def __init__(self, api_key: str):

        self.config = Config()

        self.client = OpenAIImageClient(api_key)

        self.builder = PromptBuilder()

    def generate_one(self):

        robot = RobotPrompt(

            name="Friendly white ceramic service robot with glowing blue LED eyes",

            hairstyle="Mohawk"

        )

        prompt = self.builder.build(robot)

        output = Path(self.config.output_folder) / "001.png"

        self.client.generate_image(

            prompt=prompt,

            output_file=str(output),

            model=self.config.model,

            size=self.config.image_size

        )

        print()

        print("--------------------------------")

        print("Collection Studio Pro")

        print("--------------------------------")

        print(f"Saved : {output}")

        print("--------------------------------")

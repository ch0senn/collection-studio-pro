
import os
from pathlib import Path

from dotenv import load_dotenv

from app.api.openai_client import OpenAIImageClient
from app.core.prompt_builder import PromptBuilder


def main():

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not found")

    prompt = PromptBuilder().robot_portrait(
        robot="Friendly white ceramic service robot with glowing blue LED eyes",
        hairstyle="Mohawk",
    )

    client = OpenAIImageClient(api_key)

    output = Path("output") / "001.png"

    client.generate(
        prompt=prompt,
        output_file=output,
    )

    print(f"Saved {output}")


if __name__ == "__main__":
    main()

import os

from dotenv import load_dotenv

from app.core.collection_generator import CollectionGenerator


def main():

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:

        raise RuntimeError(

            "OPENAI_API_KEY missing.\nCreate a .env file first."

        )

    generator = CollectionGenerator(api_key)

    generator.generate_one()


if __name__ == "__main__":

    main()

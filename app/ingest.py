from dotenv import load_dotenv

from ingest.vortex_ingester import VortexIngester

load_dotenv()


def main():
    ingester = VortexIngester("../docs/")
    ingester.ingest()


if __name__ == "__main__":
    main()

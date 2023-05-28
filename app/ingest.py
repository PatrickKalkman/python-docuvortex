from dotenv import load_dotenv

from ingest.vortex_ingester import VortexIngester
from ingest.vortex_pdf_parser import VortexPdfParser

load_dotenv()


def main():
    ingester = VortexIngester(
        VortexPdfParser("../docs/Cyber_Security_Threats_in_Cloud_Literature_Review.pdf"))
    ingester.ingest()


if __name__ == "__main__":
    main()

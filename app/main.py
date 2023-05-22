import os

from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings


# load the .env file
load_dotenv()

# read the OPEN_API_KEY from the environment
OPEN_API_KEY = os.environ.get('OPENAI_API_KEY')

loader = PyPDFLoader("../docs/PlantEmpowerment.pdf")
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()

faiss_index = FAISS.from_documents(pages, embeddings)
docs = faiss_index.similarity_search("What is the best way to optimize photosynthesis",
                                     k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:300])

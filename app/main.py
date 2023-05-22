import os

from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# load the .env file
load_dotenv()

# read the OPEN_API_KEY from the environment
OPEN_API_KEY = os.environ.get('OPENAI_API_KEY')

loader = PyPDFLoader("../docs/PlantEmpowerment.pdf")
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()

vector_store = FAISS.from_documents(pages, embeddings)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff",
                                 retriever=vector_store.as_retriever())

query = "What is Photosynthetic Active Radiation?"
result = qa.run(query)
print(result)

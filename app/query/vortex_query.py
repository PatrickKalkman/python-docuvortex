from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import AIMessage, HumanMessage
from langchain.vectorstores.chroma import Chroma

from settings import COLLECTION_NAME, PERSIST_DIRECTORY


class VortexQuery:
    def __init__(self):
        load_dotenv()
        self.chain = self.make_chain()
        self.chat_history = []

    def make_chain(self):
        model = ChatOpenAI(
            client=None,
            model="gpt-3.5-turbo",
            temperature=0,
        )
        embedding = OpenAIEmbeddings(client=None)

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embedding,
            persist_directory=PERSIST_DIRECTORY,
        )

        return ConversationalRetrievalChain.from_llm(
            model,
            retriever=vector_store.as_retriever(),
            return_source_documents=True,
        )

    def ask_question(self, question: str):
        response = self.chain({"question": question, "chat_history": self.chat_history})

        answer = response["answer"]
        source = response["source_documents"]
        self.chat_history.append(HumanMessage(content=question))
        self.chat_history.append(AIMessage(content=answer))

        return answer, source

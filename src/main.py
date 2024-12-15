from dotenv import load_dotenv

from src.document_processor import DocumentProcessor
from src.giga_chat import GigaChatManager
from src.rag import RAGChain
from src.vector_store import VectorStoreManager
from src.web import ChatbotInterface

load_dotenv()
import logging
import os


class Chatbot:
    def __init__(self, pdf_path: str, vectorstore_path: str):
        self.document_processor = DocumentProcessor(pdf_path)
        self.vectorstore_manager = VectorStoreManager()
        self.gigachat_manager = GigaChatManager()
        self.vectorstore_path = vectorstore_path

    def setup(self):
        documents = self.document_processor.load_and_split()

        if os.path.exists(self.vectorstore_path):
            print("Loading vectorstore")
            vectorstore = self.vectorstore_manager.load_vectorstore(
                self.vectorstore_path
            )
        else:
            print("Creating vector store")
            vectorstore = self.vectorstore_manager.create_vectorstore(documents)
            self.vectorstore_manager.save_vectorstore(
                vectorstore, self.vectorstore_path
            )

        rag_chain = RAGChain(vectorstore, self.gigachat_manager.giga).create_chain()
        self.interface = ChatbotInterface(rag_chain)

    def run(self):
        self.interface.launch()


if __name__ == "__main__":
    pdf_path = "docs/Machine_Learning_System_Design.pdf"
    vectorstore_path = "vectorstore"

    chatbot = Chatbot(pdf_path, vectorstore_path)
    chatbot.setup()
    chatbot.run()

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


class VectorStoreManager:
    def __init__(self, embedding_model_name="sentence-transformers/all-mpnet-base-v2"):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=embedding_model_name,
            multi_process=True,
            encode_kwargs={"normalize_embeddings": True},
        )

    def create_vectorstore(self, documents):
        return FAISS.from_documents(documents, self.embedding_model)

    def save_vectorstore(self, vectorstore, path):
        vectorstore.save_local(path)

    def load_vectorstore(self, path):
        return FAISS.load_local(
            path, self.embedding_model, allow_dangerous_deserialization=True
        )

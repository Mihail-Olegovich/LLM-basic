from langchain import hub
from langchain.chains import RetrievalQA

class RAGChain:
    def __init__(self, vectorstore, llm):
        self.retriever = vectorstore.as_retriever()
        self.llm = llm
        self.prompt = hub.pull("rlm/rag-prompt")

    def create_chain(self):
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )
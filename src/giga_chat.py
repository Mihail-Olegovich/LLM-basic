import os
from langchain.chat_models.gigachat import GigaChat

class GigaChatManager:
    def __init__(self):
        self.giga_key = os.getenv("GIGACHAT_API_KEY")
        self.giga = GigaChat(
            credentials=self.giga_key,
            model="GigaChat-Pro",
            timeout=30,
            verify_ssl_certs=False
        )

    def get_response(self, prompt):
        return self.giga(prompt)
# ai_engine.py - Motor Inteligente de Processamento de Mensagens
import time
from knowledge_base import SearchEngine

class AIEngine:
    def __init__(self):
        self.search_engine = SearchEngine()

    def process_message(self, user_text):
        # Simula tempo de processamento/raciocínio
        time.sleep(0.3)
        return self.search_engine.search(user_text)

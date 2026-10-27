# auth.py - Gerenciamento de Login e Sessão
from config import USERS_DB

class AuthManager:
    def __init__(self):
        self.current_user = None

    def authenticate(self, username, password):
        user = username.strip().lower()
        if user in USERS_DB and USERS_DB[user] == password.strip():
            self.current_user = user
            return True, f"Bem-vindo, {user}!"
        return False, "Usuário ou senha incorretos."

    def logout(self):
        self.current_user = None

    def get_user(self):
        return self.current_user or "Visitante"

# ui_desktop.py - Interface Desktop com Tkinter e Suporte a Pesquisas
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from config import APP_NAME, VERSION, CURSO, PROFESSORES, THEME_DARK, THEME_LIGHT
from auth import AuthManager
from ai_engine import AIEngine

class DesktopApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME} v{VERSION}")
        self.geometry("980x680")
        self.minsize(850, 550)

        self.auth = AuthManager()
        self.ai = AIEngine()
        self.is_dark = True
        self.theme = THEME_DARK

        self.configure(bg=self.theme["bg"])
        self.show_login()

    def show_login(self):
        self.login_frame = tk.Frame(self, bg=self.theme["bg"])
        self.login_frame.pack(expand=True, fill="both")

        card = tk.Frame(self.login_frame, bg=self.theme["card_bg"], bd=1, relief="solid", padx=35, pady=35)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="🤖 TechAI Pro", font=("Helvetica", 20, "bold"), bg=self.theme["card_bg"], fg=self.theme["accent"]).pack(pady=(0, 5))
        tk.Label(card, text=f"{CURSO}\n{PROFESSORES}", font=("Helvetica", 9), bg=self.theme["card_bg"], fg=self.theme["text_muted"]).pack(pady=(0, 20))

        tk.Label(card, text="Usuário:", font=("Helvetica", 10, "bold"), bg=self.theme["card_bg"], fg=self.theme["text"]).pack(anchor="w")
        self.ent_user = tk.Entry(card, font=("Helvetica", 11), width=30)
        self.ent_user.insert(0, "admin")
        self.ent_user.pack(pady=(2, 12))

        tk.Label(card, text="Senha:", font=("Helvetica", 10, "bold"), bg=self.theme["card_bg"], fg=self.theme["text"]).pack(anchor="w")
        self.ent_pass = tk.Entry(card, font=("Helvetica", 11), width=30, show="*")
        self.ent_pass.insert(0, "admin123")
        self.ent_pass.pack(pady=(2, 20))

        btn = tk.Button(card, text="Acessar Sistema", font=("Helvetica", 11, "bold"), bg=self.theme["accent"], fg="white", command=self.handle_login, cursor="hand2")
        btn.pack(fill="x", ipady=6)

    def handle_login(self):
        u = self.ent_user.get()
        p = self.ent_pass.get()
        success, msg = self.auth.authenticate(u, p)
        if success:
            self.login_frame.destroy()
            self.show_chat()
        else:
            messagebox.showerror("Erro de Acesso", msg)

    def show_chat(self):
        self.chat_container = tk.Frame(self, bg=self.theme["bg"])
        self.chat_container.pack(fill="both", expand=True)

        # Header
        header = tk.Frame(self.chat_container, bg=self.theme["sidebar_bg"], height=55, padx=20, pady=10)
        header.pack(fill="x", side="top")

        tk.Label(header, text=f"🤖 TechAI Pro | Usuário: {self.auth.get_user()}", font=("Helvetica", 11, "bold"), bg=self.theme["sidebar_bg"], fg=self.theme["accent"]).pack(side="left")

        btn_logout = tk.Button(header, text="Sair", command=self.handle_logout, bg="#ef4444", fg="white", font=("Helvetica", 9), cursor="hand2")
        btn_logout.pack(side="right", padx=5)

        btn_theme = tk.Button(header, text="Alternar Tema", command=self.toggle_theme, bg=self.theme["card_bg"], fg=self.theme["text"], font=("Helvetica", 9), cursor="hand2")
        btn_theme.pack(side="right", padx=5)

        btn_clear = tk.Button(header, text="Limpar Chat", command=self.clear_chat, bg=self.theme["card_bg"], fg=self.theme["text"], font=("Helvetica", 9), cursor="hand2")
        btn_clear.pack(side="right", padx=5)

        # Chat Body
        self.chat_area = scrolledtext.ScrolledText(self.chat_container, wrap=tk.WORD, font=("Consolas", 10), bg=self.theme["chat_bg"], fg=self.theme["text"], bd=0, padx=15, pady=15)
        self.chat_area.pack(fill="both", expand=True, padx=10, pady=10)
        self.chat_area.config(state=tk.DISABLED)

        # Input Frame
        input_frame = tk.Frame(self.chat_container, bg=self.theme["sidebar_bg"], padx=15, pady=12)
        input_frame.pack(fill="x", side="bottom")

        self.input_field = tk.Entry(input_frame, font=("Helvetica", 11), bg=self.theme["card_bg"], fg=self.theme["text"], insertbackground=self.theme["text"])
        self.input_field.pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=6)
        self.input_field.bind("<Return>", lambda e: self.send_msg())

        btn_send = tk.Button(input_frame, text="Pesquisar / Enviar", font=("Helvetica", 10, "bold"), bg=self.theme["accent"], fg="white", command=self.send_msg, cursor="hand2")
        btn_send.pack(side="right", ipadx=12, ipady=4)

        self.append_text("🤖 TechAI Assistant", "Sistema inicializado! Digite qualquer assunto de TI (Python, SQL, Docker, Redes, Clean Code) para pesquisar.")

    def send_msg(self):
        msg = self.input_field.get().strip()
        if not msg:
            return

        self.append_text(f"👤 {self.auth.get_user()}", msg)
        self.input_field.delete(0, tk.END)

        self.after(400, lambda: self.process_ai(msg))

    def process_ai(self, query):
        resp = self.ai.process_message(query)
        self.append_text("🤖 TechAI Assistant", resp)

    def append_text(self, sender, text):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}:\n{text}\n\n" + "-"*60 + "\n\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def clear_chat(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state=tk.DISABLED)
        self.append_text("🤖 TechAI Assistant", "Histórico de mensagens limpo.")

    def handle_logout(self):
        self.auth.logout()
        self.chat_container.destroy()
        self.show_login()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.theme = THEME_DARK if self.is_dark else THEME_LIGHT
        self.configure(bg=self.theme["bg"])
        self.chat_container.destroy()
        self.show_chat()

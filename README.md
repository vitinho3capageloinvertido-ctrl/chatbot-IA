# TechAI Pro - Sistema de Assistência & Pesquisa de TI

**Curso Técnico de Desenvolvimento de Sistemas**  
**Professores:** Luis Felipe Cardoso & Wesley Fioreze  

---

## 🏗️ Estrutura Modular do Projeto
O projeto foi totalmente expandido e arquitetado em módulos reutilizáveis de código limpo:

```
chatbot-ti-pro/
│── config.py            # Configurações globais, usuários e temas
│── auth.py              # Módulo de autenticação e gerenciamento de sessão
│── knowledge_base.py    # Motor de pesquisa e base de conhecimento ampliada
│── ai_engine.py         # Processamento de respostas da IA
│── ui_desktop.py        # Interface gráfica Desktop (Tkinter)
│── main.py              # Ponto de entrada do código Python
│── index.html           # Interface Web completa
│── requirements.txt     # Dependências do sistema
└── README.md            # Documentação técnica do projeto
```

---

## 🚀 Como Executar

### 1. Aplicação Desktop em Python (Tkinter)
Para executar a versão desktop com suporte a login, alternância de tema e pesquisas:
```bash
python main.py
```

### 2. Aplicação Web
Para abrir no navegador:
```bash
python -m http.server 8000
```
Acesse: `http://localhost:8000`

---

## 🔑 Credenciais Pré-configuradas (`config.py`)
- **Administrador:** `admin` / `admin123`
- **Estudante:** `estudante` / `ti2026`
- **Professores:** `luis.cardoso` / `prof123` | `wesley.fioreze` / `prof123`

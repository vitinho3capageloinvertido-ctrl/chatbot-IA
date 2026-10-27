# knowledge_base.py - Base de Conhecimento Ampliada para Pesquisa de TI
import json

TI_TOPICS = {
    "python": {
        "title": "🐍 Python & Desenvolvimento",
        "keywords": ["python", "py", "tkinter", "pip", "flask", "django", "fastapi", "pandas", "numpy"],
        "summary": "Linguagem de alto nível, interpretada e multiparadigma.",
        "details": (
            "Python é referência em Inteligência Artificial, Ciência de Dados, Backend Web e Automação.\n\n"
            "• Web Frameworks: Django, Flask, FastAPI\n"
            "• Interfaces Gráficas: Tkinter, PyQt, CustomTkinter\n"
            "• Dados & IA: Pandas, NumPy, Scikit-Learn, PyTorch"
        )
    },
    "javascript": {
        "title": "⚡ JavaScript & Ecossistema Web",
        "keywords": ["javascript", "js", "node", "react", "express", "vue", "typescript", "npm", "nextjs"],
        "summary": "Linguagem fundamental da Web para Frontend e Backend.",
        "details": (
            "Com Node.js, JavaScript tornou-se uma linguagem Full Stack versátil.\n\n"
            "• Frontend: React.js, Vue.js, Angular, Next.js\n"
            "• Backend: Node.js, Express, NestJS\n"
            "• Ferramentas: Vite, Webpack, npm, pnpm"
        )
    },
    "banco_de_dados": {
        "title": "🗄️ Bancos de Dados & SQL",
        "keywords": ["banco", "sql", "mysql", "postgres", "postgresql", "oracle", "select", "insert", "nosql", "mongodb", "redis"],
        "summary": "Armazenamento, modelagem e manipulação persistente de dados.",
        "details": (
            "Modelos Relacionais (SQL) utilizam tabelas e ACID. NoSQL foca em escalabilidade.\n\n"
            "• Relacionais: PostgreSQL, MySQL, SQLite, SQL Server\n"
            "• NoSQL: MongoDB (Documentos), Redis (Chave-Valor), Cassandra\n"
            "• Exemplo SQL: SELECT * FROM usuarios WHERE ativo = TRUE;"
        )
    },
    "devops": {
        "title": "🐳 DevOps, Docker & Nuvem",
        "keywords": ["docker", "devops", "container", "kubernetes", "deploy", "ci/cd", "aws", "azure", "git"],
        "summary": "Integração contínua, conteinerização e infraestrutura.",
        "details": (
            "Práticas DevOps garantem agilidade na entrega de software seguro e escalável.\n\n"
            "• Conteinerização: Docker, Podman\n"
            "• Orquestração: Kubernetes (K8s)\n"
            "• CI/CD: GitHub Actions, GitLab CI, Jenkins"
        )
    },
    "redes_seguranca": {
        "title": "🌐 Redes, HTTP & Segurança da Informação",
        "keywords": ["redes", "tcp", "ip", "http", "https", "dns", "firewall", "vpn", "criptografia", "lgpd", "ssh"],
        "summary": "Comunicação de dados, protocolos e proteção cibernética.",
        "details": (
            "Fundamentos essenciais para conectividade e proteção de sistemas.\n\n"
            "• Protocolos Web: HTTP/1.1, HTTP/2, HTTP/3 (QUIC)\n"
            "• Segurança: TLS/SSL, Criptografia Assimétrica, Firewalls, Auth JWT\n"
            "• Camadas OSI/TCP-IP: Roteamento, IPV4/IPV6, DNS"
        )
    },
    "engenharia_software": {
        "title": "📐 Engenharia de Software & Arquitetura",
        "keywords": ["clean code", "solid", "arquitetura", "microsservicos", "mvc", "design patterns", "uml", "scrum", "agil"],
        "summary": "Boas práticas, padrões de projeto e metodologias ágeis.",
        "details": (
            "Desenvolvimento sustentável e organizado de sistemas complexos.\n\n"
            "• Princípios SOLID: S.O.L.I.D para orientação a objetos\n"
            "• Padrões de Projeto: Singleton, Factory, Observer, Strategy\n"
            "• Metodologias: Scrum, Kanban, TDD (Test-Driven Development)"
        )
    }
}

class SearchEngine:
    def __init__(self):
        self.kb = TI_TOPICS

    def search(self, query):
        q = query.lower().strip()
        results = []

        for key, topic in self.kb.items():
            for kw in topic["keywords"]:
                if kw in q:
                    results.append(topic)
                    break

        if results:
            first = results[0]
            return f"**{first['title']}**\n\n{first['details']}"
        
        return (
            f"🔎 **Pesquisa Registrada para:** '{query}'\n\n"
            "Não encontrei um tópico exato na base local. Tente pesquisar termos como:\n"
            "• *Python, JavaScript, SQL, Docker, Redes, Clean Code, SOLID ou Git*."
        )

    def get_all_topics(self):
        return [t["title"] for t, t in self.kb.items()]

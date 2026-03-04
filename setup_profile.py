import os

README = """# Olá, eu sou o Lucas Montenegro 👋

### Software Quality Assurance | Python Developer | Recife, BR 🇧🇷

Estudante apaixonado por qualidade de software, automação de testes e boas práticas de QA. Estou construindo um portfólio sólido que combina testes manuais documentados, automação com Selenium e scripts Python.

---

## 🛠️ Tecnologias & Ferramentas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

## 📂 Projetos em Destaque

| Repositório | Descrição | Stack |
|---|---|---|
| [qa-manual-test-project](https://github.com/lucasmontenegrodev/qa-manual-test-project) | Testes manuais completos: Test Cases, Bug Reports e fluxo ágil | Markdown, Jira |
| [automacao-selenium-python](https://github.com/lucasmontenegrodev/automacao-selenium-python) | Automação E2E com Selenium WebDriver e Page Object Model | Python, Selenium |
| [logica-programacao-python](https://github.com/lucasmontenegrodev/logica-programacao-python) | Lógica de programação, automação de cálculos e tratamento de exceções | Python |
| [voice-assistant-whisper-chatgpt](https://github.com/lucasmontenegrodev/voice-assistant-whisper-chatgpt) | Assistente de voz com Speech-to-Text e ChatGPT | Python, OpenAI |
| [finance-ai-qa-project](https://github.com/lucasmontenegrodev/finance-ai-qa-project) | QA aplicado a sistema financeiro com IA | Python |

---

## 📈 Foco atual

- 🧪 Aprofundando em **testes manuais estruturados** e documentação profissional
- 🤖 Evoluindo em **automação de testes** com Selenium + POM
- 📡 Aprendendo **testes de API** com Postman e Python (requests)
- 📚 Estudando **metodologias ágeis** aplicadas a QA (Scrum, Kanban)

---

## 🔗 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucas-montenegro-689a5a3a4/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lucasmontenegrodev)
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README.strip())

print("\n✅ README.md criado com sucesso!")
print("\nAgora rode os comandos abaixo para subir no GitHub:\n")
print("  git add .")
print('  git commit -m "feat: adiciona README do perfil"')
print("  git push\n")

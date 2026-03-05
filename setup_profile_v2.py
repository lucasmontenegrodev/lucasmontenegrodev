import os

README = """# Olá, eu sou o Lucas Montenegro 👋

### Software Quality Assurance Engineer | Python & JavaScript | Recife, BR 🇧🇷

Estudante apaixonado por qualidade de software, automação de testes e boas práticas de QA. Portfólio ativo com testes manuais documentados, automação E2E com Cypress e Selenium, testes mobile, API REST com Postman e estudos em JavaScript e Python.

---

## 🛠️ Tecnologias & Ferramentas

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cypress](https://img.shields.io/badge/Cypress-17202C?style=for-the-badge&logo=cypress&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

## 📂 Projetos em Destaque

| Repositório | Descrição | Stack |
|---|---|---|
| [qa-manual-test-project](https://github.com/lucasmontenegrodev/qa-manual-test-project) | Test Cases, Bug Reports e fluxo ágil completo com Jira | Markdown, Jira |
| [automacao-cypress](https://github.com/lucasmontenegrodev/automacao-cypress) | Testes E2E automatizados com Cypress em e-commerce | JavaScript, Cypress |
| [qa-mobile-testing](https://github.com/lucasmontenegrodev/qa-mobile-testing) | Testes de responsividade mobile e API REST com Postman | Markdown, Postman |
| [automacao-selenium-python](https://github.com/lucasmontenegrodev/automacao-selenium-python) | Automação E2E com Selenium WebDriver e Page Object Model | Python, Selenium |
| [estudos-javascript](https://github.com/lucasmontenegrodev/estudos-javascript) | Fundamentos e intermediário de JavaScript com exercícios práticos | JavaScript |
| [logica-programacao-python](https://github.com/lucasmontenegrodev/logica-programacao-python) | Lógica de programação, automação de cálculos e tratamento de exceções | Python |

---

## 📈 Foco atual

- 🧪 Testes manuais estruturados com rastreabilidade completa via **Jira**
- 🤖 Automação E2E com **Cypress** e **Selenium**
- 📱 Testes de **responsividade mobile** e **API REST** com Postman
- 🟨 Evoluindo em **JavaScript** para automação e desenvolvimento
- ☁️ Aprofundando em **Azure Cloud** e **GenAI** aplicados a QA

---

## 🔗 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucas-montenegro-689a5a3a4/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lucasmontenegrodev)
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README.strip())

print("\n✅ README.md atualizado com sucesso!")
print("\nAgora rode:\n")
print("  git add .")
print('  git commit -m "feat: atualiza README com novos projetos e tecnologias"')
print("  git push\n")

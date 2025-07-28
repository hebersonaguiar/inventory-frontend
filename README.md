# 📊 Inventory Frontend

Frontend simples e funcional para visualização e atualização de dados de inventário de hosts, desenvolvido com [**Streamlit**](https://streamlit.io/).

Este frontend se conecta ao backend `inventory`, apresentando dados em tabelas interativas com autenticação via JWT.

---

## 🚀 Tecnologias

- [Streamlit](https://streamlit.io/)
- [Python 3.12+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [JWT Authentication](https://jwt.io/)
- [EncryptedCookieManager](https://github.com/joachimvanderhenst/streamlit-cookies-manager)

---

## 📦 Funcionalidades

- Tela de **login** com autenticação protegida por token JWT
- Listagem de hosts com visualização tabular
- Edição de campos como:
  - Ambiente (`produutivo/não produtivo`)
  - Linguagem da aplicação (`pyhton`)
  - Observações (`Autenticação via API REST`)
- Integração com o backend via API REST
- Utilização de cookies criptografados para sessão

---

## 🧪 Pré-requisitos

- Docker e Docker Compose instalados
- Backend (`inventory`) em execução na mesma rede Docker

---

## 📁 Estrutura

```bash
inventory-frontend/
├── app.py             
├── auth/                 # Páginas de login/logout
│   ├── login.py          # Tela de login
├── protected/            # Páginas protegidas pós-login
│   ├── home.py           # Página principal
│   ├── hosts_list.py     # Listagem de hosts
│   └── host_edit.py      # Edição de host
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env

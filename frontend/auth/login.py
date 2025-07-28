import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

def login_page():
    st.title("Login - Inventário")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        try:
            response = requests.post(f"{API_URL}/api/v1/auth/login", json={
                "username": username,
                "password": password
            })

            if response.status_code in (200, 201):
                token = response.json().get("access_token")
                st.session_state["jwt_token"] = token
                st.session_state["logged_in"] = True
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos!")
        except Exception as e:
                st.error(f"Erro ao tentar login: {e}")

import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")
cookies = EncryptedCookieManager(
    prefix="login",  # prefixo opcional
    password=os.getenv("COOKIE_TOKEN")  # troque por algo seguro
)

# Necessário para funcionar corretamente
if not cookies.ready():
    st.stop()

def logout():
    if "token" in cookies:
        cookies["token"] = "expired"
        cookies.save()

    st.session_state.clear()
    st.session_state.logged_in = False
    st.session_state.username = None

def login_page():
    st.title("Login")

    st.set_page_config(
        layout="centered", 
        page_title="Dashboard Inventory",
        page_icon="🖥️",
        initial_sidebar_state="collapsed"
    )

    # Se já estiver logado via cookie
    if cookies.get("token") and cookies.get("token") != "expired":
        st.session_state["jwt_token"] = cookies.get("token")
        st.session_state["logged_in"] = True
        st.rerun()

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        login_submit = st.form_submit_button("Entrar")  
        # login_button = st.button("Entrar")

    if login_submit:
        try:
            response = requests.post(f"{API_URL}/api/v1/auth/login", json={
                "username": username,
                "password": password
            })

            if response.status_code in (200, 201):
                token = response.json().get("access_token")
                cookies["token"] = token
                cookies.save()
                st.session_state["jwt_token"] = token
                st.session_state["logged_in"] = True
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos!")
        except Exception as e:
                st.error(f"Erro ao tentar login: {e}")

import streamlit as st
import os
from streamlit_cookies_manager import EncryptedCookieManager
from protected.hosts_list import listar_hosts
from protected.host_edit import editar_host
from dotenv import load_dotenv

load_dotenv()

cookies = EncryptedCookieManager(
    prefix="login",  # prefixo opcional
    password=os.getenv("COOKIE_TOKEN")  # troque por algo seguro
)

def logout():
    cookies.delete("token")
    cookies.save()
    st.session_state.clear()
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()

def home_page():
    st.sidebar.success("Logado com sucesso")
    st.sidebar.button("Sair", on_click=logout)

    st.set_page_config(
        page_title="Dashboard Inventory",
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    menu = ["Listar Hosts", "Editar Hosts"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Listar Hosts":
        listar_hosts()
    elif choice == "Editar Hosts":
        editar_host()

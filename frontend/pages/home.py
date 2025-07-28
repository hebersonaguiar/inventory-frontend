import streamlit as st
from pages.hosts_list import listar_hosts
from pages.host_edit import editar_hosts

def logout():
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

    menu = ["Listar Hosts", "Editar Host"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Listar Hosts":
        listar_hosts()
    elif choice == "Editar Hosts":
        editar_hosts()

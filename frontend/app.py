import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

API_URL = os.getenv("API_URL")

# Mudar para usar api
USERS = {
    "admin": "admin"
}

def check_login(username, password):
    return USERS.get(username) == password

def login_page():
    st.title("Login")

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
                token = response.json.get("access_token")
                st.session_state["jwt_token"] = token
                st.session_state["logged_in"] = True
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos!")
        except Exception as e:
                st.error(f"Erro ao tentar login: {e}")




    # if st.button("Entrar"):
    #     if check_login(username, password):
    #         st.session_state.logged_in = True
    #         st.session_state.username = username
    #         st.success("Login realizado com sucesso!")
    #         st.rerun()
    #     else:
    #         st.error("Usuário ou senha inválidos!")

def main_app():

    st.set_page_config(
        page_title="Dashboard Inventory",
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    menu = ["Listar Hosts", "Editar Host"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Listar Hosts":
        st.subheader("Lista de Hosts")
        response = requests.get(f"{API_URL}/api/v1/inventory")
        if response.status_code in (200, 201):
            hosts = response.json()
            if not hosts:
                st.info("Nenhum host encontrado")
            else:
                # Converte para DataFrame
                dataFrame = pd.DataFrame(hosts)

                # Ordena as colunas
                ordered_columns = ["hostname","ipv4","distribution","so","up_time","mem_free","mem_total","mac_address","arch","processor","created_at","updated_at","notes","app_language","app_system","env","is_internal","location","midleware","url"]
                dataFrame = dataFrame[ordered_columns]

                # Mostra tabela interativa
                st.dataframe(dataFrame, use_container_width=True)
        else:
            st.error("Erro ao buscar hosts")

    elif choice == "Editar Host":
        st.subheader("Editar Host")

        # Carrega lita de hosts para edição
        response = requests.get(f"{API_URL}/api/v1/inventory")
        if response.status_code in (200, 201):
            hosts = response.json()
            hostnames = [host['hostname'] for host in hosts]

            if not hostnames:
                st.info("Nenhum host para editar.")
            else:
                st.markdown("**Selecione o host para editar**")
                selected_host = st.selectbox(" ", hostnames)

                # Busca dados completos de host selecionado
                host_data = next(host for host in hosts if host['hostname'] == selected_host)

                st.markdown("**Edite os campos abaixo**")

                # Criar colunas para exibição lado a lado
                col1, col2 = st.columns(2)

                with col1:
        
                    st.markdown("##### IPv4")
                    st.code(host_data.get("ipv4", ""))

                    st.markdown("**Distribuição**")
                    st.code(host_data.get("distribution", ""), language="")

                    st.markdown("**Sistema Operacional**")
                    st.code(host_data.get("so", ""), language="")

                    st.markdown("**Uptime**")
                    st.code(host_data.get("up_time", ""))

                    st.markdown("**Memória Livre**")
                    st.code(host_data.get("mem_free", ""))

                    st.markdown("**Memória Total**")
                    st.code(host_data.get("mem_total", ""))

                    st.markdown("**MAC Address**")
                    st.code(host_data.get("mac_address", ""))

                    st.markdown("**Arquitetura**")
                    st.code(host_data.get("arch", ""))

                    st.markdown("**Processador**")
                    st.code(host_data.get("processor", ""), language="")
                
                with col2:
                    url = st.text_input("URL", value=host_data.get("url", ""))

                    linguagens = ["Python", "Node.js", "Java", "Go", "PHP", "Ruby", "C#", "Outros"]
                    app_language = st.selectbox(
                        "Linguagem App",
                        options=linguagens,
                        index=linguagens.index(host_data.get("app_language", "Python")) if host_data.get("app_language") in linguagens else linguagens.index("Python")
                    )

                    app_system = st.text_input("Sistema App", value=host_data.get("app_system", ""))
                    
                    environments = ["Produção", "Homologação", "Desenvolvimento", "Staging"]
                    env = st.selectbox(
                        "Ambiente",
                        options=environments,
                        index=environments.index(host_data.get("env", "Produção")) if host_data.get("env") in environments else environments.index("Produção")
                    )

                    publication = ["Interno", "Externo"]
                    is_internal = st.selectbox(
                        "Interno?",
                        options=publication,
                        index=publication.index(host_data.get("is_internal", "Interno")) if host_data.get("is_internal") in publication else publication.index("Interno")
                    )

                    local = ["AWS", "Huawei", "On Premise"]
                    location = st.selectbox(
                        "Local",
                        options=local,
                        index=local.index(host_data.get("location", "On Premise")) if host_data.get("location") in local else local.index("On Premise")
                    )
                    midleware = st.text_input("Midlleware", value=host_data.get("midleware", ""))
                    st.markdown("##### Observações")
                    notes = st.text_area(" ", host_data.get("notes", ""), height=100)

                if st.button("Salvar alterações"):
                    payload = {
                        "hostname": selected_host,
                        "url": url,
                        "notes": notes,
                        "app_language": app_language,
                        "app_system": app_system,
                        "env": env,
                        "is_internal": is_internal,
                        "location": location,
                        "midleware": midleware
                    }

                    update_response = requests.put(f"{API_URL}/api/v1/inventory", json=payload)

                    if update_response.status_code in (200, 201):
                        st.success("Host atualizado com sucesso!")
                    else:
                        st.error(f"Erro ao atualizar host: {update_response.text}")
        else:
            st.error("Erro ao carregar lista de hosts para edição.")

def logout():
    if st.sidebar.button("Sair"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

def run():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        logout()
        main_app()
    else:
        login_page()

if __name__ == "__main__":
    run()
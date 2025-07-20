import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL") # <-- PASSAR URL VIA .env

menu = ["Listar Hosts", "Editar Host"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Listar Hosts":
    st.subheader("Lista de Hosts")
    response = requests.get(f"{API_URL}/api/v1/inventory")
    print(response.status_code)
    if response.status_code == 200 or response.status_code == 201:
        hosts = response.json()
        for host in hosts:
            st.write(f"**{host['hostname']}** - {host['ipv4']}")
    else:
        st.error("Erro ao buscar hosts")

elif choice == "Editar Host":
    st.subheader("Editar Host")
    hostname = st.text_input("Hostname para editar")
    if st.button("Carregar"):
        response = requests.post(f"{API_URL}/hosts/hostname", json={"hostname": hostname})
        if response.status_code == 200 or response.status_code == 201:
            host = response.json()
            ipv4 = st.text_input("IPv4", host.get("ipv4",""))
            so = st.text_input("SO", host.get("so",""))
            ## ADICIONAR O RESTANTE DOS PARAMETROS
            if st.button("Salvar"):
                update_response = requests.post(f"{API_URL}/api/v1/inventory/{hostname}", json={
                    "ipv4": ipv4,
                    "so": so
                    ## ADICIONAR O RESTANTE DOS PARAMETROS
                })
                if update_response.status_code == 200 or update_response.status_code == 201:
                    st.success("Host atualizado com sucesso!!")
                else:
                    st.error("Erro ao atualizar host")
        else:
            st.error("Host não encontrado")

import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

API_URL = os.getenv("API_URL") # <-- PASSAR URL VIA .env

st.set_page_config(
    page_title="Dashboard Inventory",
    page_icon="🖥️",
    layout="wide",  # 👈 permite usar largura total
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

            # # Opcional: ordena por hostname
            # dataFrame = dataFrame.sort_values(by="hostname")
            
            # Ordena as colunas
            ordered_columns = ["hostname","ipv4","distribution","so","up_time","mem_free","mem_total","mac_address","arch","processor","created_at","updated_at","notes","app_language","app_system","env","is_internal","location","midleware","url"]
            dataFrame = dataFrame[ordered_columns]

            # Mostra tabela interativa
            st.dataframe(dataFrame, use_container_width=True)
            # for host in hosts:
            #     st.write(f"**{host['hostname']}** - {host['ipv4']}")
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
            selected_host = st.selectbox("Selecione o Host para editar", hostnames)

            # Busca dados completos de host selecionado
            host_data = next(host for host in hosts if host['hostname'] == selected_host)

            st.write("Edite os campos abaixo:")

            # Cria inputs para os campos editáveis
            ipv4 = st.text_input("IPv4", value=host_data.get("ipv4", ""), disabled=True)
            st.markdown(f"**IPv4:** {host_data.get('ipv4', '')}")
            st.code(host_data.get("ipv4", ""))
            distribution = st.text_input("Distribuição", value=host_data.get("distribution", ""), disabled=True)
            so = st.text_input("Sistema Operacional", value=host_data.get("so", ""), disabled=True)
            up_time = st.text_input("Uptime", value=host_data.get("up_time", ""), disabled=True)
            mem_free = st.text_input("Memória Livre", value=host_data.get("mem_free", ""), disabled=True)
            mem_total = st.text_input("Memória Total", value=host_data.get("mem_total", ""), disabled=True)
            mac_address = st.text_input("MAC Address", value=host_data.get("mac_address", ""), disabled=True)
            arch = st.text_input("Architecture", value=host_data.get("arch", ""), disabled=True)
            processor = st.text_input("Processor", value=host_data.get("processor", ""), disabled=True)
            url = st.text_input("URL", value=host_data.get("url", ""))
            notes = st.text_input("Descrição", value=host_data.get("notes", ""))
            app_language = st.text_input("Linguagem App", value=host_data.get("app_language", ""))
            app_system = st.text_input("Sistema App", value=host_data.get("app_system", ""))
            env = st.text_input("Ambiente", value=host_data.get("env", ""))
            is_internal = st.text_input("Interno?", value=host_data.get("is_internal", ""))
            location = st.text_input("Local", value=host_data.get("location", ""))
            midleware = st.text_input("Midlleware", value=host_data.get("midleware", ""))

            if st.button("Salvar alterações"):
                payload = {
                    "hostname": selected_host,
                    "ipv4": ipv4,
                    "arch": arch,
                    "processor": processor,
                    "so": so,
                    "distribution": distribution,
                    "mem_total": mem_total,
                    "mem_free": mem_free,
                    "up_time": up_time,
                    "mac_address": mac_address,
                    "url": url,
                    "notes": notes,
                    "app_language": app_language,
                    "app_system": app_system,
                    "env": env,
                    "is_internal": is_internal,
                    "location": location,
                    "midleware": midleware
                }

                update_response = requests.post(f"{API_URL}/api/v1/inventory", json=payload)

                if update_response.status_code in (200, 201):
                    st.success("Host atualizado com sucesso!")
                else:
                    st.error(f"Erro ao atualizar host: {update_response.text}")
    else:
        st.error("Erro ao carregar lista de hosts para edição.")

    # hostname = st.text_input("Hostname para editar")
    # if st.button("Carregar"):
    #     response = requests.post(f"{API_URL}/hosts/hostname", json={"hostname": hostname})
    #     if response.status_code == 200 or response.status_code == 201:
    #         host = response.json()
    #         ipv4 = st.text_input("IPv4", host.get("ipv4",""))
    #         so = st.text_input("SO", host.get("so",""))
    #         ## ADICIONAR O RESTANTE DOS PARAMETROS
    #         if st.button("Salvar"):
    #             update_response = requests.post(f"{API_URL}/api/v1/inventory/{hostname}", json={
    #                 "ipv4": ipv4,
    #                 "so": so
    #                 ## ADICIONAR O RESTANTE DOS PARAMETROS
    #             })
    #             if update_response.status_code == 200 or update_response.status_code == 201:
    #                 st.success("Host atualizado com sucesso!!")
    #             else:
    #                 st.error("Erro ao atualizar host")
    #     else:
    #         st.error("Host não encontrado")

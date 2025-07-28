import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

def listar_hosts():
    st.subheader("Lista de Hosts")

    # Protege página com token de login do usuário logado
    headers = {"Authorization": f"Bearer {st.session_state['jwt_token']}"}
    
    try:
        response = requests.get(f"{API_URL}/api/v1/inventory", headers=headers)

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
    except Exception as e:
        st.error(f"Erro: {e}")

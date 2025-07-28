import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

def editar_host():
    st.subheader("Editar de Host")

    # Protege página com token de login do usuário logado
    headers = {"Authorization": f"Bearer {st.session_state['jwt_token']}"}

    try:
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
    except Exception as e:
        st.error(f"Erro: {e}")

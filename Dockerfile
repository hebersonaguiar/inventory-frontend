# Usa uma imagem base leve do Python
FROM python:3.12-slim

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza pacotes e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libffi-dev \
    libpq-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório da aplicação
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala os requisitos
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando padrão ao iniciar o container
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

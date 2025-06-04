Passo a passo detalhado do projeto agente_csv_i2a2

Este documento apresenta uma descrição completa, explicada passo a passo, de tudo que foi realizado até o momento no projeto do Desafio 2 - I2A2, com o agente inteligente interpretando dados em CSV.

1. Criação da pasta do projeto

No terminal:

mkdir agente_csv_i2a2
cd agente_csv_i2a2

Criamos uma pasta exclusiva para o projeto e entramos nela.

2. Inicialização do Git

git init

Prepara o repositório local para versionamento com Git.

Se ainda não tiver repositório remoto:

git remote add origin https://github.com/Rodrigo-RRC/agente_csv_i2a2.git

3. Criação do .gitignore

type nul > .gitignore
notepad .gitignore

Adicionamos ao .gitignore:

.env
venv/
__pycache__/

Esses arquivos e pastas não devem ir para o GitHub.

4. Criação do ambiente virtual

python -m venv venv
venv\Scripts\activate

Criação e ativação de ambiente virtual exclusivo do projeto.

5. Instalação das bibliotecas

pip install langchain langchain-community openai python-dotenv

Instalação das dependências essenciais:

langchain: motor para criar agentes inteligentes

langchain-community: integrações com modelos (OpenAI, etc.)

openai: acesso à API da OpenAI

python-dotenv: carrega a chave da API de forma segura

6. Criação do arquivo .env

type nul > .env
notepad .env

Conteúdo do arquivo:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

Serve para proteger sua chave de API.

7. Criação do main.py

type nul > main.py
notepad main.py

Conteúdo atualizado do main.py:

from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializa o modelo da OpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key, temperature=0.3)

# Define a pergunta do usuário
mensagem = HumanMessage(content="O que é uma nota fiscal?")

# Envia para o modelo e imprime resposta
resposta = llm.invoke([mensagem])
print("\n💬 Resposta do agente:")
print(resposta.content)

8. Commit e push para o GitHub

git add .
git commit -m "Criação inicial com ambiente, .env e main.py"
git push origin main

Atualizamos o repositório com todas as configurações iniciais.

9. Criação da pasta dados e upload do .zip

mkdir dados
type nul > dados\.gitkeep
# upload manual do arquivo 202401_NFs.zip para a pasta dados/

O arquivo .gitkeep foi criado para versionar a pasta vazia no Git.

10. Criação do agente_csv.py para descompactar o .zip

type nul > agente_csv.py
notepad agente_csv.py

Conteúdo atualizado do agente_csv.py:

import os
import zipfile

def descompactar_arquivo(nome_zip, pasta_base="dados"):
    """
    Descompacta o arquivo ZIP informado dentro da pasta 'dados/descompactado/{nome_zip_sem_extensao}'.
    """
    caminho_zip = os.path.join(pasta_base, nome_zip)

    if not os.path.exists(caminho_zip):
        print(f"❌ Arquivo ZIP '{nome_zip}' não encontrado em '{pasta_base}/'.")
        return None

    nome_pasta_saida = os.path.splitext(nome_zip)[0]
    pasta_saida = os.path.join(pasta_base, "descompactado", nome_pasta_saida)

    os.makedirs(pasta_saida, exist_ok=True)

    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_saida)

    arquivos_extraidos = os.listdir(pasta_saida)

    print(f"✅ Arquivo '{nome_zip}' descompactado com sucesso!")
    print(f"📂 Arquivos extraídos em '{pasta_saida}':")
    for arquivo in arquivos_extraidos:
        print("   └──", arquivo)

    return pasta_saida  # importante para próximos passos

# Execução direta (para testes manuais)
if __name__ == "__main__":
    descompactar_arquivo("202401_NFs.zip")

11. Execução do agente descompactador

python agente_csv.py

Resultado esperado:

✅ Arquivo '202401_NFs.zip' descompactado com sucesso!
📂 Arquivos extraídos em 'dados\\descompactado\\202401_NFs':
   └── 202401_NFs_Cabecalho.csv
   └── 202401_NFs_Itens.csv

12. Commit do agente_csv.py

git add agente_csv.py
git commit -m "Função descompactar_arquivo modularizada com retorno do caminho da pasta extraída"
git push origin main


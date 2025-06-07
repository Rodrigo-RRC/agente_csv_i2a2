# Passo a passo detalhado do projeto agente_csv_i2a2

Este documento apresenta uma descrição completa, explicada passo a passo, de tudo que foi realizado até o momento no projeto do Desafio 2 - I2A2, com o agente inteligente interpretando dados em CSV.

---

## 📁 Criação da pasta do projeto

```bash
mkdir agente_csv_i2a2
cd agente_csv_i2a2
```

---

## 🔄 Inicialização do Git

```bash
git init
git remote add origin https://github.com/Rodrigo-RRC/agente_csv_i2a2.git
```

---

## 📂 Criação do .gitignore

```bash
type nul > .gitignore
notepad .gitignore
```

Conteúdo do `.gitignore`:

```
.env
venv/
__pycache__/
```

---

## 🐍 Criação do ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 📦 Instalação das bibliotecas

```bash
pip install langchain langchain-community openai python-dotenv
```

---

## 🔐 Criação do arquivo .env

```bash
type nul > .env
notepad .env
```

Conteúdo do arquivo:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🧠 Criação do main.py

```bash
type nul > main.py
notepad main.py
```

Conteúdo atualizado do `main.py`:

```python
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

from agente_inteligente.ler_csv import ler_csvs_notas

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

df_cabecalho, df_itens = ler_csvs_notas()

print("\n📄 Amostra do cabeçalho das notas fiscais:")
print(df_cabecalho.head())

print("\n📦 Amostra dos itens das notas fiscais:")
print(df_itens.head())

pergunta = f"Quantas notas fiscais foram emitidas no total neste conjunto de dados? O arquivo contém {len(df_cabecalho)} registros."

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    temperature=0.3
)

mensagem = HumanMessage(content=pergunta)
resposta = llm.invoke([mensagem])

print("\n💬 Resposta do agente:")
print(resposta.content)
```

---

## 💾 Commit inicial

```bash
git add .
git commit -m "Criação inicial com ambiente, .env e main.py"
git push origin main
```

---

## 📦 Criação da pasta `dados` e upload do .zip

```bash
mkdir dados
type nul > dados\.gitkeep
```

Upload manual do arquivo `202401_NFs.zip` para a pasta `dados/`.

---

## 📂 Criação do `agente_csv.py` para descompactar o .zip

```bash
type nul > agente_csv.py
notepad agente_csv.py
```

Conteúdo:

```python
import os
import zipfile

def descompactar_arquivo(nome_zip, pasta_base="dados"):
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

    return pasta_saida

if __name__ == "__main__":
    descompactar_arquivo("202401_NFs.zip")
```

Execução para testes:

```bash
python agente_inteligente\agente_csv.py
```

---

## ✅ Commit do descompactador

```bash
git add agente_csv.py
git commit -m "Função descompactar_arquivo modularizada com retorno do caminho da pasta extraída"
git push origin main
```

---

## 📁 Criação da pasta `agente_inteligente` e reorganização dos arquivos

```bash
mkdir agente_inteligente
type nul > agente_inteligente\__init__.py
move agente_csv.py agente_inteligente\
move ler_csv.py agente_inteligente\
```

---

## 📄 Criação do `ler_csv.py`

```bash
type nul > agente_inteligente\ler_csv.py
notepad agente_inteligente\ler_csv.py
```

Conteúdo:

```python
import pandas as pd
import os

def ler_csvs_notas(caminho_base="dados/descompactado"):
    try:
        caminho_cabecalho = os.path.join(caminho_base, "202401_NFs_Cabecalho.csv")
        caminho_itens = os.path.join(caminho_base, "202401_NFs_Itens.csv")

        df_cabecalho = pd.read_csv(caminho_cabecalho, sep=';', encoding='utf-8')
        df_itens = pd.read_csv(caminho_itens, sep=';', encoding='utf-8')

        print("✅ Arquivos CSV lidos com sucesso.")
        return df_cabecalho, df_itens

    except Exception as e:
        print(f"❌ Erro ao ler arquivos CSV: {e}")
        return None, None
```

---

## 🔁 Commit da reorganização

```bash
git add .
git commit -m "Criação da pasta agente_inteligente e reorganização dos módulos"
git push origin main
```

# README\_COMANDOS.md

Este arquivo documenta os **comandos utilizados no terminal (CMD)** durante o desenvolvimento do projeto `agente_csv_i2a2`, até a etapa 6. Ele será atualizado à medida que o projeto evoluir.

---

## 📁 Criação do diretório do projeto

```bash
mkdir agente_csv_i2a2
cd agente_csv_i2a2
```

---

## 🧪 Inicialização do Git

```bash
git init
git remote add origin https://github.com/Rodrigo-RRC/agente_csv_i2a2.git
```

---

## ⚙️ Criação de arquivos vazios

```bash
type nul > .gitignore
notepad .gitignore

# Conteúdo do .gitignore:
.env
venv/
__pycache__/

# Outros arquivos
type nul > main.py
notepad main.py

type nul > .env
notepad .env
```

---

## 🐍 Criação e ativação do ambiente virtual (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 📦 Instalação das bibliotecas essenciais

```bash
pip install langchain langchain-community openai python-dotenv
```

---

## 🧪 Teste de instalação (listar pacotes)

```bash
pip list
```

---

## 🧹 Limpar terminal (CMD ou PowerShell)

```bash
cls
```

---

## 🗑️ Deletar arquivos incorretos

```bash
del ".env]"
```

---

## 🧾 Git: Adicionar, commit e push

```bash
git add .
git commit -m "Criação inicial com ambiente, .env e main.py"
git push origin main
```

---

## ▶️ Execução do script principal

```bash
python main.py
```

---

Este documento será mantido atualizado conforme o desenvolvimento do agente evolui nas próximas etapas.

Próxima etapa: leitura de CSV com Pandas e integração com LangChain.

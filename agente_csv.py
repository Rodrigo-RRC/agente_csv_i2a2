# agente_csv.py
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

import os
import zipfile

def descompactar_arquivo(nome_arquivo_zip, pasta_raiz="dados"):
    """
    Recebe o nome de um arquivo ZIP e descompacta na pasta:
    dados/descompactado/NOME_DO_ARQUIVO_SEM_ZIP
    """
    caminho_completo_zip = os.path.join(pasta_raiz, nome_arquivo_zip)

    if not os.path.exists(caminho_completo_zip):
        print(f"❌ Arquivo '{nome_arquivo_zip}' não encontrado dentro de '{pasta_raiz}/'")
        return None

    nome_base_sem_extensao = os.path.splitext(nome_arquivo_zip)[0]
    pasta_destino = os.path.join(pasta_raiz, "descompactado", nome_base_sem_extensao)

    os.makedirs(pasta_destino, exist_ok=True)

    with zipfile.ZipFile(caminho_completo_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)

    arquivos_extraidos = os.listdir(pasta_destino)

    print(f"✅ Arquivo '{nome_arquivo_zip}' descompactado com sucesso!")
    print(f"📂 Arquivos extraídos em '{pasta_destino}':")
    for nome_arquivo in arquivos_extraidos:
        print("   └──", nome_arquivo)

    return pasta_destino

# Execução direta para testes manuais
if __name__ == "__main__":
    descompactar_arquivo("202401_NFs.zip")

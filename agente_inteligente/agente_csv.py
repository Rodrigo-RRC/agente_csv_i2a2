import os
import zipfile

def descompactar_arquivo(nome_arquivo_zip, pasta_raiz="dados"):
    """
    Descompacta o arquivo ZIP para a subpasta 'dados/descompactado/NOME_SEM_ZIP/',
    somente se ainda não tiver sido descompactado.
    """
    # Caminho completo do arquivo zipado
    caminho_zip = os.path.join(pasta_raiz, nome_arquivo_zip)

    if not os.path.exists(caminho_zip):
        print(f"❌ Arquivo '{nome_arquivo_zip}' não encontrado em '{pasta_raiz}/'")
        return None

    # Nome base (sem extensão .zip)
    nome_base = os.path.splitext(nome_arquivo_zip)[0]

    # Caminho de destino (subpasta com nome do zip)
    pasta_destino = os.path.join(pasta_raiz, "descompactado", nome_base)

    # Verifica se já existe a subpasta com arquivos
    if os.path.exists(pasta_destino) and os.listdir(pasta_destino):
        print(f"📦 Arquivo '{nome_arquivo_zip}' já foi descompactado. Pulando etapa...")
        return pasta_destino

    # Cria a pasta se não existir
    os.makedirs(pasta_destino, exist_ok=True)

    # Descompacta
    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.extractall(pasta_destino)

        arquivos_extraidos = os.listdir(pasta_destino)

        print(f"✅ Arquivo '{nome_arquivo_zip}' descompactado com sucesso!")
        print(f"📂 Arquivos extraídos em '{pasta_destino}':")
        for nome_arquivo in arquivos_extraidos:
            print("   └──", nome_arquivo)

        return pasta_destino

    except Exception as e:
        print(f"❌ Erro ao descompactar '{nome_arquivo_zip}': {e}")
        return None

# Execução direta para testes manuais
if __name__ == "__main__":
    descompactar_arquivo("202401_NFs.zip")

import os
import shutil

# Caminho da pasta que você quer organizar
pasta_alvo = "C:\\Users\joaovictor.rosa\\OneDrive - Dataprev\\Automacao\\CompararOrigTransf"  # coloque aqui o caminho da sua pasta

# Extensões que você quer organizar
tipos_de_arquivos = {
    "Imagens": [".jpg", ".jpeg", ".png"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Executáveis": [".exe"],
    "Compactados": [".zip", ".rar"],
}

# Criar pastas se não existirem e mover os arquivos
for arquivo in os.listdir(pasta_alvo):
    caminho_arquivo = os.path.join(pasta_alvo, arquivo)

    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)

        for tipo, extensoes in tipos_de_arquivos.items():
            if extensao.lower() in extensoes:
                pasta_destino = os.path.join(pasta_alvo, tipo)

                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                print(f"Movido {arquivo} para {tipo}")
                break

import os
import json
from image_analyzer import analisar_imagem
from db import init_db, inserir_resultado

# Iniciar o banco de dados
init_db()

# Carregar parâmetros
with open("parametros.json", "r") as f:
    parametros = json.load(f)

pasta_imagens = "imagens/"

for imagem in os.listdir(pasta_imagens):
    if imagem.endswith(".jpg") or imagem.endswith(".png"):
        caminho = os.path.join(pasta_imagens, imagem)
        proporcao = analisar_imagem(caminho)

        if proporcao >= parametros["limite_verde"]:
            classificacao = "Saudável"
        elif proporcao <= parametros["limite_vermelho"]:
            classificacao = "Com Problemas"
        else:
            classificacao = "Regular"

        print(f"{imagem}: {classificacao} ({proporcao * 100:.2f}% verde)")
        inserir_resultado(imagem, proporcao, classificacao)

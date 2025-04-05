import requests
import json
from time import sleep

NOTICIAS_JOGATINA = "C:\/Users\/amand\/OneDrive\/Documentos\/Pos-Graduacao\/Segundo semestre\/Desenvolvimento de Aplicações Orientadas a Serviços\/day-01\/servico-4\/noticias\/jogatinas.json"
NOTICIAS_SISTEMAS = "C:\/Users\/amand\/OneDrive\/Documentos\/Pos-Graduacao\/Segundo semestre\/Desenvolvimento de Aplicações Orientadas a Serviços\/day-01\/servico-4\/noticias\/sistemas.json"

URL_JOGATINA = "http://localhost:5001/gravar"
URL_SISTEMAS = "http://localhost:5002/gravar"

def enviar(url, arquivo_noticias):
    sucesso = False

    with open(arquivo_noticias, "r") as arquivo:
        conteudo = json.load(arquivo)
        print(f"conteudo = {conteudo}")
        noticias = conteudo["noticias"]

        arquivo.close()

        resposta = requests.post(url, json=json.dumps(noticias))

        sucesso = resposta.status_code == 201

    return sucesso

if __name__ == "__main__":
    while True:
        sucesso = enviar(URL_JOGATINA, NOTICIAS_JOGATINA)
        if sucesso:
            print("noticias sobre Jogos Eletrôncios enviadas")
        else:
            print("Erro ao enviar noticias sobre jogos eletrônicos")

        sucesso = enviar(URL_SISTEMAS, NOTICIAS_SISTEMAS)
        if sucesso:
            print("noticias sobre Sistemas operacionais enviadas")
        else:
            print("Erro ao enviar noticias sobre Sistemas operacionais")

        sleep(10)

# rodar a cli abaixo
# python crawler.py
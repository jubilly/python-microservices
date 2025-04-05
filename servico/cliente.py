import urllib.request as requisicao
import json
from time import sleep

URL_SERVICO = "http://localhost:5000"
URL_JOGATINA = f"{URL_SERVICO}/jogatina"
URL_SISTEMAS = f"{URL_SERVICO}/sistemas"
URL_ALIVE = f"{URL_SERVICO}/alive"

def acessar(url):
    sucesso, conteudo = False, None
    try:
        resposta = requisicao.urlopen(url)
        conteudo = resposta.read().decode("utf-8")
        sucesso = True
    except Exception as error:
        print(f"Ocorreu um erro acessando a URL: {url}")

    return sucesso, conteudo

def get_jogatina():
    sucesso, noticias = acessar(URL_JOGATINA)
    if sucesso:
        noticias = json.loads(noticias)

    return sucesso, noticias

def get_sistemas():
    sucesso, noticias = acessar(URL_SISTEMAS)
    if sucesso:
        noticias = json.loads(noticias)

    return sucesso, noticias

def imprimir(tipo_noticias, noticias):
    print(f"Ultimas noticias sobre {tipo_noticias}")
    for contador, noticia in enumerate(noticias):
        print(f"#{contador + 1}: {noticia}")

def servico_alive():
    sucesso, alive = acessar(URL_ALIVE)

    return sucesso and alive == "sim"

if __name__ == "__main__":
    while True:

        if servico_alive():

            sucesso, noticias = get_jogatina()
            if sucesso:
                imprimir("Jogos eletronicos", noticias)
            else:
                print("Não há noticias disponíveis")

            sucesso, noticias = get_sistemas()
            if sucesso:
                imprimir("Sistemas operacionais", noticias)
            else:
                print("Não existem noticias de sistemas")
        else:
            print("Serviço de noticias indisponível!")

        sleep(3)
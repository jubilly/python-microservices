import urllib.request as requisicao
import json
from time import sleep

URL_JOGATINA = "http://localhost:5001"
URL_JOGATINA_NOTICIAS = f"{URL_JOGATINA}/noticias"
URL_JOGATINA_ALIVE = f"{URL_JOGATINA}/alive"

URL_SISTEMAS = "http://localhost:5002"
URL_SISTEMAS_NOTICIAS = f"{URL_SISTEMAS}/noticias"
URL_SISTEMAS_ALIVE = f"{URL_SISTEMAS}/alive"

def acessar(url):
    sucesso, conteudo = False, None
    try:
        resposta = requisicao.urlopen(url)
        if resposta.code == 200:
            conteudo = resposta.read().decode("utf-8")
            sucesso = True
    except Exception as error:
        print(f"Ocorreu um erro acessando a URL: {url}")

    return sucesso, conteudo

def get_jogatina():
    sucesso, noticias = acessar(URL_JOGATINA_NOTICIAS)
    if sucesso:
        noticias = json.loads(noticias)
        sucesso = sucesso and bool(noticias)

    return sucesso, noticias

def get_sistemas():
    sucesso, noticias = acessar(URL_SISTEMAS_NOTICIAS)
    if sucesso:
        noticias = json.loads(noticias)
        sucesso = sucesso and bool(noticias)

    return sucesso, noticias

def imprimir(tipo_noticias, noticias):
    print(f"Ultimas noticias sobre {tipo_noticias}")
    for contador, noticia in enumerate(noticias):
        print(f"#{contador + 1}: {noticia}")

def servico_jogatinas_alive():
    sucesso, alive = acessar(URL_JOGATINA_ALIVE)

    return sucesso and alive == "sim"

def servico_sistemas_alive():
    sucesso, alive = acessar(URL_SISTEMAS_ALIVE)

    return sucesso and alive == "sim"

if __name__ == "__main__":
    while True:

        if servico_jogatinas_alive():

            sucesso, noticias = get_jogatina()
            if sucesso:
                imprimir("Jogos eletronicos", noticias)
            else:
                print("Não há noticias disponíveis")

        else:
            print("Serviço de noticias sobre Jogos eletrônicos está indisponível!")

        if servico_sistemas_alive():
                
            sucesso, noticias = get_sistemas()
            if sucesso:
                imprimir("Sistemas operacionais", noticias)
            else:
                print("Não existem noticias de sistemas")
        else:
            print("Serviço de noticias sobre Sistemas operacionais está indisponível")

        sleep(3)

# rodar a cli abaixo
# python cliente.py
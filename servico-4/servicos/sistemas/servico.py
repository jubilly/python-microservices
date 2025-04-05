from flask import Flask, Response, request
from pymemcache.client import base
import json

VERSAO = "1.0"
INFO = {
  "descricao": "servico que disponibiliza noticias sobre Sistemas Operacionais",
  "autor": "Amanda Prates",
  "versao": VERSAO
}

BANCO_NOTICIAS = "db_sistemas"
PORTA_BANCO = 11211

ALIVE = "sim"

servico = Flask("noticias")

@servico.get("/")
def get():
  return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/info")
def get_info():
  return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/alive")
def is_alive():
  return Response(ALIVE, status=200, mimetype="text/plain")

@servico.post("/gravar")
def gravar_jogatina():
  sucesso, noticias = False, request.get_json()

  try:
    cliente = base.Client((BANCO_NOTICIAS, PORTA_BANCO))
    cliente.set("sistemas", noticias)
    cliente.close()

    sucesso = True
  except Exception as error:
    print(f"Error = {str(error)}")

  return Response(status=201 if sucesso else 422)

@servico.get("/noticias")
def get_sistemas():
  sucesso, noticias = False, None

  try:

    cliente = base.Client((BANCO_NOTICIAS, PORTA_BANCO))
    noticias = cliente.get("sistemas")
    if noticias is None:
        noticias = []

    cliente.close()

    sucesso = True
  except Exception as error:
    print(f"ocorreu um erro acessando as noticias de jogatina, {error}")

  return Response("{}" if noticias is None else noticias, status=200 if sucesso else 204, mimetype="application/json")

if __name__ == "__main__":
  servico.run(host="0.0.0.0", debug=True)
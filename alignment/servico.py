from flask import Flask

servico = Flask(__name__)

@servico.get("/info")
def get_info():
    return "teste em servico web"

if __name__ == "__main__":
    servico.run()
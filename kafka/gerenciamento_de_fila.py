from kafka import KafkaClient, KafkaProducer
from faker import Faker
import random
import json

ESPECIALIDADES = ["ortopedista", "cardiologista", "endocrinologista", "urologista", "pneumologistsa"]
TOTAL_PACIENTES = 20

print(f"Rodando...")

def iniciar_fila_atendimento():

    iniciada = False

    try:
        cliente = KafkaClient(
            bootstrap_servers =["localhost:9092"], 
            api_version = (0, 10, 1)
        )
        cliente.add_topic("pacientes")
        cliente.close()

        iniciada = True

    except Exception as error:
        print(f"erro iniciando fila de atendimento: {str(error)}")

    return iniciada
    
def gerar_paciente_ficticio():
    fake = Faker("pt_BR")

    nome = fake.name()
    endereco = fake.address()
    idade = random.randint(14, 100)
    especialidade = random.choice(ESPECIALIDADES)
    return {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "especialidade": especialidade
    }

def on_sucesso(mensagem_de_sucesso):
    print(f"sucesso enviando paciente: {mensagem_de_sucesso}")

def on_erro(_):
    print(f"erro enviando paciente")

def gerar_fila_atendimento():
    produtor = KafkaProducer(
        bootstrap_servers = ["localhost:9092"], 
        api_version = (0, 10, 1)
    )

    for _ in range(TOTAL_PACIENTES):
        paciente = gerar_paciente_ficticio()
        print(f"enviando paciente {paciente['nome']} para a fila do {paciente['especialidade']}")

        envio = produtor.send(topic='pacientes', value=json.dumps(paciente).encode("utf-8"))
        envio.add_callback(on_sucesso).add_errback(on_erro)

        produtor.flush()

    produtor.close()

if __name__ == "__main__": 
    iniciada = iniciar_fila_atendimento()
    if iniciada:
        gerar_fila_atendimento()
    else:
        print("Fila de atendimento não iniciada.")
# rodar a cli abaixo
# python gerenciamento_de_fila.py
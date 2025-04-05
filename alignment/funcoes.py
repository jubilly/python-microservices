def somar(numero_a, numero_b):
    resultado = numero_a + numero_b

    return resultado

def somar_e_multiplcar(numero_a, numero_b):
    multiplicacao = numero_a * numero_b
    soma = numero_a + numero_b

    return multiplicacao, soma



if __name__ == "__main__":
    resulado = somar(2, 3)
    abobora, batata = somar_e_multiplcar(4, 5)
    _, multiplicacao = somar_e_multiplcar(6,7) #o _ é uma boa pratica para mostrar para o desenvolvedor que o primeiro retorno está sendo ignorado
    print(f"resultado = { resulado}")
    print(f"multiplicacao = {abobora}")
    print(f"multiplicacao = {multiplicacao}")
    print(f"soma = {batata}")
FRUTAS = [
    "banana",
    "abacaxi",
    "manga",
    "goiaba",
    "maçã"
]

if __name__ == "__main__":
    # print(f"lista de frutas: {FRUTAS}")
    # for fruta in FRUTAS:
    #     print(f"{fruta} é uma fruta")
    # FRUTAS.append("melância")
    # for fruta in FRUTAS:
    #     print(f"{fruta} é uma fruta")

    FRUTAS.append("melância")
    for index, fruta in enumerate(FRUTAS):
        print(f"{fruta} é uma fruta na posicao {index}")
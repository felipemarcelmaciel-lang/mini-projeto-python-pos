from functools import reduce

def analisar(lista, limite) -> dict:
    """
    Filtra números pares maiores que o limite,
    eleva ao quadrado e calcula soma, contagem e média inteira.
    """
    filtrados = filter(lambda x: x % 2 == 0 and x > limite, lista)
    quadrados = map(lambda x: x ** 2, filtrados)

    def acumulador(acc, valor):
        soma, contagem = acc
        return soma + valor, contagem + 1

    soma, contagem = reduce(acumulador, quadrados, (0, 0))

    media = soma // contagem if contagem > 0 else 0

    return {
        "soma_quadrados": soma,
        "contagem": contagem,
        "media_inteira": media
    }
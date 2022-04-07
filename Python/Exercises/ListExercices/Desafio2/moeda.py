def moeda(value, monetary):
    aumentado = aumentar(value, 10)
    diminuido = diminuir(value, 10)
    cortado = metade(value,2)
    dobrado = dobro(value, 2)
    print(f'Valor: {monetary} {str(value).replace(".", ",")} aumentado: {monetary} {str(aumentado).replace(".", ",")}')
    print(f'Valor: {monetary} {str(value).replace(".", ",")} diminuido: {monetary} {str(diminuido).replace(".", ",")}')
    print(f'Metade: {monetary} {str(cortado).replace(".", ",")}')
    print(f'Dobro: {monetary} {str(dobrado).replace(".", ",")}')


def aumentar(value, n):
    value += n
    return value


def diminuir(value, n):
    value -= n
    return value


def dobro(value, n):
    value *= n
    return value


def metade(value, n):
    value /= n
    return value
def area(l, c):
    a = l * c
    print(f'Largura: {l}')
    print(f'Comprimento: {c}')
    print(f'A área total: {a}m²')


if __name__ == '__main__':
    largura = int(input('Digite a largura: '))
    comprimento = int(input('Digite o comprimento: '))
    area(largura, comprimento)


def maior(lista):
    print('Analisando Valores ')
    print(lista)
    print(f'O maior valor é: {max(lista)}')
    print('-='*20)

if __name__ == '__main__':
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    maior(valores)

    valores2 = [4, 1, 5, 67, 4, 2, 7, 8, 87, 99]
    maior(valores2)

    valores = [7]
    maior(valores)
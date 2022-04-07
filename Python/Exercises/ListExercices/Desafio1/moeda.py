from utils import *

if __name__ == '__main__':
    balance = float(input("Balanço?: "))
    impost = float(input('Taxa: '))
    print(f'Valor aumentado: {aumentar(balance, impost)}')
    print(f'Valor diminuido: {diminuir(balance, impost)}')
    print(f'Valor dobro: {dobro(balance, 2)}')
    print(f'Valor metade: {metade(balance, 2)}')

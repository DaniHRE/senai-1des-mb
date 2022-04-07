list = []
listpar = []
listimpar = []

while True:
    num = int(input('Digite um número: '))
    list.append(num)
    if num % 2 == 0:
        listpar.append(num)
    elif num % 2 == 1:
        listimpar.append(num)
    opUser = str(input("Quer continuar: [S/N]")).strip().upper()
    if opUser == "S":
        continue
    elif opUser == "N":
        break
    else:
        break

print(f"Normal: {list}")
print(f"Pares: {listpar}")
print(f"Impares: {listimpar}")

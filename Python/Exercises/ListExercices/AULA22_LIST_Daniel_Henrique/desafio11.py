alunos = list()

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota1: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    op_usuario = input("Deseja continuar? [S/N]").lower().strip().replace(" ", "")
    if op_usuario in 'Nn':
        break
print("="*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print("=" * 30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    op_us = int(input("Mostrar a nota de qual aluno? [999 para encerrar]"))
    if op_us == 999:
        break
    if op_us <= len(alunos) - 1:
        print(f"Notas de {alunos[op_us][0]} são {alunos[op_us][1]}")
        print()
print("Keker")





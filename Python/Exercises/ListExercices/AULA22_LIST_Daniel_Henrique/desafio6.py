expr = str(input("Escreva a expressão: : "))

pilha = []

for parent in expr:
    if parent == '(':
        pilha.append('')
    elif parent == ')':
        if len(parent) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')

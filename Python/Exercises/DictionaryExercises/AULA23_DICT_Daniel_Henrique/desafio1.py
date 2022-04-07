turma = {
    'Aluno': input('Digite o nome: '),
    'Nota': int(input('Digite a nota: '))
}

if turma['Nota'] < 3.9:
    turma['Situação'] = 'Reprovado'
elif turma['Nota'] < 6.9:
    turma['Situação'] = 'Recuperação'
elif turma['Nota'] <= 10:
    turma['Situação'] = 'Aprovado'

print(f"Aluno: {turma['Aluno']} ")
print(f"Nota do {turma['Aluno']}: {turma['Nota']}")
print(f"O {turma['Aluno']} está {turma['Situação']}")

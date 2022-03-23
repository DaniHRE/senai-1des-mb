# Create a dictionary to store some values

dados = {
    'details': {
        'name': 'Roberto',
        'idade': 20,
        'sexo': 'M',
    },
    'functions': {
        'ping': 'pong',
        'print': 'printado',
        'exclude': 'excluded'
    }
}

# while to loop te program
while True:
    print('=======================================')
    print('What u want to see? \x1B[3m[Dict and Property]\x1B[0m')
    print('=======================================')

    # while to input Dict and Property
    while True:
        opDict = input('\033[1mDict:\033[0m ')
        opProp = input('\033[1mProperty:\033[0m ')

        # try to print inserted dict an property
        try:
            print(f'\nThis property is:  {dados[opDict][opProp]}\n')
            break

        # if this condition is invalid, go to KeyError exception
        except KeyError:
            print('\n\033[1m\033[31mThis key value ou property is invalid\033[0m \n')

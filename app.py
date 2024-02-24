from utils import criar_arquivo

# INICIO
name = input('Digite o nome para a planilha: ')
n_lines = int(input('Quantas linhas? '))
n_columns = int(input('Quantas colunas? '))

columns = [{'name': 'ID', 'type': 'number'}]

for n in range(1, n_columns+1):
    col_definition = {}
    col_definition['name'] = input('Nome da coluna ' + str(n) + ': ')
    col_definition['type'] = input('Tipo da coluna ' + str(n) + ' (name, int, phone, email, address, date_birth, choice): ')
    
    if col_definition['type'] == 'choice':
        col_definition['choices'] = []
        keep_moving = True
        
        while keep_moving:
            col_definition['choices'].append(input('Adicionando opção: '))
            keep_moving = False if input('Sair (S/N)? ') == 'S' else True

    columns.append(col_definition)

criar_arquivo(name, n_lines, columns)

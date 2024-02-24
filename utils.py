import openpyxl
import faker
import random

# Inicializa o gerador de dados fictícios
faker_instance = faker.Faker()

# Cria um novo arquivo Excel
workbook = openpyxl.Workbook()


def criar_arquivo(name: str, n_lines: int, columns: list) -> str:
    
    # Seleciona a planilha ativa (por padrão, há uma planilha chamada "Sheet")
    sheet = workbook.active
    
    # Adiciona cabeçalhos à primeira linha
    headers = []
    for col_definition in columns:
        headers.append(col_definition['name'])
    
    sheet.append(headers)

    # Adiciona linhas de dados fictícios
    for i in range(1, n_lines+1):
        row = [i]
        for col_definition in columns:
            if col_definition['name'] == 'ID':
                continue
            
            if 'choices' in col_definition:
                row.append(obter_valor_de_coluna(col_definition['type'], col_definition['choices']))
            else:
                row.append(obter_valor_de_coluna(col_definition['type']))
            
        sheet.append(row)

    # Salva o arquivo Excel
    workbook.save(name + ".xlsx")
    print("Arquivo '" + name + ".xlsx' criado com sucesso.")

def obter_valor_de_coluna(type: str, choices: list = ['']) -> any:
    match type:
        case 'name':
            return faker_instance.name()
        
        case 'int':
            return random.randint(18, 80)
            
        case 'phone':
            return faker_instance.phone_number()
            
        case 'email':
            return faker_instance.email()
            
        case 'address':
            return faker_instance.address()
            
        case 'date_birth':
            return faker_instance.date_of_birth(minimum_age=9, maximum_age=110)
        
        case 'choice':
            return random.choice(choices)
        
        case _:
            return None
            

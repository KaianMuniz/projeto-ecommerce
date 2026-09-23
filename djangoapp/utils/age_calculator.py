from datetime import date

def calcular_idade(data_nascimento):
    hoje = date.today()

    idade = hoje.year - data_nascimento.year

    if hoje.month < data_nascimento.month:
        idade -= 1
    elif hoje.month == data_nascimento.month and hoje.day < data_nascimento.day:
        idade -= 1

    return idade
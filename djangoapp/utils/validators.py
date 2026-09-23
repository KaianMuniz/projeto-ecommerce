from django.core.exceptions import ValidationError
import re
from .age_calculator import calcular_idade

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        raise ValidationError('CPF deve possuir 11 dígitos.')

    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido.')

   
    soma = sum(
        int(cpf[i]) * (10 - i)
        for i in range(9)
    )

    digito_1 = (soma * 10) % 11
    digito_1 = 0 if digito_1 == 10 else digito_1

    if digito_1 != int(cpf[9]):
        raise ValidationError('CPF inválido.')


    soma = sum(
        int(cpf[i]) * (11 - i)
        for i in range(10)
    )

    digito_2 = (soma * 10) % 11
    digito_2 = 0 if digito_2 == 10 else digito_2

    if digito_2 != int(cpf[10]):
        raise ValidationError('CPF inválido.')

def valida_cep(cep):
    cep = re.sub(r'\D', '', cep)

    if len(cep) != 8:
        raise ValidationError('CEP deve possuir 8 dígitos.')

def valida_data_nascimento(data_nascimento):
    idade = calcular_idade(data_nascimento)

    if idade < 18:
        raise ValidationError(
            'Você precisa ter pelo menos 18 anos.'
        )
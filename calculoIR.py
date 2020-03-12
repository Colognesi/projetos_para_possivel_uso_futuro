'''
Codigo realizado para o calculo de IR com base no salario fornecido.
'''


def retorna_Salario(salario, salario_Bruto):
    return print(
        "O seu salario bruto é de: {}, voce recebeu um total de desconto do INSS de: {}".format(salario, round(
            salario_Bruto, 2)))


def total(salario, salario_Bruto):
    total = salario - salario_Bruto
    if tem_dependentes(qtd_dependentes):
        total = total - (dependentes_valor * qtd_dependentes)
    return total


def tem_dependentes(dependentes):
    if dependentes > 0:
        dependentes = True
        return dependentes
    else:
        dependentes = False
        return dependentes


def calculo_IR(total):
    if total >= 1903.99:
        if total == 1903.99 and total <= 2826.65:
            total = aliquotas[3]
            return print("Voce deve retornar {} como Imposto de Renda".format(total))
        elif total == 2826.66 and total <= 3751.05:
            total = aliquotas[2]
            return print("Voce deve retornar {} como Imposto de Renda".format(total))
        elif total == 3751.06 and total <= 4664.68:
            total = aliquotas[1]
            return print("Voce deve retornar {} como Imposto de Renda".format(total))
        else:
            total = aliquotas[0]
            return print("Voce deve retornar {} como Imposto de Renda".format(total))


def valor_desconto_dependentes(valor, qtd):
    valor_dependentes_somado = valor * qtd
    return print("A quantidade total a ser descontado por dependentes é de: " + str(valor_dependentes_somado))


def mensagem_retorno(total):
    return print("Seu salario liquido é de: {}".format(round(total, 2)))


aliquotas = [869.36, 636.13, 354.80, 142.80]
dependentes_valor = 189.59
inss = [0.14, 0.12, 0.09, 0.075]

qtd_dependentes = input("Qual a quantidade de dependentes: ")
qtd_dependentes = int(qtd_dependentes)

salario_Bruto = input("insira seu salario bruto: ")
salario_Bruto = float(salario_Bruto)
salario = salario_Bruto

if salario_Bruto <= 1045.0:
    desconto = salario_Bruto * inss[3]
    retorna_Salario(salario, desconto)
    mensagem_retorno(total(salario, desconto))
    calculo_IR(total(salario, desconto))
    valor_desconto_dependentes(dependentes_valor, qtd_dependentes)

elif 1045.0 < salario_Bruto <= 2089.60:
    desconto = salario_Bruto = inss[2]
    retorna_Salario(salario, desconto)
    mensagem_retorno(total(salario, desconto))
    calculo_IR(total(salario, desconto))
    valor_desconto_dependentes(dependentes_valor, qtd_dependentes)

elif 2089.60 < salario_Bruto <= 3134.40:
    desconto = salario_Bruto * inss[1]
    retorna_Salario(salario, desconto)
    mensagem_retorno(total(salario, desconto))
    calculo_IR(total(salario, desconto))
    valor_desconto_dependentes(dependentes_valor, qtd_dependentes)

else:
    desconto = salario_Bruto * inss[0]
    retorna_Salario(salario, desconto)
    mensagem_retorno(total(salario, desconto))
    calculo_IR(total(salario, desconto))
    valor_desconto_dependentes(dependentes_valor, qtd_dependentes)

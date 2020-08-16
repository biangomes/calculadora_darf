'''
@author: beatriz nascimento gomes
@date: 16-08-2020
@what_is:
    Simulando uma calculadora de documento de arrecadacao da receita federal para operacoes de day trade.
    Estas operacoes correspondem a compra e venda (nao necessariamente nessa ordem) de ativos ou mercado futuro na bolsa
    de valores.

@variaveis:
    lucro_total: ele sera utilizado para receber o lucro das operacoes e sera usado no calculo da darf
    dias_operacao: sera usado para o laço for, pra alimentar a variavel lucro_total
    total_despesas = eh identificado nas notas de corretagem e corresponde a: taxa operacional + registro BMF + taxa BMF
    irrf = imposto da receita
    iss = outra taxa
    valor_negocio = valor bruto de credito ou debito das operacoes feitas
    saldo_liquido: é o valor do negocio subtraído pelo irrf, iss e total_despesas, corresponde ao saldo q será creditado
                   operador
    valor_DARF: corresponde ao valor que o operador deverá pagar à receita federal
'''

lucro_total = 0

dias_operacao = int(input("Quantidade de dias em que você operou: "))
print("Você só contabilizará o lucro.")

for i in range(1, dias_operacao+1):
    print("-" * 50)
    print("Dia ", i)
    total_despesas = float(input("Total das despesas = "))
    irrf = float(input("IRRF = "))
    iss = float(input("ISS = "))
    valor_negocio = float(input("Valor dos negócios = "))
    saldo_liquido = valor_negocio - (total_despesas + irrf + iss)
    lucro_total += saldo_liquido
    # aqui vou so mostrar o resumo dos dados obtidos
    print("O total de despesas foi: R$", total_despesas)
    print("O saldo bruto foi: R$", valor_negocio)
    print("O saldo líquido foi: R$", saldo_liquido)
    print("O lucro total, por enquanto, está no valor de: R$", lucro_total)

print("-"*50)
print("Lembre-se sempre de pagar em dia.")
valor_DARF = 0.2 * lucro_total
print("O valor da sua DARF será igual a: R$", valor_DARF)

if valor_DARF < 10:
    print("Como o valor é inferior a R$10,00, este valor deverá ser acrescentado no seu próximo lucro.")
else:
    print("O valor máximo para pagamento é sempre até o último dia útil do mês seguinte. :)")




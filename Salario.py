print('\033[31m''=' * 51)
print('\033[34m''==.=.=.=.=.= -> ''\033[33m''REAJUSTE SALARIAL''\033[36m'' <- =.=.=.=.=.=.==')
print('\033[36m''=' * 51)
print()

salario = float(input('\033[35m'"Qual é o salário do funcionário? R$"))
if salario <= 2800:
    novo = salario + (salario * 20 / 100)
    velho = novo - salario
    print(f"Para salários de até R$ 2.800,00 o reajuste é de 20%")
elif 2800 < salario <= 7000:
    novo = salario + (salario * 15 / 100)
    velho = novo - salario
    print(f"Para salários de até R$ 7.000,00 o reajuste é de 15%")
elif not (salario <= 7000 or not (salario <= 15000)):
    novo = salario + (salario * 10 / 100)
    velho = novo - salario
    print(f"Para salários de até R$ 15.000,00 o reajuste é de 10%")
else:
    novo = salario + (salario * 5 / 100)
    velho = novo - salario
    print(f"Para salários acima de R$ 15.000,00 o reajuste é de 5%")
print('\033[31m''O salário do funcionário que era de R$ {:.2f}\n'
      '\033[36m''Com o novo aumento, passou a ser de R$ {:.2f}'.format(salario, novo))
print(f"O reajuste foi de R$ {velho:.2f} ")

print()
print('\033[31m''=' * 51)
print('\033[34m''=.=.=.=.= -> ''\033[33m''FIM DO PROGRAMA PYTHON''\033[36m'' <- =.=.=.=.=.=')
print('\033[31m''=' * 51)
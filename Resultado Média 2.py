print('\033[31m''=' * 51)
print('\033[34m ==.= -> \033[35m Lendo três números, maior e menor \033[32m <- =.==')
print('\033[31m''=' * 51)

while True:
    n1 = float(input('\033[32m''Informe a 1ª nota: '))
    n2 = float(input('\033[36m''Informe a 2ª nota: '))
    m = (n1 + n2) / 2
    print('\033[35M''A média das notas {:.1f} e {:.1f} é -> {:.1f}'.format(n1, n2, m))
    if m >= 6:
        print('\033[31m''Aluno APROVADO !!! ')
    elif 4 <= m < 6:
        print('\033[34m''O aluno está em RECUPERAÇÃO !!! ')
    else:
        print('\033[31m''Aluno REPROVADO !!!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[32m''Deseja continuar -> [S/N]? ')).strip().upper()
    if resp == 'N':
        break
print()
print('\033[31m''=' * 51)
print('\033[34m =.=.=.=.= -> \033[33m FIM do PROGRAMA  \033[36m <- =.=.=.=.=')
print('\033[31m''=' * 51)

s = 0
for c in range(0, 15):
        n = int(input('Digite suas médias: '))
        s = s + n
print('A média entre todos os valores é igual a {:.1f}'.format(s/15))
if (n >= 7):
    print('Parabéns, você foi aprovado!')
elif(n < 7):
    print('Reprovado')

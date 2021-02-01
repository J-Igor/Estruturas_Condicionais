cosseno = float(input('Digite o valor do cateto oposto: '))
cateto = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (cosseno ** 2 + cateto ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
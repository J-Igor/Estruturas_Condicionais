a = str(input("Olá, qual seu nome? "))
b = int(input("Digite a sua idade: "))
c = str(input("Digita o seu sexo (M/F): "))

altura = float(input("Digite sua altura (M): "))
peso = float(input("Digite seu peso (Kg): "))

imc = peso / altura**2
 
print("Seu IMC é de {:.1f}".format(imc))
 
if imc < 18.5:
	print("(ABAIXO DO NORMAL) Magreza")
elif imc <= 18.5 and imc < 25:
	print("(NORMAL) Parabéns você está Saudável ")
elif imc <= 25 and imc < 30:
	print("(SOBREPESO) Você está com Obesidade de Grau I ")
elif imc <= 30 and imc < 40:
	print("(OBESIDADE) Você está com Obesidade de Grau II ")
else:
	print("(OBESIDADE GRAVE) Você está com Obesidade de Grau III ")
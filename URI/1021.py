valor = float(input())
print("NOTAS:\n%d nota(s) de R$ 100.00" %(int(valor / 100)))
valor = valor % 100
print("%d nota(s) de R$ 50.00" %(int(valor / 50)))
valor = valor %	 50
print("%d nota(s) de R$ 20.00" %(int(valor / 20)))
valor = valor % 20
print("%d nota(s) de R$ 10.00" %(int(valor / 10)))
valor = valor % 10
print("%d nota(s) de R$ 5.00" %(int(valor / 5)))
valor = valor % 5
print("%d nota(s) de R$ 2.00" %(int(valor / 2)))
valor = valor % 2
print("MOEDAS:\n%d moeda(s) de R$ 1.00" %(int(valor)))
valor = valor % 1
print("%d moeda(s) de R$ 0.50" %(int(valor / 0.5)))
valor = valor % 0.5
print("%d moeda(s) de R$ 0.25" %(int(valor / 0.25)))
valor = valor % 0.25
print("%d moeda(s) de R$ 0.10" %(int(valor / 0.10)))
valor = valor % 0.10
print("%d moeda(s) de R$ 0.05" %(int(valor / 0.05)))
valor = valor % 0.05
print("%d moeda(s) de R$ 0.01" %(int(valor / 0.01)))
valor = int(input())
print("%d\n%d nota(s) de R$ 100,00" %(valor, int(valor / 100)))
valor = valor % 100
print("%d nota(s) de R$ 50,00" %(int(valor / 50)))
valor = valor % 50
print("%d nota(s) de R$ 20,00" %(int(valor / 20)))
valor = valor % 20
print("%d nota(s) de R$ 10,00" %(int(valor / 10)))
valor = valor % 10
print("%d nota(s) de R$ 5,00" %(int(valor / 5)))
valor = valor % 5
print("%d nota(s) de R$ 2,00" %(int(valor / 2)))
valor = valor % 2
print("%d nota(s) de R$ 1,00" %(valor))
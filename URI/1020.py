idade = int(input())
ano = idade / 365
idade = idade % 365
mes = idade / 30
print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(ano , mes, idade % 30))
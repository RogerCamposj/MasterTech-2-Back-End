import statistics as es
# from statistics import mean   // serve para importar só uma lib da biblioteca

historia_n1 = float(input('nota1:  '))
historia_n2 = float(input('nota2:  '))

lista_notas = [historia_n1, historia_n2]
media = es.mean(lista_notas)
print(media)

if media >= 7:
    print('aprovado')

elif media >= 5 and media < 7:
    print('recuperação')

else:
    print('reprovado')






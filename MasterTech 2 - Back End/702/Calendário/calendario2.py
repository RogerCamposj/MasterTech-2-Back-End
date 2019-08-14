def dias(dia):
    retur n {
        1: 'Domingo',
        2: 'Doming',
        3: 'Domio',
        4: 'Dongo',
        5: 'Dmingo',
        6: 'Domngo',
        7: 'Dogo',
    }[dia]


x = int(input('diite  de 1 a 7: '))

try:
    print(dias(x))
except:
    print('inserir número válido')

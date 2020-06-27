#Estrutura FOR

tuplas = (1,2,3,4,5)

for t in tuplas:
    print(t)

lista = [(1,2), (2,3),(3,4)]
type (lista)

(t1, t2) = lista[0]
print(t1)


for (t1, t2) in lista:
    print (t1 * t2)
    
d = {'k1': 1, 'k2':2, 'k3':3}

for (key, valor) in d.items():
    print(key, ':', valor)

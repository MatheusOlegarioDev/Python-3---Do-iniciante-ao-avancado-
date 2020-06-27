#Compreensão em Listas

#Formas Erradas de Listas não apropriadas para o dia a dia;

# X = [1,2,3,4,5]

# x = []

# for in range(0,30):
#    x += [i]

    #x.append(i)


lista = [i for i in range(0,30)]

valores = [i * 2 + 10 for i in range(0,15)]

print(lista)
print(valores)

# Criação de listas de pares

x = []

for i in range(0,20):
    if i % 2 == 0:
        x += [i]

x = [i for i in range (0,20) if i % 2 == 0]

listas = []
listas = [letter for letter in 'word']

#Conversão de Temperaturas

celsius = [0,10,15,20,30,100]

fahrenheit = [ (temp * (9/5)  + 32) for temp in celsius]

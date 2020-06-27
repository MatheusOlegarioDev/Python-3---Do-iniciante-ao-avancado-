#Teste de avaliação de declarações

# Use for, split() e if para criar uma declaração que imprima as palavras que
# comecem com 's';

st = 'Frase boa é frase curta'
split_string = st.split()

for letra in split_string:
    if letra[0] == 's':
       print (letra)

#Use Range() para imprimir todos os números pares de 0 a 10.

x = range(0, 10)

for num in x:
    if num % 2 == 0:
        print(num)

#Use a compreensão de lista para criar uma lista de todas os números entre
# 1 e 50 que são divisiveis por 3.

lista = [x for x in range (1, 50) if x % 3 == 0]
print(lista)

# Percorra a string abaixo e se o comprimento de uma palavra for par imprima " é par"

string = 'Print every word in this sentence that has an even number of letters'

splt_string = st.split()

for i in split_string:
    size = len(i)
    if size % 2 == 0:
        print(i, ':possui comprimento par!')


#Escreva um programa que imprima os números inteiros de 1 a 100 para
# múltiplos de três imprima "Fizz" ao ivés do número, e para os
# múltiplos de cinco imprima "buzz" para números que são múltiplos
# de três e cinco impressões "FizzBuzz".

for i in range(1, 100):
    if i % 3 == 0 and i & 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Buzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# Use compreensão em listas para criar uma lista das primeiras letras
# de cada palavra na string abaixo:

st = 'Olá Matheus Olegario Vieira Couto'

split_st = st.split()

compiladas = [latter for latter in split_st]
print(compiladas)
        

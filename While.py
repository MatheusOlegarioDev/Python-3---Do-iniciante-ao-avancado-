x = 1
while x < 10:
    print('O valor de X e:', x)
    x += 1
else:
    print('O valor de x e:', x)


b = 1
c = 1

while b < 10 and c < 20:
    print('O valor de b * c é:', b * c)
    b += 1
    c += 2
else:
    print('O valor de b * c', b * c )


#Break

x = 1
lista = []

while True:
    lista += [x]
    x += 1
    if x > 10:
        break
print(lista)


#Continue


number = 50
x = 1

while x < number:
    x +=1
    if x % 2 == 1:
        continue
    if x % 2 == 0:
        print(x,'par')
        










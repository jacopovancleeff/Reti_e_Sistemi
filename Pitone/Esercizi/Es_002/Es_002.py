n_volte = input("\n Inserire il numero di parole da inserire : ")
lista = []


for i in range (int( n_volte)):
    x=input("\n Inserire una parola : ")
    lista.append(x)

y=input("\n Inserire la lunghezza minima : ")

for i in range (len(lista)):
    if(len(lista[i])>=int(y)):
        print(lista[i])
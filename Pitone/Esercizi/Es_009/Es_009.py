"""
Es   : 009 
Nome : Jacopo Van Cleeff

"""
def main():

    # creo la mia lista che poi userò per creare la matrice

    matrice =[]

    # chiedo in input le dimensioni e creo la matrice piena di False

    dim = int(input("Inserire il numero di colonne : "))

    for i in range(dim):
        matrice.append([False for i in range(dim)])

    # chiedo in input le coordinate e sostituisco gli 0 con degli 1 nelle apposite cell

    continuare = 0

    # ciclo finchè l'utente inserisce numeri diversi da -1

    while continuare != -1:

        # prendo le coordinate da tastiera e le separo

        coord = input("Inserire la x e la y separate da una virgola per posizionare un ostacolo (x,y) : ")
        coord_int = coord.split(",")

        # metto nelle coordinate date dall'utente l'ostacolo segnalandolo con un True

        matrice[dim -(int(coord_int[1]))][(int(coord_int[0]))-1] = True
       
        continuare= int(input("Inserire un numero qualsiasi se si vuole continuare? (-1 per terminare) : "))

    # stampo la matrice 

    for j in matrice:
        print(j)

if __name__ == "__main__":
    main()
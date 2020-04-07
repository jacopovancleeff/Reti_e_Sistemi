   
def addMatGraf(): 
   
    matrice =[]

    n = int(input("Inserire il numero di colonne  "))

    for i in range(n):
        matrice.append([0 for i in range(n)])
        

    for k in range (n):

        take_str = input(f"Inserire i nodi con cui è collegato il nodo {k} ")
        take = [int(i) for i in take_str.split(",") if i != '']

        for i in take:
            matrice[k][i]=1

    return matrice

def addDizGraf(m):
    d = {}
    l = []
    
    for k,_ in enumerate(m):
        l = [i for i,_ in enumerate(m)if m[k][i]!=0]
        d[k]=l
    
    return d

def retDizMat(d):
    m = []
    for i,_ in enumerate(d):
        m.append([0 for k in range(len(d))])
        

def main():
    mat = addMatGraf()
    diz = addDizGraf(mat)

if __name__ == "__main__":
    main()
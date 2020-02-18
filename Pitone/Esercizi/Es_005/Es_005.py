import random

def push(stack,element):           
    stack.append(element)   
    return stack

def pop(stack):
    element = stack.pop()
    return stack,element

def coppare(stack):

    #pila1=[]
    #pila2=[]
    #item=[]
    
    y = random.randint(1,len(stack)-1)
    stack = stack[y:len(stack)] + stack[0:y]
    
    """
    for i in range (0,y):
        item = pop(stack)
        push(pila1,item)  

    for i in range (y,len(stack)):
        item = pop(stack)
        push(pila2,item)

    for i in range (0,y):
        item = pop(pila1)
        push(stack,item)  

    for i in range (y,len(stack)):
        item = pop(pila2)
        push(stack,item) 
    """       
    
    return stack





class carta(object):

    #metodo costruttore della classe

    def __init__(self,seme,numero):
        self.seme = seme
        self.numero = numero

    def stampa (self):
        print(f"Il seme della carta è {self.seme} e la carta è {self.numero}")


# c = carta("Cuori",13)
# c.stampa()

Semi = ["C","P","F","D"]
Mazzo = []

for i in range(1,14):
    for s in Semi:
        push(Mazzo,carta(s,i))

Mazzo = coppare(Mazzo)

for i in Mazzo:
    i.stampa()

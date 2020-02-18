def addressCheck(string):
    field=string.split(".")
    ip=[]
    for index,_ in enumerate(field):
        try:
            ip.append(int(field[index]))
        except:
            print("\n ----------------------------------------------")
            print("\n WARNING")
            print("\n the number entered is not valid")
            print("\n ----------------------------------------------")
    for index,_ in enumerate(ip):
        if ip[index] < 0:
            ip[index] = 0
        if ip[index] > 255:
            ip[index] = 255
    while len(ip) > 4:
        ip.pop(len(ip)-1)
    while len(ip) < 4:
        ip.append(0)
    return ip

def maskCheck(string):
    
    mask = []
    field = string.split(".")

    for index,_ in enumerate(field):
        mask.append(int(field[index]))
   
    return mask

def decimale(change):

    somma = (change[0]*(256**3)) + (change[1]*(256**2)) + (change[2]*(256**1)) + change[3]

    return somma

def setHost(m):

    host = (2**32)-m

    return host

def to_str(ip):
    return '.'.join(str(ip >> n & 0xFF) for n in [24, 16, 8, 0])

def countIP(ip,n):

    disp = []

    for i in range(1,n-1):
        disp.append(to_str(ip+i))
        

    return disp

def main():

    # chiedo in input e cotrollo l'ip che mi da l'utente 

    string=input ("enter ip address (decimal mode) \n")
    ip=addressCheck(string)                                               # lista ip

    # chiedo in input e controllo la subnet mask che mi da l'utente

    string=input ("enter ip mask (only number) \n")
    mask=maskCheck(string)                                                  # lista mask

    # converto in decimale l'indirizzo ip

    ip_de = decimale(ip)                                                 # numero intero
    print(ip_de)

    # converto in decimale la subnet mask

    mask_de = decimale(mask)                                              # numero intero

    # conto il numero di host disponibili

    n_host = setHost(mask_de)
    print(n_host)

    # resetto l'indirizzo ip con la subnet mask

    ip_de = ip_de & mask_de
    print(ip_de)

    # creo la lista con tuttti gli indirizzi ip disponibili

    ip_disp = countIP(ip_de,n_host)
    print(ip_disp)
    
if __name__ == "__main__":
    main()
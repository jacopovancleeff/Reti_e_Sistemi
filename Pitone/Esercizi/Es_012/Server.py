import socket as sck

HOST = '79.31.222.112'
PORTA = 6000
BYTE  = 4096

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.bind((HOST,PORTA))

print("Server avviato in attesa del messaggio ...")

data, addr = s.recvfrom(BYTE)

data  = (eval(data.encode)).decode

s.sendto(data,(addr))

s.close()
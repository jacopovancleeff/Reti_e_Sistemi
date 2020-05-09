import socket as sck

def server():

    HOST = 'localhost'
    PORTA = 5000
    BYTE  = 4096

    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind((HOST, PORTA))
    s.listen(1)
    conn, addr = s.accept()

    while True:
        data = conn.recv(1024)
        if not data: break
    conn.send(data)

if __name__ == '__main__':
    server()
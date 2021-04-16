import socket
from threading import Thread
L=[]

def ConversaSimultanea(a,b):
    mensagem = ""
    print(f"Cliente {a} ou {b} ntrou no chat")
    while mensagem != "Fim":
        mensagem = L[a].recv(5000)
        if not mensagem:
            break
        L[b].sendall(mensagem)
    conn.close()

host = '127.0.0.1'
port = int('40000')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4,tipo de socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))  # liga o socket com IP e porta
s.listen(1)  # espera chegar pacotes na porta especificada
print("Listening")

for i in range(2):
    print(f"Esperando cliente numero {i} conectar-se")
    conn, addr = s.accept()  # as variaveis conn a addr sao preenchidas pela funcao accept
    L.append(conn)
    print(f"Cliente {i} conectado e acrescentado(append)")
    
t1 = Thread(target=ConversaSimultanea, args=(1,0)).start()
t2 = Thread(target=ConversaSimultanea, args=(0,1)).start()


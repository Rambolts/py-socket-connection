import socket

def client(h, p):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 tipo de socket
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
	while True:
		try:
			s.connect((h, p))
			break
		except Exception as e:
			pass
	print("Conectou")
	msg = ''

	while msg != "Fim":
		msg = input("Entre com a mensagem: ")
		s.sendall(msg.encode('utf-8'))          # Envia dados
		var = s.recv(1024)                      # Recebe dados
		print(var)

	s.close()  # Termina conexao
	print("Fechou a conexao")

if __name__ == '__main__':
	host = '127.0.0.1'                         #input("Entre com o IP do servidor remoto:")
	port = 40000                               #input("Entre com a porta do servidor remoto:")
	client(host, port)

import random 
import socketserver 
import socket, os 
import string

# -------------------------------------------

# Bibliotecas Importadas

# -------------------------------------------

# - random: usada para gerar valores aleatórios.

# - socketserver e socket: utilizadas para facilitar a criação de servidores TCP.

# - os: oferece acesso a recursos do sistema operacional.

# - string: contém coleções úteis de caracteres como letras e dígitos.

# -------------------------------------------

# Leitura da Flag Real

# -------------------------------------------

# Lê o conteúdo do arquivo flag.txt, remove espaços em branco e armazena na variável 'flag'.

flag = open('flag.txt','r').read().strip()

# -------------------------------------------

# Função 1: Enviar Mensagem

# -------------------------------------------

def send_message(server, message): # Codifica a mensagem (string) para bytes utilizando UTF-8 enc = message.encode() # Envia a mensagem codificada através da conexão com o cliente server.send(enc)

# -------------------------------------------

# Função 2: Gerar XOR da Flag Falsa

# -------------------------------------------

def setup(server, key): # Define uma flag falsa que será usada no desafio flag = 'THM{thisisafakeflag}' xored = ""

```
# Faz o XOR entre cada caractere da flag falsa e a chave fornecida
for i in range(0, len(flag)):
    xored += chr(ord(flag[i]) ^ ord(key[i % len(key)]))

# Converte o resultado para hexadecimal para facilitar a visualização/transmissão
hex_encoded = xored.encode().hex()
return hex_encoded
```

# -------------------------------------------

# Função 3: Início da Conexão e Execução do Desafio

# -------------------------------------------

def start(server): # Gera uma chave aleatória de 5 caracteres (letras e números) res = ''.join(random.choices(string.ascii\_letters + string.digits, k=5)) key = str(res)

```
# Executa a função de XOR com a flag falsa e a chave gerada
hex_encoded = setup(server, key)

# Envia a mensagem com o texto codificado (flag falsa XOR)
send_message(server, "This XOR encoded text has flag 1: " + hex_encoded + "\n")

# Solicita ao usuário que tente adivinhar a chave usada no XOR
send_message(server,"What is the encryption key? ")

# Recebe a resposta do usuário (cliente TCP)
key_answer = server.recv(4096).decode().strip()

# Compara a resposta com a chave verdadeira
try:
    if key_answer == key:
        # Se correta, envia a flag real (lida do arquivo flag.txt)
        send_message(server, "Congrats! That is the correct key! Here is flag 2: " + flag + "\n")
        server.close()
    else:
        # Caso a chave esteja incorreta
        send_message(server, 'Close but no cigar' + "\n")
        server.close()
except:
    # Em caso de erro (como conexão encerrada), mostra mensagem genérica
    send_message(server, "Something went wrong. Please try again. :)\n")
    server.close()
```

# -------------------------------------------

# Classe que Trata Requisições TCP

# -------------------------------------------

class RequestHandler(socketserver.BaseRequestHandler): def handle(self): # Executa a função de início para cada nova conexão start(self.request)

# -------------------------------------------

# Execução do Servidor

# -------------------------------------------

if **name** == '**main**': socketserver.ThreadingTCPServer.allow_reuse_address = True server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), RequestHandler) server.serve_forever()

import socket
from googletrans import Translator

translator = Translator()
server_lang = 'en'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1337))
server.listen()

client, addr = server.accept()

while True:
    try:
        message = client.recv(1024).decode()
        
        if not message:
            print("Client closed the connection.")
            client.close()
            break
        
        if ']' in message:
            lang = message[1:message.index(']')]
            translation = translator.translate(
                message[message.index(']')+1:],
                src=lang, dest=server_lang
            )
            
            print(translation.text)
        else:
            print("Invalid message format: Missing closing bracket ']'")
    except KeyboardInterrupt:
        print("Server interrupted.")
        client.close()
        break

from socket import *


#local ağa bağlantı sağlıyor
server=socket(AF_INET,SOCK_STREAM)
server.bind(("127.0.1.1", 8083))
#client tarafını dinliyor
server.listen() 

print('Listening Port')
#clientin bağantısını sağlıyor
connection , address = server.accept()

print('user connected')
#chat sağlanabilmesi için döngüye alınıyor
while(1):
    
    data = input('server:')
    connection.send(bytes(data,'utf-8'))
    receivedData=connection.recv(2048).decode('utf-8')
    print('client:',receivedData)
    #eğer data eşitse fotoyu gönder
    if receivedData == 'photo send':
        file = open('server_image.jpg',"wb")
        received_image =connection.recv(2048)
        while received_image:
            file.write(received_image)
            received_image = connection.recv(2048)
            
            
file.close()
connection.close()


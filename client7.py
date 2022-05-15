from socket import *
#server bağlantısı yapılan yer
client=socket()
client.connect(('127.0.1.1', 8083))

print('server connected')
#döngüye alınıyor görüşmenin devam etmesi için
while(1):
    receivedData = client.recv(2048).decode('utf-8')
    print('server:', receivedData)
    data = input('client:')
    client.send(bytes(data,'utf-8'))
    if data == 'photo send':
        file = open('client_image.jpg', 'rb')
        client_image =file.read(2048)
        while client_image:
            client.send(client_image)
            client_image=file.read(2048)
            
file.close()
client.close()
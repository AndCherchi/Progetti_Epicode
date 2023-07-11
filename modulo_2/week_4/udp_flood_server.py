import socket
import random
import string

buffersize = 1024

INDIRIZZO = "127.0.0.1"
PORTA = 80


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: # creo il socket
        s.bind((INDIRIZZO, PORTA))
        print("Il Server è in ascolto \n")
        while True:
                bytesAddressPair = s.recvfrom(buffersize) #dichiaro la dimensione del pacchetto che riceverò, il metodo recvfrom() restituirà una tupla
                messaggio = bytesAddressPair[0] # nella prima posizione il messaggio ricevuto dal client
                indirizzo = bytesAddressPair[1] # nella seconda posizione l'indirizzo e il numero di porta del mittente del pacchetto
                
                clientMsg = " Il client ha inviato : {}".format(messaggio) 
                clientIP = "Il client ha il seguente IP address {}".format(indirizzo)
                
                print(clientMsg)
                print(clientIP)

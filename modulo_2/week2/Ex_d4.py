#Traccia : 
# Si scriva un programma in python che in base alla scelta dell'utente permetta di calcolare
# il perimetro di diverse figure geometriche (scegliete pure quelle che volete voi).
# Per la risoluzione dell'esercizio abbiamo scelto : 
# - Quadrato (perimetro = lato *4)
# - Cerchio (circonferenza = 2*pi greco * r)
# - Rettangolo (perimetro = base*2 + altezza*2)

scelta = 0 
#perimetro = 0

# faccio scegliere all'utente quale perimetro vuole calcolare
# una volta scelto, faccio il casting della stringa ricevuta in input e trasformo la stringa in un intero 

scelta= int(input("Di quale figura geometrica vuoi calcolare il perimetro ? \n 1 Quadrato \t 2 Cerchio \t 3 Rettangolo \n"))
# una volta trasformata in numero intero, uso l'istruzione if per eseguire solo la parte di codice interessata
# ovvero quella che corrisponde alla scelta dell'utente.
if(scelta == 1):
    lato = int (input("Inserisci il lato del quadrato : \n"))
    perimetro= lato*4
    print("Il perimetro del lato è : ", perimetro)

if(scelta == 2 ):
    raggio= int(input("Inserisci il raggio della circonferenza :\n"))
    circonferenza = 2 *3.14 * raggio
    print("La circonferenza del cerchio è : ", circonferenza)
if(scelta==3):
    base= int(input("Inserisci la base del rettangolo : "))
    altezza= int(input("\n Inserisci l'altezza del rettangolo : "))
    perimetro= (base*2) + (altezza*2)
    print("\n Il perimetro del rettangolo è : ",perimetro)


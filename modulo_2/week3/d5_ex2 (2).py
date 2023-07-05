# Scrivi una funzione che data in ingresso una lista A contentente n parole, 
# restituisca in output una lista B di interi che rappresentano 
# la lunghezza delle parole contenute in A.

#inizio creando le funzioni che userò nel programma
def contalettere(listina):  # creo la funzione contalettere una funzione opzionale creata solo a scopo illustrativo per verificare l'effettiva lunghezza delle parole inserite
    for parola in listina: # a questo punto con un ciclo for scorro all'interno della lista di parole
        print("la parola : ", parola)   #e stampo ogni parola inserita nella lista
        numeroLettere = len(parola) # utilizzo il metodo delle stringhe len che mi restituisce
        print(" ha ",numeroLettere, "lettere") # il valore intero della lunghezza della stringa

def trasformalista (lista_A,lista_B): #questa è la funzione richiesta dal programma
    for parola in lista_A: #ciclo for per scorrere gli elementi della lista
        numeroLettere = len(parola) #utilizzo len per vedere quanto è lunga la parola inserita
        lista_B.append(numeroLettere) #uso il metodo append per inserire in coda alla lista il numero 
        
# creo le liste vuote
nuovalista = []
listaParole = []
#stampo a schermo un messaggio iniziale e poi chiedo all'utente di inserire quanto vuole che sia lunga la lista
print("Ciao, creiamo una lista di parole...  \n")
lung= int(input("Quanto vuoi che sia lunga?\n"))

#ciclo for in range della lunghezza inserita dall'utente
for parole in range(lung):
    #faccio inserire la parola all'utente e poi uso il metodo append  per inserirla nella lista
    parola= input("Inserisci parola da includere nella lista : \n")
    listaParole.append(parola)

# Dopo aver popolato la lista invoco le due funzioni create
contalettere(listaParole)
trasformalista(listaParole,nuovalista)

#infine stampo la nuova lista creata con la funzione trasformalista 
print("Il numero delle lettere per ogni parola inserita è : \n" ,nuovalista)
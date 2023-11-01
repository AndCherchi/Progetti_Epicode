Day 3 : 
Esercizio 2 
Traccia : Scrivere un programma in linguaggio assemblativo, che presi due dati a e b in memoria, calcola l'espressione (a+3)*b ponendo il risultato nel registro accumulatore.

move EBX,a -> inserisci nel registro EBX il valore in esadecimale a
add EBX,3  -> aggiungi al registro EBX il valore 3
mul b      -> moltiplica il valore presente nel registro EBX per il valore esadecimale b
mov EAX,EBX -> copia il valore presente nel registro EBX nel registro accumulatore EAX


/ L'esercizio non è ancora stato ultimato, purtroppo per motivi lavorativi non ho potuto completare la consegna!


#include <stdio.h>
#include <string.h>
#include <ctype.h>


#define LUNG 10



int main(){

        // dichiarazione delle variabile che verranno usate durante il programma
        char nome[LUNG];
        char scelta[2];
        int risposta;
        int punteggio=0;
        int i=1;
        int lunghezza = 0;
        int errore = 0;
        int contatore=0;
        // inizio del ciclo per l'esecuzione del programma, è stato usato il do/ while in questo caso, così da permetterci di poter tornare di nuovo al menu iniziale  gioco una volta terminate le domande
        
        do
        {
        printf("\n Voglio fare un gioco con te !\n");
        printf("In questo gioco ti farò alcune semplici domande, se risponderai correttamente ti assegnerò un punto! \n");
        printf("Sei pronto a iniziare? \n A) SI B) NO \n");
        printf(" >>> ");
        scanf("%s",&scelta);
        // primo controllo aggiunntivo, rendere l'input dell'utente sempre maiuscolo
        while(scelta[contatore] !=0){
                if(scelta[contatore] >=97 && scelta[contatore] <=122){
                        scelta[contatore] = scelta[contatore] - 32;
                }
                contatore++;
        }


        if(strcmp(scelta,"A")==0)  // effettuato un controllo sulla stringa 
                {
                        // inserito controllo aggiuntivo nel caso in cui il nome risultasse troppo lungo, il gioco non permette la prosecuzione in quanto continua a chiedere all'utente un nome  valido
                        do{
                        printf("\n Iniziamo");
                        printf("\n Innanzitutto, dimmi come ti chiami : \t ");
                        scanf("%s", nome);
                        printf("Piacere %s, pronto ? \n", nome);
                        lunghezza = strlen(nome);
                        if(lunghezza > LUNG)
                        {
                                printf("Il nome è troppo lungo \n, Riproviamo: \t");
                        }
                        }while(lunghezza > LUNG );
                        
                        //implementato ulteriore controllo, questa volta sulle domande, nel caso in cui l'utente dia una risposta non prevista
                        printf("Quale è la capitale dell'Austria? \n");
                        printf("1) Roma \t 2) Vienna \t 3) Parigi \t 4) Zurigo \n");
                        printf(" >>> ");
                        scanf("%d",&risposta);
                        if(risposta=2){
                                punteggio+=1;
                                // printf("Molto bene \n");
                        }
                         
                        printf("A quanti anni si può votare per il senato della repubblica in Italia ? \n");
                        printf("1) 25 \t 2)30 \t 3)18 \t 4)40 \n");
                        printf(" >>> "); 

                        scanf("%d",&risposta);
                        if(risposta ==1)
                        {
                        //      printf("Molto bene \n");
                                punteggio+=1;
                        }
                        printf("Quanti sono i segni zodiacali ? \n 1)9 \t 2)14 \t 3)12 \t 4)15\n");
                        printf(" >>> "); 
                        scanf("%d",&risposta);
                        if(risposta ==3)
                        {
                        //      printf("Molto bene \n");
                                punteggio+=1;
                        }
                        printf("Quante settimane ci sono in un anno ? \n 1) 57 \t 2)44 \t 3)49 \t 4)56 \n");
                        printf(" >>> "); 
                        scanf("%d",&risposta);
                        if(risposta==4)
                        {
                        //      printf("Molto bene \n");
                                punteggio+=1;
                        }


                        printf("Punteggio totalizzato %d \n ",punteggio);
                }
        else
                {
                        printf("\n Addio allora \n");
                }
        }
        while(i==1);

        return 0;
}



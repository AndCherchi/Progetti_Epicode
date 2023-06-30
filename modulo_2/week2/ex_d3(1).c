#include <stdio.h>
#include <string.h>


#define LUNG 10


int main(){  

        // dichiarazione delle variabile che verranno usate durante il programma
        char nome[LUNG];
        char scelta[2]; 
        int risposta;   
        int punteggio=0;
        int i=1;
        // inizio del ciclo per l'esecuzione del programma, è stato usato il do/ while in questo caso, così da permetterci di poter tornare di nuovo al menu iniziale  gioco una volta terminate le domande  
        
        do
        { 
        printf("\n Voglio fare un gioco con te !\n");
        printf("In questo gioco ti farò alcune semplici domande, se risponderai correttamente ti assegnerò un punto! \n");
        printf("Sei pronto a iniziare? \n A) SI B) NO \n");
        printf(" >>> ");    
        scanf("%s",&scelta); 
        if(strcmp(scelta,"A")==0)  // effettuato un controllo sulla stringa 
                {  
                        printf("Molto bene \n Iniziamo");
                        printf("Innanzitutto, dimmi come ti chiami : \t ");
                        scanf("%s",&nome);

                        printf("Quale è la capitale dell'Austria? \n");
                        printf("1) Roma \t 2) Vienna \t 3) Parigi \t 4) Zurigo \n");
                        printf(" >>> "); 
                        scanf("%d",&risposta);
                        if(risposta == 2)    
                        {  
                                punteggio+=1;
                        //      printf("Molto bene \n"); 
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

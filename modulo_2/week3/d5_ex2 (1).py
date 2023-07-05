import string
import random

print(string.ascii_letters)
print(string.digits)


parola_sicura = []
print("Quanto vuoi che sia lunga la pw?  ")
lunghezza = int(input("8 caratteri o 20 caratteri"))

if(lunghezza==8):
    stringa = string.ascii_letters + string.digits 
    for carattere in range(8):
        parola_sicura.append(random.choice(stringa))
    password = "".join(parola_sicura)
    print(password)
elif(lunghezza== 20):
    stringa = string.ascii_letters + string.digits + string.punctuation
    for carattere in range(20):
        parola_sicura.append(random.choice(stringa))
    password = "".join(parola_sicura)
    print(password)
else:
    print("\n Scelta non prevista \n")
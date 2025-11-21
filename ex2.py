'''Fes un programa que generi un número aleatori entre 1 i 10, i demani a l'usuari que l'endevini. El programa ha de: 

Donar pistes dient si el número és més gran o més petit
Comptar quants intents necessita l'usuari
Acabar quan l'usuari encerti el número'''

# Importem la llibreria de random
import random

# Variables
num = random.randint(1, 10)
intents = 0
intent = int(input("Posa un numero del 1 al 10 per adivinar "))

# Bucle while
while intent != num: # Amb aixo fem que si el numero introduit no es igual que el random el bucle continui
    if intent < num: # Si el numero introduit es mes petit que el random et dona una pista dient que es mes petit i torna a demanar un numero
        print(f"{intent} es mes petit que el numero a adivinar")
        intent = int(input("Posa un numero del 1 al 10 per adivinar "))
        intents = intents + 1
    else: # Si el numero introduit es mes gran que el random et dona una pista dient que es mes gran i torna a demanar un numero
        print(f"{intent} es mes gran que el numero a adivinar")
        intent = int(input("Posa un numero del 1 al 10 per adivinar "))
        intents = intents + 1
if intent == num: # Si el numero introduit es igual que el random surt del bucle i et diu que ho has adivinat i els intents que has necessitat
    print(f"Ho has adivinat!!!\nHas necessitat {intents} intents")
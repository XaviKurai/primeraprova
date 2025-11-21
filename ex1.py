'''Enunciat 1 - Compte enrere
Fes un programa que demani un número, valida que sigui més gran que 0, i faci un compte enrere fins a 0, mostrant tots els números. Quan arribi a 0 ha de mostrar "BOOM!".
Pots utilitzar   time.sleep(0.5) de la llibreria time
import time # HA DE SER LA PRIMERA LÍNIA'''

# Importem la llibreria time
import time

# Variable del numero
num = int(input("Posa un numero per fer la compta enrere "))

# Un if per comprovar si el numero es 0 o negatiu
if num <= 0:
    print("El numero no pot ser 0 ni negatiu!")
    exit()
# Si el numero es positiu entra al while
else:
    while num != 0: # El while fa que si la variable num no es 0 s'executi un print amb el numero, despres resta 1 al numero i torna a començar fins arribar a 0 que fa el print "BOOOM"
        time.sleep(0.5)
        print(f"{num}")
        num -= 1
        if num == 0:
            print("BOOOOOOOOM!")
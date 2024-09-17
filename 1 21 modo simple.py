import random
dealer = int(0)
jugador = []
cartas = ["2","3","4","5","6","7","8","9","10","J","Q","K","As"]
sumcar = int(0)
x = int(2)
respuesta = str
cuentaCartas = 0

print("Hola, éste es un juego de Blackjack o 21. Comencemos.")

for num in range(0,x): # Por cada número que haya en un rango desde 0 hasta lo que vale x, o sea, 2,
    jugador.append(random.choice(cartas)) # utiliza .append para agregar lo que escogió random a las
                                          # cartas del jugador.
print("Jugador, tus cartas son", jugador)

while respuesta == "sí" or "si": # 
    respuesta = input("¿Solicitas otra carta?:").lower()
    if respuesta == "no":
        break
    jugador.append(random.choice(cartas))
    print("Tus cartas son", jugador)

dealer = random.randrange(17,26)

for carta in jugador:
    if jugador[cuentaCartas] == "2":
        sumcar+=2
    if jugador[cuentaCartas] == "3":
        sumcar+=3
    if jugador[cuentaCartas] == "4":
        sumcar+=4
    if jugador[cuentaCartas] == "5":
        sumcar+=5
    if jugador[cuentaCartas] == "6":
        sumcar+=6
    if jugador[cuentaCartas] == "7":
        sumcar+=7
    if jugador[cuentaCartas] == "8":
        sumcar+=8
    if jugador[cuentaCartas] == "9":
        sumcar+=9
    if jugador[cuentaCartas] == "10":
        sumcar+=10
    if jugador[cuentaCartas] == "J" or "Q" or "K":
        sumcar+=10    
    if jugador[cuentaCartas] == "As":
        if sumcar+11>=21:
            sumcar+=1
        else:
            sumcar+=11
    cuentaCartas+=1

print("El jugador ha acumulado un total de {} puntos, mientras que el Dealer tiene {}".format(sumcar, dealer))

if sumcar == 21 and sumcar == dealer:
    print("Esto es un empate. El jugador y el Dealer han acumulado 21 puntos. Blackjack.")
elif sumcar == dealer and sumcar != 21:
    print("Esto es un empate. El jugador y el Dealer han acumulado la misma cantidad de puntos.")
elif sumcar == 21 and dealer < sumcar:
    print("El jugador ha ganado esta partida al acumular 21 puntos. Blackjack.")
elif dealer > 21:
    print("El jugador ha ganado esta partida: El Dealer ha acumulado más de 21 puntos.")
elif sumcar > dealer and dealer < 21:
    print("El jugador ha ganado esta partida al acercarse más a 21 sin pasarse.")
else:
    print("El Dealer ha ganado esta partida.")

jugador.clear()
sumcar = 0
cuentaCartas = 0
dealer = 0
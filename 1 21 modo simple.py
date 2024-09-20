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

while respuesta == "sí" or "si": # Aquí recoje la respuesta la respuesta del jugador para continuar el juego.
    respuesta = input("¿Solicitas otra carta?: Sí o No").lower() # Dependiendo de que sea "sí", "si" o "no",
    if respuesta == "no":                                        # esto para evitar que se bugee el ciclo,  
        break                                                    # continua dándole cartas al jugador o rompe
    jugador.append(random.choice(cartas))                        # el ciclo para comenzar las condicionales
    print("Tus cartas son", jugador)                             # de la partida.

dealer = random.randrange(17,26) # Para este punto, el ciclo ha de haber terminado y es momento de darle al dealer
                                 # su respectiva cantidad de puntos. Como realmente no jugó con cartas o su equiva-
for carta in jugador:            # lente, generamos una cantidad entre 17 y 26 para compararla con las cartas del
    if jugador[cuentaCartas] == "2": # jugador.
        sumcar+=2
    if jugador[cuentaCartas] == "3": # En este ciclo FOR, se analizan todas las cartas que el jugador aceptó,
        sumcar+=3                    # al ser la lista un tipo str, tengo que analizar cada una y después
    if jugador[cuentaCartas] == "4": # sumarle su valor natural o su correspondiente al ser J, Q o K.
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
    if jugador[cuentaCartas] == "J":
        sumcar+=10
    if jugador[cuentaCartas] == "Q":
        sumcar+=10
    if jugador[cuentaCartas] == "K":
        sumcar+=10   
    if jugador[cuentaCartas] == "As": # En esta parte está el fix. Si al sumar al total de cartas 11 y el resultado
        if sumcar+11>=21:             # da más o igual que 21, no me conviene que A valga 11, entonces vale 1.
            sumcar+=1                 # Si, por el contrario, vale menos que eso, entonces A puede valer 11.
        else:
            sumcar+=11
    cuentaCartas+=1 # Después de haber analizado toda la lista, suma a cuentaCartas 1, porque es el que itera
                    # por toda la lista.
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

jugador.clear() # Se reinicia el juego al final.
sumcar = 0
cuentaCartas = 0
dealer = 0
## BLACKJACK EN PYTHON.
Hola, este proyecto es un juego simple de BlackJack o 21 desarrollado en terminal. Siéntase libre de utilizar este código como mejor le sirva, no es necesario que dé créditos ya que utiliza lógica muy básica.

# Características.
- Partida simple y clásica.
- Únicamente el jugador puede optar por recibir o rechazar cartas.
- La partida se lleva a través de la terminal.

# Cómo jugar.
1. El jugador comienza con un conjunto de cartas vacío.
2. Preguntar al jugador si desea quedarse con las cartas que tiene, o si solicita una carta.
3. Si el jugador solicita una carta, generar aleatoriamente una carta de una baraja y agregarla a las cartas que tiene el jugador.
4. Calcular el valor de las cartas que tiene el jugador (numérico) y mostrarlo cada vez que el jugador obtenga una carta. Considerar el valor del As como 11.
5. Volver a preguntar al jugador lo mismo que en el paso (2), hasta que el jugador decida detenerse.
6. Cuando el jugador se detenga, generar aleatoriamente un número entre el 17 y el 26 (incluyendo ambos números). Este será el valor de "la casa" o el "Dealer" contra el cual debe competir el número obtenido por las cartas del jugador.
7. Mostrar los números obtenidos por el jugador y por la casa.

# Variables utilizadas.
dealer: Guarda el valor de las cartas que Dealer tiene, es un número entero.
jugador: Guarda las cartas generadas por un random, es una lista de tipo entero.
cartas: Contiene las cartas que se usan normalmente en el juego, es una lista de tipo str.
sumcar: SUMar CARtas, suma el valor numéricos de las cartas que el Jugador ha acumulado conscientemente.
x: Únicamente se utiliza al inicio del código para asignar las cartas iniciales del Jugador.
respuesta: Se utiliza en el ciclo principal del juego para generar cartas, guarda la respuesta del Jugador para continuar el ciclo o no.
cuentaCartas: Se utiliza como base del ciclo FOR que analiza cada carta que ha recibido el Jugador. Es un entero.

# FIXs implementados.
Como parte de los fixes implementados, el As se toma de dos maneras automáticamente, si al sumar 11 a sumcar, el resultado da más que 21, el valor de As es 1, de otra manera, el valor de As es 11.

## TAHANY ISABELLA PIÑA, PROGRAMACIÓN II, ING. JESICA VIANNEY HERNÁNDEZ GUERRA, SEPTIEMBRE 19/2024.
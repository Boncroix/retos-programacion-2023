import random
'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */'''
points = {
    0: 'love',
    1: '15',
    2: '30',
    3: '40'
}
players = ['P1', 'P2']
count_p1 = 0
count_p2 = 0
advantage = False

while not advantage:
    point = random.choice(players)
    if point == 'P1':
        count_p1 += 1
    elif point == 'P2':
        count_p2 += 1

    if abs(count_p1 - count_p2) == 2 and count_p1 > 3:
        print('Ha ganado el Jugador 1')
        break
    elif abs(count_p2 - count_p1) == 2 and count_p2 > 3:
        print('Ha ganado el Jugador 2')
        break
    elif count_p1 == count_p2 == 3:
        print('Deuce')
        advantage = True
    else:
        print(f'{points[count_p1]} - {points[count_p2]}')

while advantage:
    point = random.choice(players)
    if point == 'P1':
        count_p1 += 1
    elif point == 'P2':
        count_p2 += 1

    if abs(count_p1 - count_p2) == 1 or abs(count_p2 - count_p1) == 1:
        print('Ventaja')
    elif count_p1 == count_p2:
        print('Deuce')
    elif abs(count_p1 - count_p2) == 2 and count_p1 > 3:
        print('Ha ganado el Jugador 1')
        break
    elif abs(count_p2 - count_p1) == 2 and count_p2 > 3:
        print('Ha ganado el Jugador 2')
        break

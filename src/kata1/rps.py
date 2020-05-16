from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
draw = "Empate!" #'Empate!'
win = "Ganaste!" #'Ganaste!'
lose = "Perdiste!" #'Perdiste!'

def quienGana(player, ai):
    print(player, ai)

    player = player.title()
    ai = ai.title()

    print(player, ai)

    if player == options[0]:        # Piedra
        if ai == options[0]:          # Piedra
            return draw
        elif ai == options[1]:        # Papel
            return lose
        else:                         # Tijeras
            return win
    elif player == options[1]:      # Papel
        if ai == options[0]:          # Piedra
            return win
        elif ai == options[1]:        # Papel
            return draw
        else:                         # Tijeras
            return lose
    elif player == options[2]:      # Tijeras
        if ai == options[0]:          # Piedra
            return lose
        elif ai == options[1]:        # Papel
            return win
        else:                         # Tijeras
            return draw
    # else:
    #     result = "Introduce una opción válida: " + ', '.join(options)

    # return result

# Entry Point
def Game():
    #
    #
    player = input("Intoduce una opción (" + ', '.join(options) + " : ")
    #
    #
    ai = options[randint(0, len(options)-1)]
    print("La IA ha sacado " + ai)

    print(player, ai)
    winner = quienGana(player, ai)

    print(winner)

Game()


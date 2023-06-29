from enum import Enum


class GameChoice(Enum):
    INVALID = -1
    PAPER = 1
    ROCK = 2
    SCISSORS = 3
    QUIT = 4
    
    
    

def game_loop():
    """
    Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cunado no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break

def read_user_choice():
    """
    Imprime un menu de instrucciones y lee la respuesta del usuario
    mediante una llamada a `input`.
    Devuelve lo que haya elegido el usario
    """
    user_choice = GameChoice.INVALID
    while user_choice == GameChoice.INVALID:
        print("\tSelect a number:\n\t\t1. Paper \n\t\t2. Rock\n\t\t3. Scissors\n\t\t4. Exit")

        try:
            user_choice = GameChoice(int(input("Enter your choice: ")))
            
        except ValueError:
            user_choice = GameChoice.INVALID
            print("\n\tInvalid choice\n\n")
    print("\n\n\tYour choice: "+ str(user_choice.name))


    return user_choice
   


def is_exit(user_choice):
    """
    Predicado que recib ela respuesta del usuario y devuelve `True` si
    ha pedido salir del juego
    """
    return user_choice == GameChoice.QUIT


def generate_computer_choice():
    """
    Genera una jugada del ordenador de forma aleatoria. El ordenador no puede elegir
    para el juego, solo Piedra, Papel o Tijera
    """
    from random import choice
    comp_choice = choice([GameChoice.PAPER,GameChoice.ROCK,GameChoice.SCISSORS])
    print("\n\n\tComputer choice: "+ str(comp_choice.name))
    return comp_choice



def evaluate_move(user_choice, computer_choice):
    """
    Recibe dos jugadas, determina cual ha ganado y devuelve un mensaje con el resultado.
    Por ejemplo: recibe Papel y Piedra, y devuelve "Papel envuelve Piedra"
    1.Papel, 2. Piedra, 3.Tijera
    """
    if user_choice == computer_choice:
        return "It´s a tie!"
    else:
        if user_choice == GameChoice.PAPER: 
            if computer_choice == GameChoice.ROCK:
                return "You win! Paper covers rock"
            else:
                return "I win! Scissors cut paper"
        elif user_choice == GameChoice.ROCK: #Piedra
            if computer_choice == GameChoice.PAPER:
                return "I win! Paper covers rock"
            else:
                return "You win! Rock smashes scissors"
        else: # Usuario elige Tijera
            if computer_choice == GameChoice.PAPER:
                return "You win! Scissors cut paper"
            else:
                return "I win! Scissors cut paper"
    

def print_result(result):
    """
    Imprime en plan bonito el resultado.
    No devuelve nada
    """
    print("\n\n-------------------------------")
    print("\tGame over!")
    print("\n\n\tResult:")
    print("\n\t\t" + result + "\n\n\n")

def log_error(error):
    """
    Guarga los datos de error en crashlytics
    """
    print(error)

if __name__ == "__main__":
    try:
        game_loop()
    except Exception as e:
        log_error(e)
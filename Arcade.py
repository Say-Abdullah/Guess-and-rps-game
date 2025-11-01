import sys
from rps import rps
from guess_number import guess_number

def play_game(name ='playerOne'):
    welcome_back = False
    while True:
        if welcome_back == True:
         print(f"\n{name}, Welcome back to the Arcade menu.")
        player_choice = input(f"\nPlease choose a game:\n1 = Rock paper scissors \n 2 = guess My number\n\n or press\"x\" to exit the arcade \n\n")
        if player_choice not in ["1","2","x"]:
            print(f"{name},please  enter 1, 2 or x")
            return play_game()
        welcome_back == True

        if player_choice == "1":
            rock_paper_scissors =rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()    
        else:
            print("\n See you next time!\n")  
            sys.exit(f"Bye {name}! 👋")      
                

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description= "Provides a personalized game experience."
    )
    parser.add_argument(
        "-n", "--name" , metavar="name" ,
        required = True, help = "The name of the person playing the game"

    )

    args = parser.parse_args()
    print(f"\n{args.name}, welcome to the arcade! ..")
    play_game(args.name)
import sys
import random

def guess_number(name ='playerOne'):
    count_game = 0
    player_wins = 0
    def play_guess_number():
        nonlocal name
        nonlocal player_wins
         
        player_choice = input(f"\n{name},guess which number I'am thinking of ...1, 2 or 3 \n\n")
        if player_choice not in ["1","2","3"]:
            print(f"{name},please  enter 1, 2 or 3")
            return play_guess_number()
        computerchoice = random.choice("123")
        
        print("")
        print(f"\n{name},you chose {player_choice}.")
        print(f"I was thinking about the number {computerchoice} .\n")
        computer = int(computerchoice)
        player = int(player_choice)
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f" {name},  you win!🎉🎉🎉"
            else:
                return f" Sorry, {name} Better Luck next time..🥲"
            
        game_result =decide_winner(player, computer)
        print(game_result)
        nonlocal count_game 
        count_game += 1
        print(f"\nGamecount: {count_game}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\n Your wining percentage:{player_wins/count_game:.2%}")
        print(f"\nplay again? {name} ")
        while True:
            playagain = input("\n Play again? \n Y for Yes \nQ to Quit\n\n ")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("thankyou for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return
    return play_guess_number



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
    guess_my_number = guess_number(args.name)
    guess_my_number()
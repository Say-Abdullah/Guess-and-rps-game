import sys
import random
from enum import Enum

def rps(name ='playerOne'):
    count_game = 0
    player_wins = 0
    python_wins = 0
    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        player_choice = input(f"\n{name},please Enter...\n1 FOR ROCK \n 2 For paper or\n 3 for scissor\n")
        if player_choice not in ["1","2","3"]:
            print(f"{name},please you must enter 1, 2 or 3")
            return play_rps()
        player = int(player_choice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("")
        print(f"\n{name},you chose {str(RPS(player)).replace('RPS.','').title()} .")
        print(f"python chose {str(RPS(computer)).replace('RPS.', '').title()} .\n")
        print("")
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f" {name},  you win!🎉🎉🎉"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f" {name},  you win!🎉🎉🎉"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f" {name},  you win!🎉🎉🎉"
            elif player ==computer:
                return " 😲tie game"
            else:
                python_wins += 1
                return f" 🐍python wins! Sorry, {name}..🥲"
            
        game_result =decide_winner(player, computer)
        print(game_result)
        nonlocal count_game 
        count_game += 1
        print(f"\nGamecount: {count_game}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPythonwins: {python_wins}")
        while True:
            playagain = input("\n Play again? \n Y for Yes \nQ to Quit\n\n ")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("thankyou for playing!\n")
            if __name__=="__main__":
                 sys.exit(f"Bye {name}! 👋")
            else:
                return
    return play_rps     



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
    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()
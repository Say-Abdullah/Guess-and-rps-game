# 🎮 Python Arcade Games

**Python Arcade Games** is a collection of interactive, terminal-based mini-games built using Python. The main entry file `arcade.py` acts as a simple game hub that lets users choose between multiple games or exit the arcade.

---

## Overview

When you run the arcade, a main menu appears allowing the user to select:
- **1** → Play *Rock Paper Scissors*  
- **2** → Play *Guess the Number*  
- **3** → Exit the arcade  

The project demonstrates modular Python design, command-line argument handling, and smooth input validation, offering a fun and educational coding experience.

---

## Rock Paper Scissors (`rps.py`)

A command-line implementation of the classic *Rock Paper Scissors* game.  
The player launches the game with a personalized name using a command-line argument:

```bash
python rps.py -n Abdullah

Guess the Number (guess_number.py)

A simple number-guessing game where Python randomly selects a number within a range.
The player tries to guess the correct number with feedback provided after each attempt:

If the guess is too high or too low, the game gives a hint.

When the correct number is guessed, it displays how many attempts were made.

This game emphasizes logic, repetition control, and user feedback handling.

Running the Arcade

Start the arcade from your terminal:

**python arcade.py**


Follow the on-screen prompts to choose a game or exit.
Each game runs independently and returns control to the arcade when finished.

**Features**

🎯 Interactive and beginner-friendly games

👤 Personalized gameplay using command-line arguments

🔁 Clean input validation and replay logic

🧩 Modular structure for easy extension

🪶 Lightweight and runs entirely in the terminal

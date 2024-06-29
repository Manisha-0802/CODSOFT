import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
    

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return"IT'S  A  TIE!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "YOU WIN!"
    
    else:
        return "COMPUTER WINS!"
#Function to play the game
def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result",f"YOU CHOSE:  {user_choice}\nCOMPUTER CHOSE:  {computer_choice}\n\n{result}")


#Create the main window
def main():
     root = tk.Tk()
     root.title("Rock-Paper-Scissors")
#Create and place buttons
     rock_button = tk.Button(root, text="Rock", width=20, command=lambda:play_game("rock"))
     rock_button.pack(pady=10)

     paper_button = tk.Button(root, text="Paper", width=20, command=lambda:play_game("paper"))
     paper_button.pack(pady=10)

     scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda:play_game("scissors"))
     scissors_button.pack(pady=10)
    
                        
#Start the Tkinter event loop
if __name__ == "__main__":
    
    
    main()

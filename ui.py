import random
import tkinter as tk
from tkinter import messagebox

class CardGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Card Game")
        self.money = 50
        self.high_score = 0

        self.intro_banner()

        self.playername_label = tk.Label(self.window, text="Player Name:")
        self.playername_label.pack()
        self.playername_entry = tk.Entry(self.window)
        self.playername_entry.pack()

        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def intro_banner(self):
        print("Welcome to the Game!")

    def start_game(self):
        self.playername = self.playername_entry.get()
        self.intro_label = tk.Label(self.window, text=f"Welcome, {self.playername}! Your starting amount is {self.money} Gold.")
        self.intro_label.pack()

        self.bet_label = tk.Label(self.window, text="Place your bet:")
        self.bet_label.pack()
        self.bet_entry = tk.Entry(self.window)
        self.bet_entry.pack()

        self.play_button = tk.Button(self.window, text="Play", command=self.play_round)
        self.play_button.pack()

    def play_round(self):
        # Remove existing GUI elements
        self.bet_label.pack_forget()
        self.bet_entry.pack_forget()
        self.play_button.pack_forget()

        # Remove previous win/loss message
        if hasattr(self, "money_label"):
            self.money_label.destroy()
            del self.money_label

        # Get the new bet from the user
        bet = int(self.bet_entry.get())
        player_card = random.randint(1, 12)
        cpu_card = random.randint(1, 12)

        result = self.compare_cards(player_card, cpu_card, bet)
        self.update_money(result)

        # Show the updated bet and the result of the round
        self.bet_label = tk.Label(self.window, text=f"Your bet: {bet} Gold")
        self.bet_label.pack()

        if result == "win":
            self.money_label = tk.Label(self.window, text="You won!")
        elif result == "lose":
            self.money_label = tk.Label(self.window, text="You lost!")
        else:
            self.money_label = tk.Label(self.window, text="It's a draw!")
        self.money_label.pack()

        # Re-add the GUI elements related to the bet and the "Play" button
        self.bet_label = tk.Label(self.window, text="Place your bet:")
        self.bet_label.pack()
        self.bet_entry = tk.Entry(self.window)
        self.bet_entry.pack()
        self.play_button = tk.Button(self.window, text="Play", command=self.play_round)
        self.play_button.pack()

    def update_money(self, result):
        if result == "win":
            self.money += int(self.bet_entry.get())
        elif result == "lose":
            self.money -= int(self.bet_entry.get())

        if self.money > self.high_score:
            self.high_score = self.money
            with open("high_score.txt", "w") as file:
                file.write(f"{self.playername}: {self.high_score}")

        self.money_label = tk.Label(self.window, text=f"Your money: {self.money} Gold")
        self.money_label.pack()

        if self.money < 0:
            messagebox.showinfo("Game Over", "You're out of money!")
            self.window.quit()

    def __init__(self):
        self.load_high_score()
        try:
            with open("high_score.txt", "r") as file:
                high_score_str = file.read().strip()  # Remove leading/trailing whitespaces
                if high_score_str:
                    self.high_score = int(high_score_str)
                else:
                    self.high_score = 0  # Set a default value if the file is empty
        except FileNotFoundError:
            self.high_score = 0  # Set a default value if the file is not found

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                high_score_str = file.read().strip()  # Remove leading/trailing whitespaces
                if high_score_str:
                    player_name, score_str = high_score_str.split(":")
                    self.high_score = int(score_str.strip())
                    self.playername = player_name.strip()
                else:
                    self.high_score = 0  # Set a default value if the file is empty
        except FileNotFoundError:
            self.high_score = 0  # Set a default value if the file is not found

        self.high_score_label = tk.Label(self.window, text=f"High Score: {self.high_score} Gold (by {self.playername})")
        self.high_score_label.pack()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Card Game")
        self.money = 50
        self.high_score = 0

        self.intro_banner()

        self.playername_label = tk.Label(self.window, text="Player Name:")
        self.playername_label.pack()
        self.playername_entry = tk.Entry(self.window)
        self.playername_entry.pack()

        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def compare_cards(self, player_card, cpu_card, bet):
        # Compare the player's card and the CPU's card
        if player_card > cpu_card:
            return "win"
        elif player_card < cpu_card:
            return "lose"
        else:
            return "draw"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = CardGame()
    game.run()

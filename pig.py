import random
import sys

class Player:
    """Creates player class for Pig, takes inputs"""
    def __init__(self):
        self.score = 0
        self.tempscore = 0
        self.turn_order = 0
        self.turn = False

    def turnlogic(self):
        """takes inputs to roll or hold, checks for bust, calculates score"""
        print("Player's turn")
        while self.turn:
            choice = input("Would you like to [r]oll or [h]old?").lower()
            if choice == "r":
                roll = random.randint(1,6)
                if roll > 1:
                    self.tempscore = self.tempscore + roll
                    print(f"You rolled a {roll}. Your total is {self.tempscore}.")
                else:
                    self.tempscore = 0
                    self.turn = False
                    print(f"You rolled a {roll}. You busted.")
            elif choice == "h":
                self.score = self.score + self.tempscore
                print(f"Your total this turn was {self.tempscore}.")
                print(f"Your overall total is {self.score}.")
                print("The AI's overall total is", a.score)
                self.tempscore = 0
                self.turn = False
            else:
                print("That was not a valid selection. Please enter r for roll or h for hold.")
        g.winstatus()
        a.turn = True


class AI:
    """Creates AI class for Pig, takes no input, logic works automatically, rolls until 20+"""
    def __init__(self):
        self.score = 0
        self.tempscore = 0
        self.turn_order = 0
        self.turn = False

    def turnlogic(self):
        """AI keeps rolling until the score reaches at least 20, then it will hold, keeps track
        of score"""
        print("AI's turn")
        while self.tempscore < 20 and self.turn == True:
            roll = random.randint(1,6)
            if roll > 1:
                self.tempscore = self.tempscore + roll
                print(f"The AI rolled a {roll}. Its total is {self.tempscore}.")
            else:
                self.tempscore = 0
                self.turn = False
                print(f"The AI rolled a {roll}. The AI busted.")
        self.score = self.score + self.tempscore
        print("The AI's total this turn was", self.tempscore)
        print("The AI's overall total is", self.score)
        print(f"Your overall total is {p.score}.")
        g.winstatus()
        p.turn = True

class Game:
    """Run the gamestate logic, defines who goes first, checks for winner, 
    asks if you want to replay"""
    def __init__(self):
        self.replay = True

    def start_game(self):
        """basic running order for methods"""
        gamestate = True
        while gamestate:
            g.turnorder()
            p.turnlogic()
            a.turnlogic()

    def turnorder(self):
        """quick check at game start to see who goes first"""
        self.turn = random.randint(0,1)
        if self.turn == 0:
            p.turn = True
        else:
            a.turn = True

    def winstatus(self):
        """checks to see if player or AI has reached score of 100, takes input to see if you 
        want to play again or exits if not"""
        if p.score >= 100:
            print("You win!")
            print("Your total was", p.score)
            print("The AI's total was", a.score)
            replay = input("Would you like to play again? y/n?").lower()
            if replay == "y":
                p.score = 0
                a.score = 0
                g.start_game()
            elif replay == "n":
                sys.exit()
            else:
                replay = input("Would you like to play again? y/n?").lower()

        elif a.score >= 100:
            print("You lose!")
            print("The AI's total was", a.score)
            print("Your total was", p.score)
            replay = input("Would you like to play again? y/n?").lower()
            if replay == "y":
                p.score = 0
                a.score = 0
                g.start_game()
            elif replay == "n":
                sys.exit()
            else:
                g.winstatus()

if __name__ == "__main__":
    g = Game()
    p = Player()
    a = AI()
    g.start_game()    
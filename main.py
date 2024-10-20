import random
import string
import logging


class TreasureMap:
    def __init__(self):
        self.treasure = self._generate_treasure()

    def _generate_treasure(self):
        x = random.randint(1, 10)
        y = random.choice(string.ascii_uppercase[:10])
        return (x, y)

    def check_guess(self, guess):
        return guess == self.treasure

    def provide_clue(self, guess):
        x_diff = abs(guess[0] - self.treasure[0])
        y_diff = abs(ord(guess[1]) - ord(self.treasure[1]))
        
        if x_diff == 0 and y_diff == 0:
            return "Very hot!"
        if x_diff <= 1 and y_diff <= 1:
            return "Hot!"
        if x_diff <= 3 and y_diff <= 3:
            return "Warm."
        return "Cold."


class Player:
    def __init__(self, max_attempts):
        self.attempts = max_attempts
        self.guesses = []

    def make_guess(self):
        while True:
            try:
                guess_input = input("Enter coordinates (X,Y) where X is 1-10 and Y is A-J: ").strip()
                x, y = guess_input.split(',')
                x = int(x)
                y = y.strip().upper()
                if 1 <= x <= 10 and y in string.ascii_uppercase[:10]:
                    guess = (x, y)
                    self.guesses.append(guess)
                    return guess
                print("Invalid input. Please try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter coordinates in the format 'X,Y' (e.g., '5,C').")


class Game:
    def __init__(self, max_attempts):
        self.treasure_map = TreasureMap()
        self.player = Player(max_attempts)
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(
            filename='log.txt',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def start(self):
        print("Welcome to the Treasure Hunt Game!")
        print("The playing field is a 10x10 grid. X: 1-10, Y: A-J")
        print("Enter coordinates in the format 'X,Y' (e.g., '5,C')")
        
        while self.player.attempts > 0:
            self._display_info()
            guess = self.player.make_guess()
            self.player.attempts -= 1
            logging.info(f"Player guessed: {guess}")
            
            if self.treasure_map.check_guess(guess):
                self._display_win()
                return True
            
            clue = self.treasure_map.provide_clue(guess)
            self._display_clue(clue)
        
        self._display_game_over()
        return False

    def _display_info(self):
        print(f"\nAttempts left: {self.player.attempts}")

    def _display_clue(self, clue):
        print(f"Clue: {clue}")
        logging.info(f"Clue provided: {clue}")

    def _display_win(self):
        print("Congratulations! You found the treasure!")
        logging.info("Player won the game")

    def _display_game_over(self):
        print("Game Over! You've run out of attempts.")
        print(f"The treasure was at {self.treasure_map.treasure}")
        logging.info("Game over - player ran out of attempts")

if __name__ == '__main__':
    max_attempts = 10
    game = Game(max_attempts)
    game.start()






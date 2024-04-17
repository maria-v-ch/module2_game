import random


class TreasureMap:
    def __init__(self):
        pass

    def set_treasure(self, x_key: int, y_key: str):
        return (x_key, y_key)

    def check_guess(self, guess: (int, str), treasure: (int, str), attempts: int):
        while guess != treasure:
            attempts -= 1
            print(f'Nice try, but wrong! Try again. Attempts left: {attempts}.')
            for index, element in enumerate(guess):


        else:
            print(f'You have just found the treasure!')


if __name__ == '__main__':
    x_key = random.randint(1, 10)
    y_key = random.choice(string.ascii_letters[0: 9])
    treasure_game = TreasureMap()



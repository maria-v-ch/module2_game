import random


class TreasureMap:
    def __init__(self):
        pass

    def set_treasure(self, x_key: int, y_key: str):
        treasure = (x_key, y_key)
        return treasure

    def check_guess(self, guess: (int, str), treasure: (int, str), attempts: int):
        while guess != treasure:
            attempts -= 1
            print(f'Nice try, but wrong! Try again. Attempts left: {attempts}.')
            for index, element in enumerate(guess):


        else:
            print(f'You have just found the treasure!')


if __name__ == '__main__':
    x_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'J']
    x_key: int = random.choice(x_keys)
    y_key: str = random.choice(y_keys)



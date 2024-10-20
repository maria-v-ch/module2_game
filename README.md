# Treasure Hunt Game

This is a simple command-line Treasure Hunt game implemented in Python. The game generates a random treasure location on a 10x10 grid, and the player must guess the location within a limited number of attempts.

## Features

- Random treasure generation
- Player guessing mechanism
- Clue system based on proximity to the treasure
- Logging of game events

## How to Play

1. Run the `main.py` file to start the game.
2. Enter coordinates in the format "X,Y" where X is a number from 1 to 10 and Y is a letter from A to J.
3. The game will provide clues after each guess:
   - "Very hot!": You're very close to the treasure
   - "Hot!": You're close to the treasure
   - "Warm.": You're getting closer
   - "Cold.": You're far from the treasure
4. Keep guessing until you find the treasure or run out of attempts.

## Classes and Methods

### TreasureMap

- `generate_treasure()`: Generates a random treasure location.
- `check_guess(guess)`: Checks if the guess matches the treasure location.
- `provide_clue(guess)`: Provides a clue based on the proximity of the guess to the treasure.

### Player

- `make_guess()`: Prompts the player for a guess and validates the input.

### Game

- `start()`: Initiates and manages the main game loop.
- `display_info()`: Displays the number of attempts left.
- `display_clue(clue)`: Displays the clue to the player.
- `display_win()`: Displays the win message.
- `display_game_over()`: Displays the game over message.

## Logging

The game logs events to a file named `log.txt`. This includes player guesses, clues provided, and game outcomes.

## Running Tests

To run the unit tests:

1. Ensure you have the `unittest` module (it comes with Python standard library).
2. Run the command: `python -m unittest test_treasure_hunt.py`

## Requirements

- Python 3.x

## Future Improvements

- Add difficulty levels
- Implement a graphical user interface
- Add multiplayer functionality

Feel free to contribute to this project by submitting pull requests or reporting issues!

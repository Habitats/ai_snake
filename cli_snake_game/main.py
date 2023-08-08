import curses
import argparse
from game import Game

def main(stdscr, speed):
  # Set up the screen
  curses.curs_set(0)
  stdscr.nodelay(1)
  stdscr.timeout(10)

  # Create a new game
  game = Game(stdscr, speed)

  # Start the game
  game.start_game()

  # Refresh the screen
  stdscr.refresh()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='CLI Snake Game')
  parser.add_argument('--speed', type=int, default=10, help='Game speed')
  args = parser.parse_args()

  # Start the game
  curses.wrapper(main, args.speed)

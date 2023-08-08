import curses
import threading
from snake import Snake
from food import Food

class Game:
    def __init__(self, stdscr, speed: int = 10):
        self.score = 0
        self.speed = speed
        self.stdscr = stdscr
        self.snake = Snake()
        self.food = Food()

    def start_game(self):
        threading.Thread(target=self.run_game).start()
        while True:
            key = self.stdscr.getch()
            self.snake.change_direction(key)

    def run_game(self):
        while True:
            self.stdscr.clear()
            self.snake.move()
            self.check_collision()
            self.update_score()
            self.draw()
            self.stdscr.refresh()
            curses.napms(1000 // self.speed)

    def check_collision(self):
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.generate()
            self.score += 1
        elif self.snake.body[0] in self.snake.body[1:]:
            self.end_game()

    def update_score(self):
        score_text = "Score: {}".format(self.score)
        self.stdscr.addstr(0, 0, score_text)

    def draw(self):
        for segment in self.snake.body:
            self.stdscr.addch(segment[0], segment[1], '#')
        self.stdscr.addch(self.food.position[0], self.food.position[1], '*')

    def end_game(self):
        self.stdscr.addstr(0, 0, "Game Over! Score: {}".format(self.score))
        self.stdscr.refresh()
        curses.napms(2000)
        curses.endwin()
        quit()

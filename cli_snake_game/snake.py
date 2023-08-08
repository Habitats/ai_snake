import random
import curses

class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 9), (10, 8)]
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0]
        if self.direction == "RIGHT":
            new_head = (head[0], head[1] + 1)
        elif self.direction == "LEFT":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "UP":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "DOWN":
            new_head = (head[0] + 1, head[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        if self.direction == "RIGHT":
            new_tail = (tail[0], tail[1] - 1)
        elif self.direction == "LEFT":
            new_tail = (tail[0], tail[1] + 1)
        elif self.direction == "UP":
            new_tail = (tail[0] + 1, tail[1])
        elif self.direction == "DOWN":
            new_tail = (tail[0] - 1, tail[1])
        self.body.append(new_tail)

    def change_direction(self, key):
        if key == curses.KEY_RIGHT and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif key == curses.KEY_LEFT and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif key == curses.KEY_UP and self.direction != "DOWN":
            self.direction = "UP"
        elif key == curses.KEY_DOWN and self.direction != "UP":
            self.direction = "DOWN"

class Food:
    def __init__(self):
        self.position = (random.randint(1, 20), random.randint(1, 60))

    def generate(self):
        self.position = (random.randint(1, 20), random.randint(1, 60))

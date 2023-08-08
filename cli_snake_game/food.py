import random

class Food:
    def __init__(self):
        self.position = (random.randint(1, 20), random.randint(1, 60))

    def generate(self):
        self.position = (random.randint(1, 20), random.randint(1, 60))

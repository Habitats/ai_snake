import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_init(self):
        self.assertEqual(self.snake.body, [(10, 10), (10, 9), (10, 8)])
        self.assertEqual(self.snake.direction, "RIGHT")

    def test_move_right(self):
        self.snake.move()
        self.assertEqual(self.snake.body, [(10, 11), (10, 10), (10, 9)])

    def test_move_left(self):
        self.snake.direction = "LEFT"
        self.snake.move()
        self.assertEqual(self.snake.body, [(10, 9), (10, 10), (10, 11)])

    def test_move_up(self):
        self.snake.direction = "UP"
        self.snake.move()
        self.assertEqual(self.snake.body, [(9, 10), (10, 10), (10, 11)])

    def test_move_down(self):
        self.snake.direction = "DOWN"
        self.snake.move()
        self.assertEqual(self.snake.body, [(11, 10), (10, 10), (10, 11)])

    def test_grow(self):
        self.snake.grow()
        self.assertEqual(self.snake.body, [(10, 10), (10, 9), (10, 8), (10, 7)])

    def test_change_direction(self):
        self.snake.change_direction("LEFT")
        self.assertEqual(self.snake.direction, "LEFT")
        self.snake.change_direction("UP")
        self.assertEqual(self.snake.direction, "UP")
        self.snake.change_direction("DOWN")
        self.assertEqual(self.snake.direction, "DOWN")
        self.snake.change_direction("RIGHT")
        self.assertEqual(self.snake.direction, "RIGHT")

if __name__ == "__main__":
    unittest.main()

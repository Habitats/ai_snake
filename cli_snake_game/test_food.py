import unittest
from food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food()

    def test_init(self):
        self.assertIsNotNone(self.food.position)

    def test_generate(self):
        old_position = self.food.position
        self.food.generate()
        self.assertNotEqual(self.food.position, old_position)

if __name__ == "__main__":
    unittest.main()

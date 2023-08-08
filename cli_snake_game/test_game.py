import unittest
import curses
from unittest.mock import patch
from game import Game
from snake import Snake
from food import Food

class TestGame(unittest.TestCase):
    @patch('curses.initscr')
    def setUp(self, mock_stdscr):
        self.game = Game(mock_stdscr, 10)

    def test_init(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.speed, 10)
        self.assertIsInstance(self.game.snake, Snake)
        self.assertIsInstance(self.game.food, Food)

    @patch.object(Snake, 'change_direction')
    def test_start_game(self, mock_change_direction):
        with patch.object(Game, 'run_game'):
            self.game.start_game()
            self.game.stdscr.getch.assert_called()
            mock_change_direction.assert_called_with(self.game.stdscr.getch.return_value)

    @patch.object(Snake, 'move')
    @patch.object(Game, 'check_collision')
    @patch.object(Game, 'update_score')
    @patch.object(Game, 'draw')
    def test_run_game(self, mock_draw, mock_update_score, mock_check_collision, mock_move):
        with patch('curses.napms'):
            self.game.run_game()
            mock_move.assert_called()
            mock_check_collision.assert_called()
            mock_update_score.assert_called()
            mock_draw.assert_called()
            self.game.stdscr.clear.assert_called()
            curses.napms.assert_called_with(1000 // self.game.speed)

    @patch.object(Snake, 'grow')
    @patch.object(Food, 'generate')
    def test_check_collision_with_food(self, mock_generate, mock_grow):
        self.game.snake.body[0] = self.game.food.position
        self.game.check_collision()
        mock_grow.assert_called()
        mock_generate.assert_called()
        self.assertEqual(self.game.score, 1)

    @patch('curses.endwin')
    def test_check_collision_with_self(self, mock_endwin):
        self.game.snake.body.append(self.game.snake.body[0])
        with self.assertRaises(SystemExit):
            self.game.check_collision()
        self.game.stdscr.addstr.assert_called_with(0, 0, "Game Over! Score: {}".format(self.game.score))
        self.game.stdscr.refresh.assert_called()
        mock_endwin.assert_called()

    def test_update_score(self):
        self.game.update_score()
        self.game.stdscr.addstr.assert_called_with(0, 0, "Score: {}".format(self.game.score))

    @patch.object(curses.window, 'addch')
    def test_draw(self, mock_addch):
        self.game.draw()
        for segment in self.game.snake.body:
            mock_addch.assert_any_call(segment[0], segment[1], '#')
        mock_addch.assert_called_with(self.game.food.position[0], self.game.food.position[1], '*')

if __name__ == "__main__":
    unittest.main()

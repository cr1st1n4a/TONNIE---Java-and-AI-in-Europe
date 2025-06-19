import unittest
from unittest.mock import patch
import quiz

class TestQuiz(unittest.TestCase):

    def test_check_answer_correct(self):
        self.assertTrue(quiz.check_answer('a', 'a'))
        self.assertFalse(quiz.check_answer('b', 'a'))

    def test_show_question_valid_answer(self):
        question = {
            "question": "Qual é a capital do Brasil?",
            "answers": {"a": "Brasília", "b": "Rio", "c": "SP", "d": "Salvador"},
            "correct_answer": "a"
        }
        with patch('builtins.input', return_value='a'):
            self.assertEqual(quiz.show_question(question), 'a')

    def test_show_question_invalid_answer(self):
        question = {
            "question": "Qual é a capital do Brasil?",
            "answers": {"a": "Brasília", "b": "Rio", "c": "SP", "d": "Salvador"},
            "correct_answer": "a"
        }
        with patch('builtins.input', return_value='x'):
            with self.assertRaises(ValueError):
                quiz.show_question(question)

    def test_show_question_timeout(self):
        question = {
            "question": "Qual é a capital do Brasil?",
            "answers": {"a": "Brasília", "b": "Rio", "c": "SP", "d": "Salvador"},
            "correct_answer": "a"
        }
        # Simula o input nunca sendo chamado (timeout)
        with patch('builtins.input', side_effect=lambda *a, **k: None):
            with self.assertRaises(ValueError):
                quiz.show_question(question)

    def test_feedback_messages(self):
        # Testa os feedbacks finais
        with patch('builtins.print') as mock_print:
            with patch('quiz.show_question', side_effect=['a', 'b', 'c', 'd', 'a']):
                with patch('quiz.check_answer', side_effect=[False, False, False, False, False]):
                    quiz.main()
                    self.assertIn(
                        unittest.mock.call("Você precisa estudar mais."),
                        mock_print.mock_calls
                    )
            with patch('quiz.show_question', side_effect=['a', 'a', 'a', 'a', 'a']):
                with patch('quiz.check_answer', side_effect=[True, False, False, False, False]):
                    quiz.main()
                    self.assertIn(
                        unittest.mock.call("Você foi bem, mas ainda pode melhorar."),
                        mock_print.mock_calls
                    )
            with patch('quiz.show_question', side_effect=['a', 'a', 'c', 'b', 'd']):
                with patch('quiz.check_answer', side_effect=[True, True, True, True, True]):
                    quiz.main()
                    self.assertIn(
                        unittest.mock.call("Parabéns, você foi bem!"),
                        mock_print.mock_calls
                    )

if __name__ == '__main__':
    unittest.main()
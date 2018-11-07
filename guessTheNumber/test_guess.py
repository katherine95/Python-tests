import unittest
from guess import guessNum
from unittest.mock import patch

'''test class inherits from unittest.Testcase'''
class TestGuessNum(unittest.TestCase):
    @patch('yourmodule.get_input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')



'''To allow to run this module directly'''
if __name__ == '__main__':
    unittest.main()

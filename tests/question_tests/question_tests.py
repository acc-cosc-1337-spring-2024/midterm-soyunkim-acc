import unittest

from src.question_a.question_a import get_random_number, test_config
from src.question_b.question_b import use_local_variable
from src.question_c.question_c import get_sum_of_evens
from src.question_d.question_d import use_global

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_random_numbers(self):
        random_number = get_random_number()
        self.assertEqual((1 <= random_number <= 5), True)

    def test_use_local_variable(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)

    def test_get_sum_of_evens(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)

    def test_global_variable(self):
        global global_variable
        global_variable = 5
        use_global()
        self.assertEqual(global_variable, 5)
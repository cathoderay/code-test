import unittest
from problem1 import solve


class TestProblem1(unittest.TestCase):
    def test_only_three_numbers_given(self):
        self.assertEqual(1*2*3, solve([1, 2, 3])) 

    def test_less_than_3_numbers_given(self):
        self.assertRaises(Exception, solve, [])
        self.assertRaises(Exception, solve, [1])
        self.assertRaises(Exception, solve, [1, 2])

    def test_more_than_three_numbers(self):
        self.assertEqual(4*3*2, solve([1, 2, 3, 4]))

    def test_3_negative_numbers(self):
        self.assertEqual(-6, solve([-1, -2, -3]))

    def test_only_zeroes(self):
        self.assertEqual(0, solve([0]*10))

    def test_only_equal_negative_numbers(self):
        self.assertEqual(-1, solve([-1]*10))

    def test_arithmetic_progression(self):
        self.assertEqual(10*9*8, solve(list(range(11))))

    def test_negative_arithmetic_progression(self):
        self.assertEqual(-3*-4*-5, solve(list(range(-20, -2))))

    def test_three_same(self):
        self.assertEqual(3*3*3, solve([1, 1, 3, 3, 3]))

    def test_reverse_input(self):
        self.assertEqual(3*2*1, solve([3, 2, 1, 0]))

    def test_random_input(self):
        self.assertEqual(3*2*1, solve([2, 0, 1, 3, 0]))
        self.assertEqual(3*2*2, solve([2, 0, 1, 3, 2]))
        self.assertEqual(3*3*4, solve([2, 0, 4, 3, 3, 3]))
        self.assertEqual(3*3*3, solve([-1, 3, 3, 3, 3]))
        self.assertEqual(500, solve([-10, -10, 1, 5]))
        self.assertEqual(6, solve([1, 2, 3]))

    def test_example_problem(self):
        self.assertEqual(300, solve([1, 10, 2, 6, 5, 3]))


if __name__ == '__main__':
    unittest.main()

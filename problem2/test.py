import unittest
from problem2 import untokenize, tokenize, solve, \
                     infix2postfix, eval_postfix, \
                     is_unary 


class Test(unittest.TestCase):
    def test_tokenize(self):
        io = (("42 + 2", ["42", "+", "2"]),
              (" 42 -2", ["42", "-", "2"]),
              (" 42* 2", ["42", "*", "2"]),
              ("42 / 2", ["42", "/", "2"]), 
              ("5-(1+2)", ["5","-", "(", "1", "+", "2", ")" ]), 
              ("(1/534.34)*2)", ["(","1","/","534.34",")","*","2",")"]))
        for i, o in io:
            self.assertEqual(tokenize(i), o)

    def test_untokenize(self):
        io = ((["42", "+", "2"], "42 + 2"),
              (["42", "-", "2"], "42 - 2"),
              (["42", "*", "2"], "42 * 2"),
              (["42", "/", "2"], "42 / 2"),
              (["(","1","/","534.34",")","*","2",")"], "( 1 / 534.34 ) * 2 )"))
        for i, o in io:
            self.assertEqual(untokenize(i), o)

    def test_is_unary(self):
        io = ((0, ('-1 * 4')),
              (2, ('1 * -4')),
              (8, ('(1 + 34 -7)-(-1)')))
        for i, o in io:
            self.assertTrue(is_unary(i, tokenize(o)))

    def test_is_not_unary(self):
        io = ((1, ('1 - 4')),
              (4, ('1 * (5 --3)')),
              (8, ('(1 + -34 -7)-(-1)')))
        for i, o in io:
            self.assertFalse(is_unary(i, tokenize(o)))

    def test_infix2postfix(self):
        io = (('42 + 2', '42 2 +'),
              ('4 * (5 - 7)', '4 5 7 - *'),
              ('1 * (2 * 6 / 3)', '1 2 6 * 3 / *'))
        for i, o in io:
            self.assertEqual(infix2postfix(i), o)

    def test_infix2postfix_unary_plus_and_minus(self):
        io = (('++1 -+-2', '1 2 @ -'),
              ('+1 / -2', '1 2 @ /'),
              ('--42 + 2', '42 @ @ 2 +'),
              ('  4 * - (-5 - +7)', '4 5 @ 7 - @ *'),
              ('-1 * +(-2 * 6 / +3)', '1 @ 2 @ 6 * 3 / *'),
              ('-1*(+2 + -3)', '1 @ 2 3 @ + *'),
              ('-4 * + + 5', '4 @ 5 *'))
        for i, o in io:
            self.assertEqual(infix2postfix(i), o)

    def test_eval_postfix(self):
        io = (('1 2 6 3 / * *', 4),
              ('1 @ 2 6 3 / * *', -4),
              ('5  @34  2 / +', 12),
              ('6 @ 3 5 - *', 12))
        for i, o in io:
            self.assertEqual(eval_postfix(i), o)

    def test_solve(self):
        io = (('- 1 * (2   * 6/3 ) ', -4),
              ('2 * 5 / 2 + 1 - (50-47)', 3),
              ('34.75 *23.123', 803),
              ('+5 - 3 ++ 2', 4),
              ('8 / 9* -0', 0),
              ('++--+8 + +- 2 * 3', 2),
              ('+--+-(2+3 *2())+-(3*((6/3*4)))', -32),
              ('(1+(3*(4+1))-9/3)', 13),
              ('3.51 + 6.49', 10),
              ('5 - 3 + 2 - 4 + 3', 3))
        for i, o in io:
            self.assertEqual(solve(i), o)

    def test_solve_with_division_by_zero_error(self):
        self.assertRaises(ZeroDivisionError, solve, '1/(5-5)')

    def test_unbalanced_parenthesis_error(self):
        self.assertRaises(Exception, solve, '1/(5-5')

    def test_malformed_expressions_error(self):
        self.assertRaises(Exception, solve, '1//*4')
        self.assertRaises(Exception, solve, '1//)*4')


if __name__ == "__main__":
    unittest.main()

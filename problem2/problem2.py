

def tokenize(s):
    """Transforms a single mathematical 
    expression (string) into a list of 
    tokens (strings) to be processed.

    Example:
        input: '-1 * (4  +  3)'
        output: ['-','1','*','(','4','+','3',')']

    Assumptions:
        The input can contain any character
        in: "0123456789./*+-@()", where @ is the
        unary minus operator.

    Algorithm analysis:
        Space: O(n)
        Time: O(n)
    """
    
    tokens = []
    buff = ''
    for char in s:
        if char in "0123456789.":
            buff += char
        else:
            if len(buff) > 0:
                tokens.append(buff)
                buff = ''
            if char in "()*+-/@":
                tokens.append(char)
    if len(buff) > 0:
        tokens.append(buff)
    return tokens


def untokenize(l):
    return ' '.join(l)


def is_unary(index, tokens):
    return index == 0 or \
           tokens[index - 1] == "(" or \
           tokens[index - 1] in "-+/*"


def infix2postfix(s):
    """Transforms a mathematical expression
    originally in infix notation into its
    representation in postfix (Reverse 
    Polish Notation).

    Example:
        input: '4 * (5 - 7)'
        output: '4 5 7 - *'

    Assumptions:
        * If an unary minus is found it will
        be replaced by @. 

        * Unary plus is discarded. 
            Example:
                input: '-4 * + + 5'
                output: '4 @ 5 *'

        * If the infix expression is 
        ambiguous as: '4 / 4 * 3', it 
        assumes a left associative approach.

    Algorithm analysis:
        Space: O(n)
        Time: O(n)
    """
    tokens = tokenize(s)
    prec = {'-': 1, '+': 1, 
            '/': 2, '*': 2, 
            '@': 3}
    out = []
    stack = []
    for i, token in enumerate(tokens):
        if token[0] in "0123456789.":
            out.append(token) 
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] is not "(":
                out.append(stack.pop()) 
            stack.pop() # "("
        else:
            if is_unary(i, tokens):
                if token == "-":
                    stack.append("@")
                    continue
                elif token == "+":
                    continue 
                else: raise Exception
            while len(stack) > 0 and \
                  stack[-1] in "-+/*@" and \
                  prec[token] <= prec[stack[-1]]:
                out.append(stack.pop())
            stack.append(token)
    while len(stack) > 0:
        out.append(stack.pop())
    return untokenize(out)


def eval_postfix(s):
    from operator import add, sub, truediv, mul

    """Evaluates a postfix expression with 
    binary operators: +, -, / and * and unary
    operator @ (unary minus)."""

    op = {'+': add, '-': sub,
          '/': truediv, '*': mul}

    tokens = tokenize(s) 
    stack = []
    for token in tokens:
        if token[0] in "0123456789.":
            stack.append(float(token))
        else:
            if token == "@":
                stack.append(-1*stack.pop())
            else:
                f = op[token]
                b = stack.pop()
                a = stack.pop()
                stack.append(f(a, b))
    return int(stack[0])


def solve(s):
    """Given a mathematical expression with basic
    operators (-, +, / and *) and integers or real 
    numbers and returns its evaluation. It deals
    with unary operator minus (which is converted 
    internally to @), unary operator plus (which is 
    deliberately discarded), brackets and precedence
    of operators and multiple blank spaces. 
    The final answer is truncated to int type.
    Example:
        input: '-1 * (2* 6/ 3)'
        output: -4

    p.s.: the function 'tokenize' could be avoided
    between some function calls and thus, reducing
    the total processing time, but it was designed
    to help with the TDD process and it does not
    harm the overall asymptotic analysis.
    """
    return eval_postfix(infix2postfix(s))

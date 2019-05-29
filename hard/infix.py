"""Simple infix calculator.

    >>> calc("1 + 2")
    3

    >>> calc("2 * 3")
    6

    >>> calc("2 * ( 1 + 2 )")
    6

    >>> calc("( 2 * 1 ) + 2")
    4

    >>> calc("( ( 1 + 2 ) * ( 3 + 4 ) ) - ( 2 * ( 1 + 3 ) )")
    13
"""


def calc(s):
    """Simple infix calculator."""

    from collections import deque

    tokens = deque(s.split())
    return calc_expression(tokens)

def calc_expression(tokens):
    first = tokens.popleft()

    if first == "(":
        calc_expression(first)
    else:
        first = int(first)

    operator = tokens.popleft()
    second = tokens.popleft()

    if second == "(":
        return calc_expression(tokens)
    else:
        second = int(second)

    if tokens:
        assert tokens.popleft() == ")"

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    else:
        raise Exception("bad operator")
    return result

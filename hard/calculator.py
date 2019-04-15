"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    nums = s.split()
    operand2 = int(nums.pop())

    while nums:
        operand1 = int(nums.pop())
        operator = nums.pop()
        if operator == "+":
            operand2 = operand1 + operand2
        elif operator == "-":
            operand2 = operand1 - operand2
        elif operator == "*":
            operand2 = operand1 * operand2
        elif operator == "/":
            operand2 = operand1 // operand2
    return operand2



    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")

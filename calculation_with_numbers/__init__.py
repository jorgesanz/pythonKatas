def zero(operation=None):
    if operation is None:
        return 0
    return operate(operation[0], 0, operation[1])


def one(operation=None):
    if operation is None:
        return 1
    return operate(operation[0], 1, operation[1])


def two(operation=None):
    if operation is None:
        return 2
    return operate(operation[0], 2, operation[1])


def three(operation=None):
    if operation is None:
        return 3
    return operate(operation[0], 3, operation[1])


def four(operation=None):
    if operation is None:
        return 4
    return operate(operation[0], 4, operation[1])


def five(operation=None):
    if operation is None:
        return 5
    return operate(operation[0], 5, operation[1])


def six(operation=None):
    if operation is None:
        return 6
    return operate(operation[0], 6, operation[1])


def seven(operation=None):
    if operation is None:
        return 7
    return operate(operation[0], 7, operation[1])


def eight(operation=None):
    if operation is None:
        return 8
    return operate(operation[0], 8, operation[1])


def nine(operation=None):
    if operation is None:
        return 9
    return operate(operation[0], 9, operation[1])


def plus(operand):
    return "sum", operand


def minus(operand):
    return "sub", operand


def times(operand):
    return "mul", operand


def divided_by(operand):
    return "div", operand


def operate(operation, oper1, oper2):
    if operation == "mul":
        return oper1 * oper2
    if operation == "sum":
        return oper1 + oper2
    if operation == "sub":
        return oper1 - oper2
    if operation == "div":
        return oper1 / oper2

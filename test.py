#!/usr/bin/python3

from filter import *
from logic import *

def test():
    """Unit testing"""

    print("Testing is_integer()")
    assert is_integer("12") == True
    assert is_integer("9") == True
    assert is_integer("AB") == False

    print("Testing is_float()")
    assert is_float("12") == False
    assert is_float("12.0") == True
    assert is_float("12..0") == False
    assert is_float("abc") == False

    print("Testing is_parentheses()")
    assert is_parentheses("abc") == False
    assert is_parentheses("(") == True
    assert is_parentheses(")") == True
    assert is_parentheses("()") == False

    print("Testing is_valid_symbol()")
    assert is_valid_symbol("1.2") == True
    assert is_valid_symbol("1") == True
    assert is_valid_symbol("(") == True
    assert is_valid_symbol("") == False
    assert is_valid_symbol("abc") == False

    print("Testing is_multiplication()")
    assert is_multiplication("*") == True
    assert is_multiplication("!") == False

    print("Testing is_division()")
    assert is_division("/") == True
    assert is_division("!") == False

    print("Testing is_addition()")
    assert is_addition("+") == True
    assert is_addition("!") == False

    print("Testing is_subtraction()")
    assert is_subtraction("-") == True
    assert is_subtraction("!") == False

    print("Testing is_white_space()")
    assert is_white_space(" ") == True
    assert is_white_space("!") == False

    print("Testing convert_to_postfix_notation()")
    notation_1 = filter_for_valid_symbols("2 + 2")
    notation_2 = filter_for_valid_symbols("((2 + 2) * 3)")
    notation_3 = filter_for_valid_symbols("(3 + 4)*(5 - 6)")
    notation_4 = filter_for_valid_symbols("2 * 3 / 4")
    assert convert_to_postfix_notation(notation_1) == ["2","2","+"]
    assert convert_to_postfix_notation(notation_2) == ["2","2","+","3","*"]
    assert convert_to_postfix_notation(notation_3) == ["3","4","+","5","6","-","*"]
    assert convert_to_postfix_notation(notation_4) == ["2","3","*","4","/"]

if __name__ == "__main__":
    test()
#!/usr/bin/python3

def test():
    #print(is_integer("12"))
    #print(is_integer("9"))
    #print(is_integer("AB"))

    #print(is_float("12"))
    #print(is_float("12.0"))
    #print(is_float("12..4"))
    #print(is_float("abc"))

    #print(is_parentheses("abc"))
    #print(is_parentheses("("))
    #print(is_parentheses(")"))
    #print(is_parentheses("()"))

    #print(is_valid_symbol("1.2"))
    #print(is_valid_symbol("1"))
    #print(is_valid_symbol("("))
    #print(is_valid_symbol(""))
    #print(is_valid_symbol("abc"))

    #print(is_multiplication("*"))
    #print(is_multiplication("!"))

    #print(is_division("/"))
    #print(is_division("!"))

    #print(is_addition("+"))
    #print(is_addition("!"))

    #print(is_subtraction("-"))
    #print(is_subtraction("!"))

def main():
    print("Challenge Calculator")
    
    terms = input("Inpute Terms: ")
    print(terms)

def filter_for_valid_symbols(notation):
    """Filters all valid symbols and return a list"""

    filterd_notation = []
    temporer_notation = ""

    for character in notation:
        temporer_notation += character
        if is_valid_symbol(temporer_notation):
            filterd_notation.append(temporer_notation)
            temporer_notation = ""
    
    if len(temporer_notation) != 0:
        print(f"Error! Restnoation: {temporer_notation}")

def is_valid_symbol(symbol):
    """Check if symbol (string) is valid operator, operant or parentheses"""

    return is_operant(symbol) or is_operator(symbol) or is_parentheses(symbol)

def is_operator(symbol):
    """Check if symbol (string) is valid operator"""

    return False

def is_operant(symbol):
    """Check if symbol (string) is valid operant"""

    return is_integer(symbol) or is_float(symbol)

def is_parentheses(symbol):
    """Check if symbol (string) is a valid parentheses"""

    if len(symbol) != 1:
        return False
    elif symbol not in "()":
        return False

    return True

def is_multiplication(symbol):
    """Check if symbol (string) is multiplication operator"""
    
    if symbol not in "*":
        return False

    return True and not is_empty(symbol)

def is_division(symbol):
    """Check if symbol (string) is division operator"""
    
    if symbol not in "/":
        return False

    return True and not is_empty(symbol)

def is_addition(symbol):
    """Check if symbol (string) is addition operator"""
    
    if symbol not in "+":
        return False

    return True and not is_empty(symbol)

def is_subtraction(symbol):
    """Check if symbol (string) is subtraction operator"""
    
    if symbol not in "-":
        return False

    return True and not is_empty(symbol)

def is_integer(symbol):
    """Checks if an symbol (string) is a valid integer"""

    for character in symbol:
        if character not in "0123456789":
            return False
    
    return True and not is_empty(symbol)

def is_float(symbol):
    """Checks if an symbol (string) is a valid float"""

    dot_detected = False

    for character in symbol:
        if character not in ".0123456789":
            return False
        if character in ".":
            if dot_detected:
                return False
            dot_detected = True
    
    return True and dot_detected and not is_empty(symbol)

def is_empty(symbol):
    """Checks if symbol (string) is empty"""

    if len(symbol) != 0:
        return False

    return True

def transform_to_prefix_notation(infix_notation):
    pass

test()
#main()
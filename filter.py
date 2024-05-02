def is_valid_symbol(symbol):
    """Check if symbol (string) is valid operator or operant"""

    return is_operant(symbol) or is_operator(symbol) or is_parentheses(symbol)

def is_function(symbol):
    """Check if symbol (string) is valid function"""
    
    return is_negative_function(symbol)

def is_unary_function(symbol):
    """Check if symbol (string) is valid unary function"""

    return is_negative_function(symbol)

def is_negative_function(symbol):
    """Check if symbol (string) is valid negative function"""

    if symbol not in ["neg", "NEG"]:
        return False

    return True and not is_empty(symbol)

def is_operator(symbol):
    """Check if symbol (string) is valid operator"""

    return is_multiplication(symbol) or is_division(symbol) or is_addition(symbol) or is_subtraction(symbol)

def is_binary_operator(symbol):
    """Check if symbol (string) is valid binary operator"""

    return is_multiplication(symbol) or is_division(symbol) or is_addition(symbol) or is_subtraction(symbol)

def is_operant(symbol):
    """Check if symbol (string) is valid operant"""

    return is_integer(symbol) or is_float(symbol)

def is_parentheses(symbol):
    """Check if symbol (string) is a valid parentheses"""

    return is_opening_parentheses(symbol) or is_closing_parentheses(symbol)

def is_opening_parentheses(symbol):
    """Check if symbol (string) is a valid opening parentheses"""

    if len(symbol) != 1:
        return False
    elif symbol not in "(":
        return False

    return True

def is_closing_parentheses(symbol):
    """Check if symbol (string) is a valid closing parentheses"""

    if len(symbol) != 1:
        return False
    elif symbol not in ")":
        return False

    return True

def is_white_space(symbol):
    """check if symbol (string) is a white space"""

    if symbol not in " ":
        return False
    
    return True and not is_empty(symbol)

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

def is_number(symbol):
    """Checks if an symbol (string) is a valid number"""

    return is_integer(symbol) or is_float(symbol)

def is_integer(symbol):
    """Checks if an symbol (string) is a valid integer"""

    for character in symbol:
        if character not in "0123456789":
            return False
    
    return True and not is_empty(symbol)

def is_float(symbol):
    """Checks if an symbol (string) is a valid float"""

    dot_detected = False

    if len(symbol) < 3:
        return False

    if not is_integer(symbol[0]) or not is_integer(symbol[-1]):
        return False

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
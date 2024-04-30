from filter import *

def convert_to_postfix_notation(infix_notation):
    """Convert infix notation to postfix notation with the shunting-yard-algorithmen"""

    postfix_notation = []
    stack = []

    for element in infix_notation:

        if is_operant(element):
            postfix_notation.append(element)
        elif is_operator(element):
            
            while not len(stack) == 0  \
            and is_operator(stack[-1]) \
            and (get_operator_precedence(element) < get_operator_precedence(stack[-1]) or (get_operator_precedence(element) == get_operator_precedence(stack[-1]) and is_left_associative(element))):
                postfix_notation.append(stack.pop())

            stack.append(element)

        #elif is_function(element) and len(stack) == 0:
        #    stack.append(element)
        #elif is_parentheses(element):
        #    while len(stack) > 0 and not is_opening_parentheses(stack[-1]):
        #        postfix_notation.append(stack.pop())
        #    if len(stack) == 0:
        #        raise ValueError("Stack is empty and closing parentheses is missing")
        else:
            raise ValueError(f"Element \"{element}\" is not an operant or function")

    return postfix_notation

def get_operator_precedence(symbol):
    """Returns precedence of operator symbol (string)"""

    if is_multiplication(symbol):
        return 1
    elif is_division(symbol):
        return 1
    elif is_addition(symbol):
        return 0
    elif is_subtraction(symbol):
        return 0
    else:
        raise ValueError(f"Symbol \"{symbol}\" ist not a valid operator")

def is_left_associative(symbol):
    """Check if symbol (string) is left associative"""

    return is_division(symbol) or is_subtraction(symbol)

def filter_for_valid_symbols(notation):
    """Filters all valid symbols and return a list"""

    filterd_notation = []
    temporer_notation = ""
    beginn_of_number = False

    for character in (notation + " "): #Add whitspace to parse last number correct
        temporer_notation += character
        
        if beginn_of_number and (not is_number(temporer_notation) and not temporer_notation[-1] == "."):
            filterd_notation.append(temporer_notation[:-1])
            temporer_notation = temporer_notation[-1]
            beginn_of_number = False         
        elif is_integer(temporer_notation) and not beginn_of_number:
            beginn_of_number = True
        
        if is_operator(temporer_notation) or is_parentheses(temporer_notation):
            filterd_notation.append(temporer_notation)
            temporer_notation = ""
        elif is_white_space(temporer_notation):
            temporer_notation = ""
    
    if len(temporer_notation) != 0:
        raise ValueError(f"Part \"{temporer_notation}\" of notation could not by parsed")
    
    return filterd_notation
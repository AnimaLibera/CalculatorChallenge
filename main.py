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

    #print(is_white_space(" "))
    #print(is_white_space("!"))

    pass

def main():
    print("Challenge Calculator")
    
    terms = input("Inpute Terms: ")
    notation_list = filter_for_valid_symbols(terms)
    print(notation_list)
    print(convert_to_postfix_notation(notation_list))

def convert_to_postfix_notation(infix_notation):
    """Convert infix notation to postfix notation with the shunting-yard-algorithmen"""

        #ENN Token IST-Operator
        #    SOLANGE Stack IST-NICHT-LEER UND
        #            Stack-Spitze IST Operator UND
        #            (Präzedenz von Token IST-KLEINER Präzedenz von Stack-Spitze ODER
        #             Präzedenz von Token IST-GLEICH Präzedenz von Stack-Spitze UND
        #             Token IST-linksassoziativ)
        #        Stack-Spitze ZU Ausgabe.
        #    ENDESOLANGE
        #    Token ZU Stack.
        #ENDEWENN

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
            print("Detected White Space")
            temporer_notation = ""
    
    if len(temporer_notation) != 0:
        raise ValueError(f"Part \"{temporer_notation}\" of notation could not by parsed")
    
    return filterd_notation

def is_valid_symbol(symbol):
    """Check if symbol (string) is valid operator or operant"""

    return is_operant(symbol) or is_operator(symbol)

def is_function(symbol):
    """Check if symbol (string) is valid function"""

    pass
    #return is_operator(symbol) or is_parentheses(symbol)

def is_operator(symbol):
    """Check if symbol (string) is valid operator"""

    return is_parentheses(symbol) or is_multiplication(symbol) or is_division(symbol) or is_addition(symbol) or is_subtraction(symbol)

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

#test()
main()
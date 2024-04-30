#!/usr/bin/python3

def test():
    #print(is_integer("12"))
    #print(is_integer("9"))
    #print(is_integer("AB"))

    #print(is_float("12"))
    #print(is_float("12.0"))
    #print(is_float("12..4"))
    #print(is_float("abc"))

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
        if is_integer(temporer_notation):
            filterd_notation.append(temporer_notation)
            temporer_notation = ""
        elif is_float(temporer_notation):
            filterd_notation.append(temporer_notation)
            temporer_notation = ""

def check_valid_symbol(notation):
    pass

def is_operator(symbol):
    pass

def is_operant(symbol):
    pass

def is_parentheses(symbol):
    pass

def is_integer(symbol):
    """Checks if an symbol (string) is a valid integer"""

    for character in symbol:
        if character not in "0123456789":
            return False
    
    return True

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
    
    return True and dot_detected

def transform_to_prefix_notation(infix_notation):
    pass

test()
#main()
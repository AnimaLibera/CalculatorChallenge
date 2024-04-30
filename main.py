#!/usr/bin/python3

from filter import *
from logic import *

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
    print("Name:\t\tChallenge Calculator")
    print("Author:\t\tGianni-Lauritz Grubert")
    print("License:\tRead, Execute und Copy is permitted")
    
    terms = input("Input Terms:\t")
    notation_list = filter_for_valid_symbols(terms)
    print(notation_list)
    print(convert_to_postfix_notation(notation_list))


#test()
main()
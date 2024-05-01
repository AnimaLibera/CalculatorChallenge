#!/usr/bin/python3

import sys
from filter import *
from logic import *

def main():

    possible_command =sys.argv[1]

    if possible_command == "info":
        print_info()
    elif possible_command == "help":
        print_help()
    else:
        notation_list = filter_for_valid_symbols(possible_command)
        print(notation_list)
        print(convert_to_postfix_notation(notation_list))

def print_info():
    print("Name:\t\tChallenge Calculator")
    print("Author:\t\tGianni-Lauritz Grubert")
    print("E-Mail:\t\tanimalibera@mail.de")
    print("License:\tRead, execute und copy is permitted")

def print_help():
    print("Available Operants:\tInteger i.e. 5 and floating i.e. 12.0 Numbers")
    print("Available Operators:\t* / + -")
    print("Available Parentheses:\t( )")

if __name__ == "__main__":
    main()
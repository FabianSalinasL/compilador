
#Fab Comp V1.0

import sys, subprocess, argparse

from lexer import *
#import tokens

from parser import *
#import rules

#from code_gen import *


class NoMainFunctionException(Exception):
    def __str__(self): return "No \"int main()\" function found."

if __name__=="__main__":


    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description='A small C compiler.')

    # The input .c file name
    parser.add_argument('input', metavar='input_file',
                        type=argparse.FileType('r'), help="the input c file")

    # The output file name
    parser.add_argument('-o', metavar='output_file', dest='output',
                        help="the name for the output files")

    # A flag to create only the asm file
    parser.add_argument('-S', dest='asm_only', action='store_const', const=True,
                        default=False, help="create only the assembly file")
    args = parser.parse_args()


    try:
        program_text = args.input.read()
    except:
        print("Could not read input file.")
    else:
        # If the file opened and was read, then carry on with tokenizing
        #try:
        token_list = tokenize(program_text)
        #print(token_list)
        #except
        #except TokenException as e: # catch any exceptions from the lexer
        #    print(e)
        #    sys.exit(1)

        print("\ncompiling ok!")
    finally:
        args.input.close()

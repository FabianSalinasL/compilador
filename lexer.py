
#Fab lexer V2.0!
import re
import sys
import inspect



class Token:

    def __init__(self, name, text = None, priority = None):
        self.name = name
        self.text = text
        self.priority = priority

valid = ["M","EM","0","1","2","3","4","5","6","7","8","9","a","b","c","d","=","{","}","+","-","*","/","", "L", "F", "C","I"]
t=0

def tokenize(program):

    #print("inside tokenize")
    #print(program)
    parts = re.split("\s+", program)
    if parts[-1] == "":
        parts.remove("")
    print(parts)
    i=0

    for part in parts:
        if part in valid:
            pass
            #print("{}: {} is instance".format(i,part))
            #i+=1
        else:
            print("ERROR: {} not defined!".format(part))
            sys.exit(1)
    gramm(parts)

    #print("next {}".format(next_token(parts)))

def gramm(parts):

    token = next_token(parts)

    if token == "M":
        #next_token(parts)
        #print("next token: {}".format(next_token(parts)))
        print("correct token!")
    else:
        print("ERROR: invalid sintax 1! expected  ---> M")
        sys.exit(1)

    token = next_token(parts)
    if token == "{":
        #next_token(parts)
        print("correct token!")
    else:
        print("ERROR: invalid sintax 2! Expected  ---> {")
        sys.exit(1)

    token = next_token(parts)

    if token == "F":
        pass
    elif token in ("a","b","c","d"): #Variable declaration
        assign(parts)
        #print("***********************")
    elif token == "L":
        pass
    elif token == "I":
        pass
    else:
        print("ERROR: invalid sintax 3! Expected F, L, I or variable")
        sys.exit(1)

    token = prev_token(parts)
    #print("before if with token: {} and t = {}".format(token,t))
    if token == "}":
        #print("inside if")
        try:
            token = next_token(parts)
        except:
            print("in exception!!")
        else:
            print("ERROR: another token after }")



def assign(parts):
    #print("entering assign")
    token = next_token(parts)
    if token == "=":
        #next_token(parts)
        print("correct token!")
    else:
        print("ERROR: invalid sintax 6! Expected  ---> =")
        sys.exit(1)

    token = next_token(parts)
    if token in ("0","1","2","3","4","5","6","7","8","9","a","b","c","d"):
        #next_token(parts)
        print("correct token!")
    else:
        print("ERROR: invalid sintax 6! Expected  ---> variable or int")
        sys.exit(1)

    token = next_token(parts)
    if token in ("a","b","c","d"):
        #print("token value: = {}".format(token))
        #token = next_token(parts)
        #print("token value: = {}".format(token))
        assign(parts)
    elif token in ("0","1","2","3","4","5","6","7","8","9"):
        print("ERROR: invalid sinax ---> starting with a number is not allowed!")
        sys.exit(1)
    elif token == "}":
        print("inside if")
        try:
            token = next_token(parts)
        except:
            print("in exception!!")
        else:
            print("ERROR: invalid sintax ---> another token after }")
            sys.exit(1)
    else:

        print("exiting assign with token value of {} and t= {}".format(token,t))


def next_token(parts):
    global t
    #print("valor t {}".format(t))
    t+=1
    return parts[t-1]

def prev_token(parts):
    global t
    #print("valor t {}".format(t))
    t-=1
    return parts[t-1]

    #for part in parts:
    #    if part == "M":

    #return(parts)




#Fab lexer!
import re
import sys



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
        print("ERROR: invalid sintax 1!  ---> {}".format(token))
        sys.exit(1)

    token = next_token(parts)
    if token == "{":
        #next_token(parts)
        print("correct token!")
    else:
        print("ERROR: invalid sintax 2!  ---> {}".format(token))
        sys.exit(1)

    token = next_token(parts)
    if token == "F":
        pass
    elif token in ("a","b","c","d"):
        token = next_token(parts)
        if token == "=":
            #next_token(parts)
            print("correct token!")
        else:
            print("ERROR: invalid sintax 3!  ---> {}".format(token))
            sys.exit(1)
        token = next_token(parts)
        if token in ("0","1","2","3","4","5","6","7","8","9"):
            #next_token(parts)
            print("correct token!")
        else:
            print("ERROR: invalid sintax 4!  ---> {}".format(token))
            sys.exit(1)




    elif token == "L":
        pass
    elif token == "I":
        pass










def next_token(parts):
    global t
    #print("valor t {}".format(t))
    t+=1
    return parts[t-1]


    #for part in parts:
    #    if part == "M":

    #return(parts)



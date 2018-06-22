
#Fab lexer!
import re



class Token:

    def __init__(self, name, text = None, priority = None):
        self.name = name
        self.text = text
        self.priority = priority
    def match(self, token):
        """Checks if the provided token matches self. Returns true iff both
        tokens have the same name and text, self.text is None"""
        if not isinstance(token, Token): return False
        if self.name != token.name: return False
        if not self.text: return True
        return (self.text == token.text)


def tokenize(program, prims):

    #print("inside tokenize")
    #print(program)
    parts = re.split("\s+", program)


    for prim in prims:
        new_parts = []
        for part in parts:
            if isinstance(part, str):
                split = part.split(prim.text)
                print(split)
                for s in split:
                    if len(s) > 0: new_parts.append(s)
                    new_parts.append(prim)
                new_parts.pop()
            else:
                new_parts.append(part)

        parts = new_parts
        #print(parts)

    def make_token(part):
        # if it's already a token, don't change anything
        if isinstance(part, Token):
            return part
        # if it's a number, store it as an integer
        elif re.fullmatch("[0-9]*", part):
            return Token("integer", part)
        # if it's a valid name, stori it as a name
        elif re.fullmatch("[a-zA-Z_][a-zA-Z0-9_]*", part):
            return Token("name", part)
        else: # we've found something unexpected! complain.
            raise TokenException(part)

    return list(map(make_token, parts))

'Grammar defines the grammar used in our language'
import error

class Grammar():
    # S: Initial  symbol
    # T: Terminal symbols
    # NT: Non-terminal symbols
    # P: Productions
    def __init__(self, S):
        self.S = S

class Terminal():
    def __init__(self, value):
        self.value = value
    
    def check(self, tokens, level, index):
        if(self.value == tokens[index].name):
            return True, index + 1, level, error.SyntaxError(True, tokens[index], level)
        else:
            return False, index, level, error.SyntaxError(False, tokens[index], level)
        return True, index + 1, level, error.SyntaxError(True, tokens[index], level)
        



class NonTerminal():
    def __init__(self, value, productions):
        self.value = value
        self.productions = productions

    def check(self, tokens, index, level):
        print("Index and level are:", index, level)
        productionCounter = 0
        productionAmount = len(self.productions)
        for production in self.productions:
            length = len(production)
            validTokens = 0
            counter = index
            maxRecursionCounter = 0
            maxRecursion = 10
            for token in production:
                # Temp infinite recursion fix
                if(token.value == self.value):
                    maxRecursionCounter += 1
                    if(maxRecursionCounter == maxRecursion):
                        break

                print("CURRENT TOKEN IS:", token.value)
                # If symbol/token is terminal
                if(token.__class__.__name__ == "Terminal"):
                    valid, counter, level, err = token.check(tokens,counter, level + 1)
                    if(valid):
                        print("Found valid terminal symbol", token.value)
                        validTokens += 1
                    else:
                        return False, index, level, err
                else:
                    valid, counter, level, err = token.check(tokens, counter, level + 1)
                    if(valid):
                        validTokens += 1
                counter += 1
                
            if(validTokens == length):
                print("Found a complete valid production")
                return True, counter, level, error.SyntaxError(True, tokens[index], level)
        
        if(productionCounter == productionAmount):
            return False, index, level, error.SyntaxError(True, tokens[index], level)
        return False, index, level, error.SyntaxError(True, tokens[index], level)

                
                

                


class Productions():
    # Products is a list of lists, each list
    # is a possible production of an NT symbol.
    def __init__(self,  product):
        self.products = product

class SyntaxTree():
    def __init__(self, initial):
        self.initial = initial
        self.current = initial
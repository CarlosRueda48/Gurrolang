import spaces, string, automata, token

def isSpace(c):
    if c == ' ':
        return True
    elif c == '\t':
        return True
    elif c == "\n":
        return True
    else:
        return False
    

# Automata that defines our rules for lexical analysis
def createAutomata():
    # Useful lists
    lowercaseList = list(string.ascii_lowercase)
    uppercaseList = list(string.ascii_uppercase)
    numberList = list(string.digits)

    # Create each state with empty transitions
    emptyTransition = [automata.Transition([], None)]
    q0 = automata.State("q0", False, emptyTransition, "INITIAL")
    q1 = automata.State("q1", True, emptyTransition, "IDENTIFIER")
    q2 = automata.State("q2", True, emptyTransition, "INTEGER")
    q3 = automata.State("q3", False, emptyTransition, "REAL_NUMBER_DOT_TRANSITION")
    q4 = automata.State("q4", True, emptyTransition, "REAL_NUMBER")
    q5 = automata.State("q5", True, emptyTransition, "COMMA")
    q6 = automata.State("q6", True, emptyTransition, "SEMICOLON")
    q7 = automata.State("q7", True, emptyTransition, "OPENING_PARENTHESIS")
    q8 = automata.State("q8", True, emptyTransition, "CLOSING_PARENTHESIS")
    q9 = automata.State("q9", True, emptyTransition, "OPENING_CURLY_BRACKETS")
    q10 = automata.State("q10", True, emptyTransition, "CLOSING_CURLY_BRACKETS")
    q11 = automata.State("q11", True, emptyTransition, "ARITHMETIC_OPERATOR")
    q12 = automata.State("q12", True, emptyTransition, "ASSIGNATION")
    q13 = automata.State("q13", True, emptyTransition, "EQUALITY_RELATIONAL_OPERATOR")
    q14 = automata.State("q14", True, emptyTransition, "RELATIONAL_OPERATOR")
    q15 = automata.State("q15", True, emptyTransition, "LOGICAL_OPERATOR")

    # Create all q0 transitions
    q0transitions = []
    q0transq1 = automata.Transition(list(string.ascii_lowercase), q1)
    q0transq2 = automata.Transition(numberList, q2)
    q0transq5 = automata.Transition(list(','), q5)
    q0transq6 = automata.Transition(list(';'), q6)
    q0transq7 = automata.Transition(list('('), q7)
    q0transq8 = automata.Transition(list(')'), q8)
    q0transq9 = automata.Transition(list('{'), q9)
    q0transq10 = automata.Transition(list('}'), q10)
    q0transq11 = automata.Transition(list('+-*/^'), q11)
    q0transq12 = automata.Transition(list('='), q12)
    q0transq14 = automata.Transition(list('><'), q14)
    q0transq15 = automata.Transition(list('&|!'), q15)
    # Add all transitions to a list and assign that list to q0's transitions
    # This part could be optimized by not creating a temp transitions list and instead assigning each transition
    # to the state's transition list when it is created
    q0transitions.extend([q0transq1,q0transq2,q0transq5,q0transq6,q0transq7,q0transq8,q0transq9,q0transq10,q0transq11,q0transq12,q0transq14,q0transq15])
    q0.transitions = q0transitions
    # Create q1 transitions
    q1transitions = []
    q1transq1chars = lowercaseList + uppercaseList + numberList
    q1transq1 = automata.Transition(q1transq1chars, q1)
    q1transitions.extend([(q1transq1)])
    q1.transitions = q1transitions

    #Create q2 transitions
    q2transitions = []
    q2transq2 = automata.Transition(numberList, q2)
    q2transq3 = automata.Transition('.', q3)
    q2transitions.extend([q2transq2, q2transq3])
    q2.transitions = q2transitions

    #Create q3 transitions
    q3transitions = []
    q3transq4 = automata.Transition(numberList, q4)
    q3transitions.extend([q3transq4])
    q3.transitions = q3transitions

    #Create q12 transitions
    q12transitions = []
    q12transq13 = automata.Transition('=', q13)
    q12transitions.extend([q12transq13])
    q12.transitions = q12transitions

    #Create StateMachine
    stateMachine = automata.StateMachine(q0, q0, "")

    return stateMachine


def lexicalAnalysis(path):
    # Open source file from path and format
    rawFile = open(path, 'r').read()
    fileText = rawFile + ' '
    print(fileText)
    length = len(fileText)
    print("File buffer length:", length)
    index = 0
    tokens = []
    lineNum = 1
    charNum = 1
    savedToken = ""
    stateMachine = createAutomata()

    while(index < length):
        #print("Index:", index)
        current = fileText[index]
        #print("Current:", current)
        # If newline is found, increase lineNum by 1, reset charNum
        # and keep iterating by adding 1 to index
        if(current == "\n"):
            lineNum += 1
            charNum = 1
            index += 1
            continue
        # Obtain token's name and value, as well as a boolean that verifies
        # if a token has really ended, if it hasn't, ignore these values.
        tokenName, tokenValue, tokenEnded = stateMachine.changeState(current)
        #print("token value and name:", tokenValue, tokenName)
        if(tokenName == "error"):
            newToken = token.ErrorToken(tokenName, tokenValue, lineNum, charNum, "Unrecognized character")
            tokens.append(newToken)
            #print(newToken)
        else:
            # Sometimes a token from the INITIAL state will be added at the end of the file,
            # still must be fixed properly, however this (not tokenName == "INITIAL") is a temporary fix
            # that makes the lexical analyzer work as intended
            if(tokenEnded and (not tokenName == "INITIAL")):
                #Palabras reservadas
                if(tokenName == "IDENTIFIER"):
                    if(tokenValue == "principal"):
                        newToken = token.Token("KEYWORD_PRINCIPAL", tokenValue, lineNum, charNum)
                        tokens.append(newToken)
                        print(newToken)
                    elif(tokenValue == "regresa"):
                        newToken = token.Token("KEYWORD_REGRESA", tokenValue, lineNum, charNum)
                        tokens.append(newToken)
                        print(newToken)
                    elif(tokenValue == "si"):
                        newToken = token.Token("KEYWORD_SI", tokenValue, lineNum, charNum)
                        tokens.append(newToken)
                        print(newToken)
                    elif(tokenValue == "mientras"):
                        newToken = token.Token("KEYWORD_MIENTRAS", tokenValue, lineNum, charNum)
                        tokens.append(newToken)
                        print(newToken)
                    elif(tokenValue == "verdadero"):
                        newToken = token.Token("KEYWORD_VERDADERO", tokenValue, lineNum, charNum)
                        tokens.append(newToken)
                        print(newToken)
                    elif(tokenValue == "falso"):
                        newToken = token.Token("KEYWORD_FALSO", tokenValue, lineNum, charNum)
                        tokens.append(newToken)
                        print(newToken)
                    else:
                        newToken = token.Token(tokenName, tokenValue, lineNum, charNum)
                        tokens.append(newToken)
                        print(newToken)
                    
                #print("Adding new valid token!")
                # If the read character was not a whitespace or similar, it must still be processed,
                # by the automata at the 
                if(not isSpace(fileText[index])):
                    #print("Decreasing index due to non-whitespace char read")
                    index -= 1
                tokenEnded = False
                
        charNum += 1
        index += 1
    
    return tokens

lex = lexicalAnalysis("source.txt")

tokenFile = open("tokens.txt","w")
# Since the comma is an accepted token in our language, token values are separated by whitespaces
# Each line of tokens.txt consists of tokenType, tokenValue, lineNumber, charNumber
for t in lex:
    tokenFile.write(t.__repr__() + "\n")
    print(t)
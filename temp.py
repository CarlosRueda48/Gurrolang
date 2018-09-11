

       
def isNumber(c):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    if c in numbers:
        print("Found number!")
        return True
    else:
        return False

# Since python islowercase and isuppercase methods return True for white spaces, I decided to instead create my own to prevent any errors
def isLowercase(c):
    # List of lowercase letters from a-z, not including á, é, í, ó, ú or ñ
    lowercase = string.ascii_lowercase
    if c in lowercase:
        return True
    else:
        return False

def isUppercase(c):
    # List of uppercase letters from a-z, not including Á, É, Í, Ó, Ú or Ñ
    uppercase = string.ascii_uppercase
    if c in uppercase:
        return True
    else:
        return False


def tokenize(s):
    tokens = []
    memory = ""
    charNum = 1
    lineNum = 0
    currentlyNumber = False
    dotAlreadyInNumber = False
    currentlyId = False
    currentlyEquals = False
    currentlyError = False
    for c in s:
        print(c,c.__class__)
        if(c == "\n"):
            # Add 1 to line number whenever \n is found, reset charNum to 1 when it happens
            lineNum += 1
            charNum = 1
        # All number validations
        elif(isNumber(c) and memory == ""):
            memory += c
            currentlyNumber = True
        elif(isNumber(c) and currentlyNumber == True):
            memory += c
        elif(c == '.' and currentlyNumber == True):
            if(dotAlreadyInNumber):
                memory += c
                currentlyError = True
            else:
                memory += c
            dotAlreadyInNumber = True
            
        elif(isNumber(c) and memory[-1] == '.'):
            memory += c
        elif(currentlyNumber and (not isNumber(c)) and (not (c == '.'))):
            memory += c
            currentlyError = True
        elif((c == ' ') and (memory[-1] == '.')):
            tokens.append(ErrorToken("Error","Invalid number error", lineNum, charNum))
            memory = ""
            currentlyNumber = False
            currentlyError = False
        elif(c == ' ' and currentlyNumber and currentlyError):
            tokens.append(ErrorToken("Error","Invalid number error", lineNum, charNum))
            memory = ""
            currentlyNumber = False
            currentlyError = False
        elif(c == ' ' and isNumber(memory[-1])):
            #If number contains a dot, it is labeled as a real number, otherwise as an integer
            if(dotAlreadyInNumber):
                tokens.append(Token("REAL_NUMBER", memory, lineNum, charNum))
                memory = ""
                currentlyNumber = False
                dotAlreadyInNumber = False
            else:
                tokens.append(Token("INTEGER", memory, lineNum, charNum))
                memory = ""
                currentlyNumber = False
        # Identifier validations
        

        # Add 1 to charNum each time a character is read
        charNum += 1

    return tokens

tokenTest = tokenize("012398214 ")
print("Token no:", len(tokenTest))
print(tokenTest)


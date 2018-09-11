import time


def isSpace(c):
    if c == ' ':
        return True
    elif c == '\t':
        return True
    else:
        return False
    
    
def formatSpaces(fileText):
    print("text length:",len(fileText))
    print(fileText)
    tokensStarted = False
    currentlySpace = False
    text = ""
    for c in fileText:
        if(isSpace(c) and (not currentlySpace)):
            text += " "
            currentlySpace = True
        elif((not isSpace(c)) and tokensStarted == False):
            tokensStarted = True
            text += c
            currentlySpace = False
        elif(tokensStarted and (not isSpace(c))):
            text += c
            currentlySpace = False

    print("\nFormatted file:")
    print(text)
    # Final space is added to prevent errors
    return text + ' '

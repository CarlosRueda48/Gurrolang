class Token:
    'Token defines the structure a token will have'

    def __init__(self, name, value, lineNum, charNum):
        self.name = name
        self.value = value
        self.lineNum = lineNum
        self.charNum = charNum

    def __str__(self):
        return('Token("Name: %s", Value:"%s", lineNum:"%d", charNum:"%d")' % (self.name, self.value, self.lineNum, self.charNum))
    def __repr__(self):
        return("%s"' '"%s"' '"%d"' '"%d" % (self.name, self.value, self.lineNum, self.charNum))

class ErrorToken:
    'ErrorToken used for whenever an error is found'
    def __init__(self, name, value, lineNum, charNum, errorDesc):
        self.name = name
        self.value = value
        self.lineNum = lineNum
        self.charNum = charNum
        self.errorDesc = errorDesc
    
    def __str__(self):
        return('Token("Name: %s", Value:"%s", lineNum:"%d", charNum:"%d", error: "%s")' % (self.name, self.value, self.lineNum, self.charNum, self.errorDesc))
    def __repr__(self):
        return("%s"' '"%s"' '"%d"' '"%d" % (self.name, self.value, self.lineNum, self.charNum))

class DescribedToken(Token):
    def __init__(self, name, value, lineNum, charNum, idType, dataType):
        super().__init__(self, name, value, lineNum, charNum)
        self.idType = idType
        self.dataType = dataType

    def __str__(self):
        return('Token("Name: %s", Value:"%s", lineNum:"%d", charNum:"%d")' % (self.name, self.value, self.lineNum, self.charNum))
    def __repr__(self):
        return("%s"' '"%s"' '"%d"' '"%d"' '"%d"' '"%d" % (self.name, self.value, self.lineNum, self.charNum, self.idType, self.dataType))

class SyntaxError():
    def __init__(self, empty, token, level):
        self.empty = empty
        self.token = token
        self.level = level
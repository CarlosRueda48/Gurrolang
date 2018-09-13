import token

class State:
    def __init__(self, name, isFinal, transitions, desc):
        self.name = name
        self.isFinal = isFinal
        self.transitions = transitions
        self.desc = desc

class Transition:
    def __init__(self, charList, destinationState):
        self.charList = charList
        self.destinationState = destinationState

class StateMachine:
    def __init__(self, initialState, currentState, memory):
        self.initialState = initialState
        self.currentState = currentState
        self.memory = memory

    def changeState(self, c):
        current = c
        # If whitespace or similar encountered, end token
        if(current == ' ' or c == "\n" or c == "\t"):
            tokenName = self.currentState.desc
            tokenValue = self.memory
            #print("Machine Reset due to whitespace or similar")
            self.resetMachine()
            return tokenName, tokenValue, True
        # Counter for each state's transitions
        counter = 1
        transitionsLength = len(self.currentState.transitions)
        for transition in self.currentState.transitions:
            # If valid transition is found, save char in memory and move to next state
            if(current in transition.charList):
                self.currentState = transition.destinationState
                self.memory += current
                #print("Current state is:", self.currentState.name)
                continue
            else:
                # If no valid transition is found at the end, check if state is final,
                # if it is, then return state name as the token name and saved memory as token value
                if(counter == transitionsLength):
                    if(self.currentState.isFinal == True):
                        tokenValue = self.memory
                        tokenName = self.currentState.desc
                        #print("Machine Reset due to final valid state")
                        self.resetMachine()
                        self.savedChar = current
                        return tokenName, tokenValue, True
                    # If state is not final and no transition is found, return an error token
                    else:
                        tokenValue = current
                        #print("Machine Reset due to error"),
                        self.resetMachine()
                        return "error", tokenValue, True
                    return self.currentState.desc, self.memory, True
            counter += 1
        return self.currentState.desc, self.memory, False

    def resetMachine(self):
        self.currentState = self.initialState
        self.memory = ""
        

 

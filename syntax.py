import grammar, token, lexical

def createGrammar():
    #Generic Tokens / Terminals

    # Terminal Symbols, they contain as value the name of its respective token,
    # these token names were already defined in the grammar and assigned by the
    # lexical analyzer.

    # Keywords and identifiers
    principalTerminal = grammar.Terminal("KEYWORD_PRINCIPAL")
    siKeywordTerminal = grammar.Terminal("KEYWORD_SI")
    regresaKeywordTerminal = grammar.Terminal("KEYWORD_REGRESA")
    mientrasKeywordTerminal = grammar.Terminal("KEYWORD_MIENTRAS")
    verdaderoKeywordTerminal = grammar.Terminal("KEYWORD_VERDADERO")
    falsoKeywordTerminal = grammar.Terminal("KEYWORD_FALSO")
    enteroKeywordTerminal = grammar.Terminal("KEYWORD_ENTERO")
    realKeywordTerminal = grammar.Terminal("KEYWORD_REAL")
    logicoKeywordTerminal = grammar.Terminal("KEYWORD_LOGICO")
    identifierTerminal = grammar.Terminal("IDENTIFIER")

    # Terminal chars
    integerTerminal = grammar.Terminal("INTEGER")
    realNumberTerminal = grammar.Terminal("REAL_NUMBER")
    commaTerminal = grammar.Terminal("COMMA")
    semicolonTerminal = grammar.Terminal("SEMICOLON")
    leftParenthesisTerminal = grammar.Terminal("OPENING_PARENTHESIS")
    rightParenthesisTerminal = grammar.Terminal("CLOSING_PARENTHESIS")
    leftCurlyBracketsTerminal = grammar.Terminal("OPENING_CURLY_BRACKETS")
    rightCurlyBracketsTerminal = grammar.Terminal("CLOSING_CURLY_BRACKETS")
    arithmeticOperatorTerminal = grammar.Terminal("ARITHMETIC_OPERATOR")
    assignationOperatorTerminal = grammar.Terminal("ASSIGNATION")
    relationalOperatorTerminal = grammar.Terminal("RELATIONAL_OPERATOR")
    logicalOperatorTerminal = grammar.Terminal("LOGICAL_OPERATOR")
    logicalNegationTerminal = grammar.Terminal("LOGICAL_NEGATION")

    #Initial Symbol
    inicio = grammar.NonTerminal("inicio", None)
    # Non Terminal Symbols
    principal = grammar.NonTerminal("PRINCIPAL", None)
    bloque_funciones = grammar.NonTerminal("bloque_funciones", None)
    sentencias = grammar.NonTerminal("sentencias", None)
    sentencia = grammar.NonTerminal("sentencia", None)
    funcion = grammar.NonTerminal("funcion", None)
    tipo_dato = grammar.NonTerminal("tipo_dato", None)
    argumentos = grammar.NonTerminal("argumentos", None)
    argumento = grammar.NonTerminal("argumento", None)
    bloque_codigo = grammar.NonTerminal("bloque_codigo", None)
    declaraciones = grammar.NonTerminal("declaraciones", None)
    si = grammar.NonTerminal("si", None)
    mientras = grammar.NonTerminal("mientras", None)
    asignacion = grammar.NonTerminal("asignacion", None)
    expresion = grammar.NonTerminal("expresion", None)
    aritmetica = grammar.NonTerminal("aritmetica", None)
    operador_aritmetico = grammar.NonTerminal("operador_aritmetico", None)
    valor_aritmetico = grammar.NonTerminal("valor_aritmetico", None)
    llamada_funcion = grammar.NonTerminal("llamada_funcion", None)
    argumentos_funcion = grammar.NonTerminal("argumentos_funcion", None)
    logica = grammar.NonTerminal("logica", None)
    operador_logico = grammar.NonTerminal("operador_logico", None)
    valor_logico = grammar.NonTerminal("valor_logico", None)
    relacional = grammar.NonTerminal("relacional", None)
    operador_relacional = grammar.NonTerminal("operador_relacional", None)
    
    # Productions
    inicio.productions = [[bloque_funciones, principal], [principal]]
    principal.productions = [[principalTerminal, leftParenthesisTerminal, rightParenthesisTerminal, declaraciones, sentencias]]
    bloque_funciones.productions = [[funcion, bloque_funciones]]
    sentencias.productions = [[sentencia], [sentencia, sentencias]]
    sentencia.productions = [[si], [mientras], [asignacion]]
    funcion.productions = [
        # With codeblock
        [tipo_dato, identifierTerminal, leftParenthesisTerminal, argumentos_funcion, rightParenthesisTerminal, leftCurlyBracketsTerminal, bloque_codigo, regresaKeywordTerminal, identifierTerminal, semicolonTerminal, rightCurlyBracketsTerminal], 
        # No codeblock, only return statement
        [tipo_dato, identifierTerminal, leftParenthesisTerminal, argumentos_funcion, rightParenthesisTerminal, leftCurlyBracketsTerminal, regresaKeywordTerminal, identifierTerminal, semicolonTerminal, rightCurlyBracketsTerminal]
    ]
    tipo_dato.productions = [[enteroKeywordTerminal], [realKeywordTerminal], [logicoKeywordTerminal]]
    argumentos.productions = [[argumento], [argumento, commaTerminal, argumentos]]
    argumento.productions = [[tipo_dato, identifierTerminal]]
    bloque_codigo.productions = [[declaraciones, sentencias]]
    declaraciones.productions = [[tipo_dato, identifierTerminal, semicolonTerminal], [tipo_dato, identifierTerminal, semicolonTerminal, declaraciones]]
    si.productions = [[siKeywordTerminal, leftParenthesisTerminal, identifierTerminal, rightParenthesisTerminal, leftCurlyBracketsTerminal, sentencias, rightCurlyBracketsTerminal]]
    mientras.productions = [[mientrasKeywordTerminal, leftParenthesisTerminal, identifierTerminal, rightParenthesisTerminal, leftCurlyBracketsTerminal, sentencias, rightCurlyBracketsTerminal]]
    asignacion.productions = [[identifierTerminal, assignationOperatorTerminal, expresion, semicolonTerminal]]
    expresion.productions = [[aritmetica], [logica], [relacional], [logicalNegationTerminal, identifierTerminal]]
    aritmetica.productions = [[leftParenthesisTerminal, aritmetica, rightParenthesisTerminal], [valor_aritmetico], [aritmetica, operador_aritmetico, aritmetica] ]
    operador_aritmetico.productions = [[arithmeticOperatorTerminal]]
    valor_aritmetico.productions = [[identifierTerminal], [enteroKeywordTerminal], [realNumberTerminal], [llamada_funcion]]
    llamada_funcion.productions = [[identifierTerminal, leftParenthesisTerminal, argumentos_funcion, rightParenthesisTerminal]]
    argumentos_funcion.productions = [[identifierTerminal], [identifierTerminal, commaTerminal, argumentos_funcion]]
    logica.productions = [[leftParenthesisTerminal, logica, rightParenthesisTerminal], [valor_logico], [logica, operador_logico, logica]]
    operador_logico.productions = [[logicalOperatorTerminal]]
    valor_logico.productions = [[identifierTerminal], [verdaderoKeywordTerminal], [falsoKeywordTerminal], [llamada_funcion]]
    relacional.productions = [[valor_aritmetico, operador_relacional, valor_aritmetico]]
    operador_relacional.productions = [relationalOperatorTerminal]

    # Grammar
    tree = grammar.SyntaxTree(inicio)

    return tree



def syntax(tokens, symbolTable):
    length = len(tokens)
    index = 0
    errorLevel = 0
    describedSymbolTable = []
    currentError = None
    tree = createGrammar()
    class SyntaxError():
        def __init__(self, token, level):
            self.token = token
            self.level = level


def syntaxAnalysis(tokens, symbolTable):
    length = len(tokens)
    errorLevel = 0
    index = 0
    describedSymbolTable = []
    tree = createGrammar()
    ("Tokens size:", length)
    valid, index, level, err = tree.current.check(tokens, index, errorLevel)
    print("Data",valid, index, level, err)
    if(valid):
        for i in range in (0,len(tokens)):
            if token[i].name == "IDENTIFIER":
                # If a parenthesis to the right exists, then we know it is a function, otherwise a variable
                    if(tokens[i+1].name == "OPENING_PARENTHESIS"):
                        describedSymbolTable.append(DescribedToken(tokens[i].name, tokens[i].validProduction, 
                            tokens[i].lineNum, tokens[i].charNum, "function", tokens[i-1].value))
                    else:
                        describedSymbolTable.append(DescribedToken(tokens[i].name, tokens[i].validProduction, 
                            tokens[i].lineNum, tokens[i].charNum, "variable", tokens[i].value))
        print(describedSymbolTable)
        return valid, describedSymbolTable
    else:
        return valid, describedSymbolTable

tokens = []
symbolTable = []
tokens, symbolTable = lexical.lexicalAnalysis("source.txt")
valid = syntaxAnalysis(tokens, symbolTable)
print(valid)


            






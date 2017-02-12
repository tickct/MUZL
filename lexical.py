"""MUZL PROJECT PART 2
MORGAN PETERS AND SEAN GRAY
2/9/2017
Yo i've been looking at this py doc more and i think this should work...

http://www.slideshare.net/dabeaz/writing-parsers-and-compilers-with-ply
"""

import ply.lex as lex

# reserved words...
reserved = {
    'if': 'IF',
    'rule': 'RULE',
    'start': 'START',
    'match': 'MATCH',
    #the _T notation tells us it is a type decloration variable not the value type
    'int': 'INT_T',
    'float': 'FLOAT_T',
    'string': 'STRING_T',
    'char': 'CHAR_T',
    'bool': 'BOOL_T'
}

# Token list
tokens_list = [
    'LOGIC',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POW',
    'LTHAN',    # LESSTHAN <
    'LETHAN',   # LESSTHANOREQUALTO <=
    'GTHAN',    # GREATERTHAN >
    'GETHAN',   # GREATERTHANOREQUALTO >=
    'ETO',      # EQUALTO ==
    'TYPE','EQUALS',
    'VAR', 'ARROW',
    'MATCHBREAK',
    'EOL',      # END OF LINE
    'COMMA', 'LBRACKET', 'RBRACKET','LPAREN','RPAREN', 'COLON',
    'ID' #to match all words including reserved
]
#seporated for easier reading, list of types with variable values
data_types_list = [
    'INT',
    'FLOAT',
    'CHAR',
    'STRING',
    'BOOL'
]

#need to put all lists before reserved for some reason
tokens = tokens_list + data_types_list + list(reserved.values())
    # regular expressions
t_MATCHBREAK = r'\|'
t_COMMA = r'\,'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LETHAN = r'\<='
t_LTHAN = r'\<'
t_GETHAN = r'\>='
t_GTHAN = r'\>'
t_PLUS = r'\+'
t_ARROW = r'->'     # longer expressions must go first
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POW = r'\^'
t_ETO = r'=='
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'

    # action code of regular expressions

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'-?\d+\.d*(e-?\d+)?'
    t.value = float(t.value)
    return t

def t_CHAR(t):
    r'\'\w\''
    t.value = t.value[1:-1] #strips away the quotes
    return t

def t_STRING(t):
    r'\"\w+\w\"'
    t.value = t.value[1:-1]  #strips away the quotes
    return t

def t_COMMENT(t):
    r'\[\#].'
    pass

    # end of line; syntax the same as the example
def t_EOL(t):
    r'!+'
    t.lexer.lineno += len(t.value)
    
def t_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
    # A string containing ignored characters (spaces and tabs)
t_ignore = ' \t \n'

# literals? like for [], ! ect.. do we need these?

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
    # precedence (i think this is the second part of the project?)

    # build it
def getLex():
    return lex.lex()
    
    # Main
if __name__ == '__main__':
# trials
    lex.input("x = 3 * 4 + 4 * 6")
    while True:
        tok = lex.token()
        print (tok)
        if not tok:
            break

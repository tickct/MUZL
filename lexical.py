"""MUZL PROJECT PART 2
MORGAN PETERS AND SEAN GRAY
2/9/2017
Yo i've been looking at this py doc more and i think this should work...
"""

import ply.lex as lex

# Token list
tokens = (
    'RULE', 'NUMBER', 'LOGIC',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'POW',
    'LTHAN',    # LESSTHAN <
    'LETHAN',   # LESSTHANOREQUALTO <=
    'GTHAN',    # GREATERTHAN >
    'GETHAN',   # GREATERTHANOREQUALTO >=
    'ETO',      # EQUALTO ==
    'TYPE', 'START', 'EQUALS',
    'VAR', 'ARROW', 'MATCH',
    'MATCHBREAK',
    'EOL',      # END OF LINE
    'COMMA', 'LBRACKET', 'RBRACKET', 'IF'
)

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
t_ARROW = r'->' # longer expressions must go first
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POW = r'\^'
t_ETO = r'=='
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'


# action code of regular expressions

def t_FLOAT(t):
    r'-?\d+\.d*(e-?\d+)?'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_comments(t):
    r'[#][^\n]*'
    pass


# end of line; syntax the same as the example
def t_EOL(t):
    r'!+'
    t.lexer.lineno += len(t.value)


# reserved words...b
# precedence

# build it

# Main
if __name__ == '__main__':
    lex.lex()
    # trials
    # lex.input("x = 3 * 4 + 4 * 6")
    # while True:
    #     tok = lex.token()
    #     if not tok:
    #         break
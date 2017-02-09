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
    'COMMA', 'BRACKET', 'IF'
)

# regular expressions
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
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'\d+'
    t.value = float(t.value)


# end of line; syntax the same as the example
def t_EOL(t):
    r'!+'
    t.lexer.lineno += len(t.value)

# Main
if __name__ == '__main__':
     lex.runmain()
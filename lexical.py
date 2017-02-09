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
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

# TYPES


# Main
if __name__ == '__main__':
     lex.runmain()
import ply.lex as lex

# Token list
tokens = (
    'RULE',
    'NUMBER',
    'LOGIC',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POW',
    'LTHAN',    # LESSTHAN <
    'LETHAN',   # LESSTHANOREQUALTO <=
    'GTHAN',    # GREATERTHAN >
    'GETHAN',   # GREATERTHANOREQUALTO >=
    'ETO',      # EQUALTO ==
    'TYPE',
    'START',
    'EQUALS',
    'VAR',
    'ARROW',
    'MATCH',
    'MATCHBREAK',
    'EOL',      # END OF LINE
    'COMMA',
    'BRACKET',
    'IF'
)

# TYPES
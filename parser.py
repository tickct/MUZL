"""
Parser of MUZL
"""

import ply.yacc as yacc
# token map import
from lexical import tokens

# starting symbol
start = 'fact'

# lowest to highest
precedence = (('nonassoc', 'LTHAN', 'GTHAN', 'ETO', 'GETHAN', 'LETHAN'),
              ('left', 'PLUS', 'MINUS'),
              ('left', 'TIMES', 'DIVIDE'),
              ('left', 'POW'))


def p_expression_pm(p):
    ''' expression : expression PLUS term
                    | expression MINUS term
                    | expression DIVIDE term '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]


def p_term_md(p):
    '''term : term TIMES factor
            | term DIVIDE factor '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_term_factor(p):
    'term: factor'
    p[0] = p[1]


def p_term_float(p):
    'term: FLOAT'
    p[0] = p[1]


if __name__ == "__main__":
    parser = yacc.yacc()

    while True:
        try:
            s = input('MUZL >')
        except EOFError:
            break
        if not s:
            continue

        print(parser.parse(s))

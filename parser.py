"""
Parser of MUZL

use ast -> pythons abstract syntax tree function

Hi Sean
"""

import ply.yacc as yacc
# token map import
from lexical import tokens


def p_term_mul(p):
    '''term : term TIMES factor'''
    p[0] = p[1] + p[3]


def p_error(p):
    print("Syntax Error at", p.value)


precedence = (
    ('nonassoc', 'LTHAN', 'GTHAN', 'ETO', 'GETHAN', 'LETHAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW')
    )


def make_parser():
    yaccparser = yacc.yacc()
    return yaccparser


if __name__ == "__main__":
    yacc = make_parser()

    print(yacc.parse("12 * 12"))



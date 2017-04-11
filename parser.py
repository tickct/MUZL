"""
Parser of MUZL

use ast -> pythons abstract syntax tree function

Hi Sean
"""

import ply.yacc as yacc
# token map import
from lexical import tokens


def p_error(p):
    print("Syntax Error at", p.value)

precedence = (
    ('nonassoc', 'LTHAN', 'GTHAN', 'ETO', 'GETHAN', 'LETHAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW')
    )


def make_parser():
    parser = yacc.yacc()
    return parser


if __name__ == "__main__":
    parser = make_parser()
    print(parser.parse("123"))



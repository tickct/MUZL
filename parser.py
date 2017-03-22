"""
Parser of MUZL

use ast -> pythons abstract syntax tree function

"""

import ply.yacc as yacc
import ast
# token map import
from lexical import tokens

# starting symbol
# start = 'fact'


# name rule ( arg1 type; arg2 type ) -> type = (X + Y)!
def p_funcrule(p):
    'funcrule: NAME RULE (parameters) ARROW TYPE EQUALS'
    p[0] = ast.FunctionDef(None, p[1], tuple(p[3]), (), 0, None, p[5])


# parameters ( [vararglist] )
def p_parameters(p):
    '''parameters : LPAREN RPAREN
                | LPAREN vararglist RPAREN'''
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]


# vararglist:
def p_vararglist(p):
    '''vararglist: vararglist COMMA NAME TYPE
                | NAME TYPE'''
    pass


binary_ops = {
    "+": ast.Add,
    "-": ast.Sub,
    "*": ast.Mult,
    "/": ast.Div,
}


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
    make_parser()


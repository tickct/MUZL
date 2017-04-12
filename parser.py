"""
Parser of MUZL

use ast -> pythons abstract syntax tree function

Hi Sean
"""

import ply.yacc as yacc
# token map import
from lexical import tokens


def p_binary_operators(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | val'''
def p_type_change(p):
    '''val : VAR DOT type
           | VAR
           | value DOT type
           | value '''
    
def p_value(p):
    '''value : INT
             | FLOAT
             | CHAR
             | STRING
             | BOOL
             | HEX '''
    
def p_type(p):
    '''type : INT_T
            | FLOAT_T
            | CHAR_T
            | STRING_T
            | BOOL_T
            | HEX_T '''
    
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



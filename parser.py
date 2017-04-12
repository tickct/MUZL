"""
Morgan Peters and Sean Gray
CS 440: Languages and Translators
Spring 2017
Parser of MUZL
"""

import ply.yacc as yacc
# token map import
from lexical import tokens


"""def p_binary_operators(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | val'''
    print(x for x in p)
    if (len(p) == 4) :
        if p[2] == '+':
            print(p)
            p[0] = p[1] + p[3]
        if p[2] == '-':
            p[0] = p[1] + p[2]
        if p[2] == '*':
            p[0] = p[1] + p[2]
        if p[2] == '/':
            p[0] = p[1] + p[2]
        if p[1] == '(':
            p[0] = p[2]
"""

def p_expression_comparisons(p):
    '''expression : expression ETO val
                  | expression LETHAN val
                  | expression GETHAN val
                  | expression GTHAN val
                  | expression LTHAN val '''
    raise NotImplementedError

def p_expression_plus(p):
    'expression : expression PLUS val'
    p[0] = p[1] + Number(p[3])

def p_expression_times(p):
    'expression : expression TIMES val'
    p[0] = p[1] * Number(p[3])

def p_expression_divide(p):
    'expression : expression DIVIDE val'
    p[0] = p[1] / Number(p[3])
    # raise NotImplementedError

def p_expression_minus(p):
    'expression : expression MINUS val'
    p[0] = p[1] - Number(p[3])
    # raise NotImplementedError

def p_expression_val(p):
    'expression : val'
    p[0] = p[1]

# No string type change added
# does not recognise Char/doubles to convert
def p_type_change(p):
    '''val : VAR type
           | VAR
           | value type
           | value '''
    print(p[1],'.', p[2])
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == 'hex':
        p[0] = hex(int(p[1]))
    elif p[2] == 'int':
        p[0] = int(p[1])
    elif p[2] == 'char':
        p[0] = chr(int(p[1]))
    elif p[2] == 'bool':
        p[0] = bool(p[1])


def p_value(p):
    '''value : INT
             | FLOAT
             | CHAR
             | STRING
             | BOOL
             | HEX '''
    p[0] = p[1]


def p_type(p):
    '''type : INT_T
            | FLOAT_T
            | CHAR_T
            | STRING_T
            | BOOL_T
            | HEX_T '''
    p[0] = p[1]


def p_error(p):
    print("Syntax Error at", p.value)
   

precedence = (
    ('nonassoc', 'LTHAN', 'GTHAN', 'ETO', 'GETHAN', 'LETHAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW')
    )


parser = yacc.yacc()

while True:
    try:
        s = input('!-')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)


def Number(a):
    if isinstance(a, int):
        return float(a)
    if isinstance(a, float):
        return a
    if isinstance(a, hex):
        return float(int(a))
    if isinstance(a, bool):
        if a:
            return 1
        else:
            return 0

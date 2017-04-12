"""
Morgan Peters and Sean Gray
CS 440: Languages and Translators
Spring 2017
Parser of MUZL
"""

import ply.yacc as yacc
# token map import
from lexical import tokens

def Number(a):
    if isinstance(a, int):
        return float(a)
    if isinstance(a, float):
        return a
    if isinstance(a, bool):
        if a:
            return 1
        else:
            return 0
    if isinstance(a,str) and len(a) == 1:
        return ord(a)
    
def TypeConvert(x,typ):
    if typ == 'hex':
        y = hex(int(x))
    elif typ == 'int':
        #char isnt a type in python
        if isinstance(x,str) and len(x) == 1:
            y = ord(x)
        else:
            y = int(x)
    elif typ == 'char':
        if isinstance(x,str) and len(x) == 1:
            y=x
        else:
            y = chr(int(x))
    elif typ == 'bool':
        y = bool(x)
    elif typ == 'float':
        #for char
        if isinstance(x,str) and len(x) == 1:
            y = float(ord(x))
        else:
            y = float(x)
    return y

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
    p[0] = Number(p[1]) + Number(p[3])

def p_expression_mult(p):
    'expression : expression TIMES val'
    p[0] = Number(p[1]) * Number(p[3])

def p_expression_divide(p):
    'expression : expression DIVIDE val'
    p[0] = Number(p[1]) / Number(p[3])

def p_expression_subtract(p):
    '''expression : expression MINUS val
                  | MINUS expression'''
    if len(p) == 3:
        p[0]=-p[2]
    else:    
        p[0] = Number(p[1]) - Number(p[3])

def p_expression_pow(p):
    'expression : expression POW val'
    p[0] = p[1] ** Number(p[3])

def p_expression_parens(p):
    '''expression : LPAREN expression RPAREN
                  | LPAREN expression RPAREN DOT type'''
    if len(p) == 6:
        p[0] = TypeConvert(p[2],p[5])
    else:
        p[0] = p[2]
        
def p_expression_val(p):
    '''expression : val
                  | val DOT type'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = TypeConvert(p[1],p[3])
   
# No string type change added
# does not recognise Char/doubles to convert

    

def p_value(p):
    '''val : INT
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

def getParser():
    return parser
if __name__ == '__main__':
    while True:
        try:
            s = input('!-')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)




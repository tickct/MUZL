"""
Morgan Peters and Sean Gray
CS 440: Languages and Translators
Spring 2017
Parser of MUZL
"""

import ply.yacc as yacc
# token map import
from lexical import tokens
import MuzlRule

rules={}

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
    if isinstance(a,str):
        if len(a) == 1:
            return ord(a)
        elif a[1] == 'x':
            return int(a,0)


def TypeConvert(x,typ):
    if typ == 'hex':
        if isinstance(x,str):
            if len(x) == 1:
                y = hex(ord(x))
            else:
                y = hex(int(x,0))
        else:
            y = hex(int(x))
    elif typ == 'int':
        #char isnt a type in python
        if isinstance(x,str):
            if len(x) == 1:
                y = ord(x)
            else:
                y=int(x,0)
        else:
            y = int(round(x))
    elif typ == 'char':
        if isinstance(x,str):
            if len(x) == 1:
                y=x
            else:
                y=chr(int(x,0))
        else:
            y = chr(int(x))
    elif typ == 'bool':
        y = bool(x)
    elif typ == 'float':
        #for char
        if isinstance(x,str):
            if len(x) == 1:
                y = float(ord(x))
            else:
                y= float(int(x,0))
        else:
            y = float(x)
    return y

# this needs to stay above all the start options, it defines what items can stand alone in a parse
def p_start(p):
    '''start : function
             | expression'''
    p[0] = p[1]
def p_rule(p):
    '''function : rname RULE LPAREN assign RPAREN ARROW type EQUALS expression EOL'''
    rules[p[1]]=MuzlRule.rule(p[1],p[4],p[7],p[9])
    p[0]= p[1] + ' created.'
def p_rname(p):
    '''rname : ID'''
    p[0]=p[1]
def p_assign_variables(p):
    '''assign : assign COLON ID type
              | ID type
              | empty '''
    if len(p) == 3:
        p[0]={p[1]:p[2]}
    elif len(p) == 5:
        p[0]={**p[1],**{p[3],p[4]}}

precedence = (
    ('nonassoc', 'LTHAN', 'GTHAN', 'ETO', 'GETHAN', 'LETHAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW')
    )

def p_expression_comparisons(p):
    '''expression : expression ETO val
                  | expression LETHAN val
                  | expression GETHAN val
                  | expression GTHAN val
                  | expression LTHAN val '''
    if p[2] == '==':
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == '<=':
        if p[1] <= p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == '>=':
        if p[1] >= p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == '>':
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == '<':
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False

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

def p_val_rule(p):
    '''val : ID LPAREN args RPAREN'''
    if p[1] in rules.keys():
        #check that arguments given match arguments expected
        if len(rules[p[1]].args) == len(p[3]):
            p[0]=TypeConvert(rules[p[1]].expression,rules[p[1]].ret)
        else:
            print('Error: Argument Mismatch, expeted',len(rules[p[1]].args),' found ',len(p[3]))
    else:
        print('Error: Rule not found:',p[1])


def p_args(p):
    '''args : val
            | args val
            | '''
    #no args
    if len(p) == 1:
        p[0] = []
    #one arg
    elif len(p)==2:
        p[0]=[p[1]]
    else:
        p[0]=[p[1],p[2]]

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

def p_empty(p):
    '''empty : '''
    
def p_error(p):
    print("Syntax Error at", p.value)






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




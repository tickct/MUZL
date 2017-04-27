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
import argparse

rules = {}
variables = {}

precedence = (
    ('nonassoc', 'LTHAN', 'GTHAN', 'ETO', 'GETHAN', 'LETHAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW')
)

def number(a):
    if isinstance(a, int):
        return float(a)
    if isinstance(a, float):
        return a
    if isinstance(a, bool):
        if a:
            return 1
        else:
            return 0
    if isinstance(a, str):
        if len(a) == 1:
            return ord(a)
        elif a[1] == 'x':
            return int(a, 0)


def type_convert(x, typ):
    if typ == 'hex':
        if isinstance(x, str):
            if len(x) == 1:
                y = hex(ord(x))
            else:
                y = hex(int(x, 0))
        else:
            y = hex(int(x))
    elif typ == 'int':
        # char isnt a type in python
        if isinstance(x, str):
            if len(x) == 1:
                y = ord(x)
            else:
                y = int(x, 0)
        else:
            y = int(round(x))
    elif typ == 'char':
        if isinstance(x, str):
            if len(x) == 1:
                y = x
            else:
                y = chr(int(x, 0))
        else:
            y = chr(int(x))
    elif typ == 'bool':
        y = bool(x)
    elif typ == 'float':
        # for char
        if isinstance(x, str):
            if len(x) == 1:
                y = float(ord(x))
            else:
                y = float(int(x, 0))
        else:
            y = float(x)
    return y


# this needs to stay above all the start options, it defines what items can stand alone in a parse
def p_start(p):
    '''start : rule
             | expression'''
    p[0] = p[1]


def p_rule(p):
    '''rule : rname RULE LPAREN assign RPAREN ARROW type RBLOCK'''
    rules[p[1]] = MuzlRule.rule(p[1], p[4], p[7], p[8])
    p[0] = p[1] + ' created.'


def p_rname(p):
    '''rname : ID'''
    p[0] = p[1]


def p_assign_variables(p):
    '''assign : assign COLON ID type
              | ID type
              | empty '''
    if len(p) == 3:
        p[0] = [[p[1], p[2]]]
    elif len(p) == 5:
        # these two need to be on different lines due to = assigning before .append
        p[1].append([p[3], p[4]])
        p[0] = p[1]
        # catch no args so it is empty list vs none
    else:
        p[0] = []
def p_expression_conditional(p):
    '''expression : IF LPAREN mathTop RPAREN expression COLON expression'''
    if p[3]:
        p[0]=p[5]
    else:
        p[0]=p[7]
def p_expression_math(p):
    'expression : mathTop'
    p[0] = p[1]
def p_mathTop_mathLV3(p):
    'mathTop : mathlv3'
    p[0] = p[1]

def p_expression_comparisons(p):
    '''mathTop : mathTop ETO mathlv3
                  | mathTop LETHAN mathlv3
                  | mathTop GETHAN mathlv3
                  | mathTop GTHAN mathlv3
                  | mathTop LTHAN mathlv3 '''
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
    'mathlv3 : mathlv3 PLUS mathlv2'
    p[0] = number(p[1]) + number(p[3])


def p_expression_subtract(p):
    '''mathlv3    : mathlv3 MINUS mathlv2
                  | MINUS mathlv3'''
    if len(p) == 3:
        p[0] = -p[2]
    else:
        p[0] = number(p[1]) - number(p[3])

def p_expression_term(p):
    '''mathlv3 : mathlv2'''
    p[0] = p[1]

def p_expression_mult(p):
    'mathlv2 : mathlv2 TIMES mathlv1'
    p[0] = number(p[1]) * number(p[3])


def p_expression_divide(p):
    'mathlv2 : mathlv2 DIVIDE mathlv1'
    p[0] = number(p[1]) / number(p[3])

def p_term_math1(p):
    'mathlv2 : mathlv1'
    p[0] = p[1]

def p_math1_math0(p):
    'mathlv1 : mathlv0'
    p[0] = p[1]

def calc_rule(rule, bindings):
    for x in range(0, len(bindings)):
        variables[rule.args[x][0]] = bindings[x]
    parse_result = type_convert(parser.parse(rule.expression), rule.ret)
    return parse_result


def p_expression_rule(p):
    '''mathlv1    : ID LPAREN args RPAREN
                  | ID LPAREN RPAREN'''

    if p[1] in rules.keys():
        # check that arguments given match arguments expected first set of ifs to see if args
        if len(p) > 4:
            if len(rules[p[1]].args) == len(p[3]):
                p[0] = calc_rule(rules[p[1]], p[3])
            else:
                print('Error: Argument Mismatch, expeted', len(rules[p[1]].args), ' found ', len(p[3]))
        else:
            if len(rules[p[1]].args) == 0:
                p[0] = calc_rule(rules[p[1]], [])
            else:
                print('Error: Argument Mismatch, expeted', len(rules[p[1]].args), ' found ', len(p[3]))

    else:
        print('Error: Rule not found:', p[1])


def p_args(p):
    '''args : val
            | args val'''
    # no args
    if len(p) == 1:
        p[0] = []
    # one arg
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_expression_pow(p):
    'mathlv1 : mathlv1 POW mathlv0'
    p[0] = p[1] ** number(p[3])


def p_expression_parens(p):
    '''mathlv0 : LPAREN expression RPAREN
             | LPAREN expression RPAREN DOT type'''
    if len(p) == 6:
        p[0] = type_convert(p[2], p[5])
    else:
        p[0] = p[2]


def p_term_val(p):
    '''mathlv0 : val
             | val DOT type'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = type_convert(p[1], p[3])


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


def p_val_id(p):
    '''val : ID '''
    if p[1] in variables.keys():
        p[0] = variables[p[1]]
    else:
        print("ID not found:", p[1])



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
    if p:
        print("Syntax Error at ", p.value)
    else:
        print("Syntax Error: END detected")






parser = yacc.yacc()

def get_parser():
    return parser


if __name__ == '__main__':
    argp = argparse.ArgumentParser()
    argp.add_argument('-d','--debug',help="output debug options",action="store_true")
    args =argp.parse_args()

    while True:
        try:
            s = input('!-')
        except EOFError:
            break
        if not s:
            continue
        if args.debug:
            result = parser.parse(s,debug=1)
        else:
            result = parser.parse(s)
        print(result)




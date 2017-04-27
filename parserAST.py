"""
Morgan Peters and Sean Gray
CS 440: Languages and Translators
Spring 2017
AST output of MUZL
"""

import ply.yacc as yacc
# token map import
from lexical import tokens
import MuzlRule

class Node:


    def __init__(self,val):
        self.val=val;
        self.children=[]

    def set_child(self,child):
        self.children.append(child)

def print_tree(node):
    queue = [(node, 0)]
    while queue:
        current = queue.pop(0)
        for x in current[0].children:
            queue.append((x,current[1]+1))
        if queue:
            if queue[0][1] == current[1]:
                print(current[0].val, end='\t')
            else:
                print(current[0].val)
        else:
            print(current[0].val)
rules = {}
variables = {}
precedence = (
    ('nonassoc', 'LTHAN', 'GTHAN', 'ETO', 'GETHAN', 'LETHAN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW')
)

# this needs to stay above all the start options, it defines what items can stand alone in a parse
def p_start(p):
    '''start : rule
             | expression'''
    node = Node("start")
    node.set_child(p[1])
    p[0]=node

def p_rule(p):
    '''rule : rname RULE LPAREN assign RPAREN ARROW type RBLOCK'''
    rules[p[1].val] = MuzlRule.rule(p[1], p[4], p[7], p[8])
    print(rules)
    node = Node("rule")
    node.set_child(p[1])
    node.set_child(p[4])
    node.set_child(p[7])
    node.set_child(Node(p[8]))
    p[0]=node


def p_rname(p):
    '''rname : ID'''
    node =Node(p[1])
    p[0] = node


def p_assign_variables(p):
    '''assign : assign COLON ID type
              | ID type
              | empty '''
    if len(p) == 3:
        node = Node([[p[1], p[2]]])
        p[0] = node
    elif len(p) == 5:
        # these two need to be on different lines due to = assigning before .append
        node = Node([[p[3],p[4]]])
        node.set_child(p[1])
        p[0] = node
        # catch no args so it is empty list vs none
    else:
        p[0] = Node("[]")



def p_expression_comparisons(p):
    '''expression : expression ETO val
                  | expression LETHAN val
                  | expression GETHAN val
                  | expression GTHAN val
                  | expression LTHAN val '''
    node = Node(p[2])
    node.set_child(p[1])
    node.set_child(p[3])
    p[0] = node

def p_expression_plus(p):
    'expression : expression PLUS term'
    node = Node(p[2])
    node.set_child(p[1])
    node.set_child(p[3])
    p[0] = node


def p_expression_subtract(p):
    '''expression : expression MINUS term
                  | MINUS expression'''
    if len(p) == 3:
        node = Node(p[1])
        node.set_child(p[2])
        p[0] = node
    else:
        node = Node(p[2])
        node.set_child(p[1])
        node.set_child(p[3])
        p[0] = node

def p_expression_term(p):
    '''expression : term'''
    node = Node("expression")
    node.set_child(p[1])
    p[0] = node

def p_expression_mult(p):
    'term : term TIMES mathlv1'
    node = Node(p[2])
    node.set_child(p[1])
    node.set_child(p[3])
    p[0] = node


def p_expression_divide(p):
    'term : term DIVIDE mathlv1'
    node = Node(p[2])
    node.set_child(p[1])
    node.set_child(p[3])
    p[0] = node

def p_term_math1(p):
    'term : mathlv1'
    node = Node("term")
    node.set_child(p[1])
    p[0] = node

def p_math1_math0(p):
    'mathlv1 : mathlv0'
    node = Node("mathlv1")
    node.set_child(p[1])
    p[0] = node

def calc_rule(rule, bindings):
    for x in range(0, len(bindings)):
        variables[rule.args[x][0]] = bindings[x]
    parse_result = parser.parse(rule.expression)
    return parse_result


def p_expression_rule(p):
    '''mathlv1    : ID LPAREN args RPAREN
                  | ID LPAREN RPAREN'''

    if p[1] in rules.keys():
        # check that arguments given match arguments expected first set of ifs to see if args
        if len(p) > 4:
            if len(rules[p[1]].args.val) == len(p[3]):
                node = Node("Rule")
                node.set_child(calc_rule(rules[p[1]], p[3]))
                p[0] = node
            else:
                print('Error: Argument Mismatch, expeted', len(rules[p[1]].args), ' found ', len(p[3]))
        else:
            # it is 2 since the arg list is a string and '[]' is len 2
            if len(rules[p[1]].args.val) == 2:
                node = Node("Rule")
                node.set_child(calc_rule(rules[p[1]],[]))
                p[0] = node
            else:
                print('Error: Argument Mismatch, expeted', len(rules[p[1]].args.val), ' found ', len(p[3]))

    else:
        print('Error: Rule not found:', p[1])


def p_args(p):
    '''args : val
            | args val'''
    # no args
    if len(p) == 1:
        p[0] = Node([])
    # one arg
    elif len(p) == 2:
        node = Node(p[1])
        p[0] = node
    else:
        node = Node(p[2])
        node.set_child(p[1])
        p[0] = node


def p_expression_pow(p):
    'mathlv1 : mathlv1 POW mathlv0'
    node = Node(p[2])
    node.set_child(p[1])
    node.set_child(p[3])
    p[0] = node


def p_expression_parens(p):
    '''mathlv0 : LPAREN expression RPAREN
             | LPAREN expression RPAREN DOT type'''
    if len(p) == 6:
        node = Node('()')
        node.set_child(p[2])
        node2 = Node('.')
        node2.set_child(p[5])
        node2.set_child(node)
        p[0] = node2
    else:
        node = Node('()')
        node.set_child(p[2])
        p[0] = node


def p_term_val(p):
    '''mathlv0 : val
             | val DOT type'''
    if len(p) == 2:
        node = Node("mathlv0")
        node.set_child(p[1])
        p[0] = node
    else:
        node = Node('.')
        node.set_child(p[1])
        node.set_child(p[3])
        p[0] = node


# No string type change added
# does not recognise Char/doubles to convert


def p_value(p):
    '''val : INT
             | FLOAT
             | CHAR
             | STRING
             | BOOL
             | HEX '''
    p[0] = Node(p[1])


def p_val_id(p):
    '''val : ID '''
    if p[1] in variables.keys():
        p[0] = Node(variables[p[1]])
    else:
        print("ID not found:", p[1])



def p_type(p):
    '''type : INT_T
            | FLOAT_T
            | CHAR_T
            | STRING_T
            | BOOL_T
            | HEX_T '''
    p[0] = Node(p[1])


def p_empty(p):
    '''empty : '''


def p_error(p):
    print("Syntax Error")




parser = yacc.yacc()


def get_parser():
    return parser


if __name__ == '__main__':
    while True:
        try:
            s = input('!-')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s,debug=1)
        print_tree(result)
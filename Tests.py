import lexical

data1='''add rule (a:int,b:int)->int=
a+b!'''
lexer=lexical.getLex()
lexer.input(data1)
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
    

import ply.lex as lex

tokens = [
    'ID',
    'NUM',
    'PE',
    'PD',
    'VIRG'
]

t_PD = r'\('
t_PE = r'\)'
t_ID = r'\w+'
t_VIRG = r','

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \n\t'

def t_error(t):
    print('Illegal caracter' + t.value[0])

lexer = lex.lex()

import ply.yacc as yacc
import sys

def p_grammar(p):
    """
    lista_mista : PE conteudo PD

    conteudo :
              | elementos

    elementos : elemento
              | elemento VIRG elementos

    elemento : ID
             | NUM
             |       
    """
    pass

def p_error(p):
    print('Syntax error')

parser = yacc.yacc()

for line in sys.stdin:
    parser.input(line)



#for line in sys.stdin:
#    lexer.input(line)
#    for tok in lexer:
#        print(tok)    
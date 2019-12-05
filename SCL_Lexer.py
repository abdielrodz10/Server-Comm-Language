# ServerCommLanguage (SCL) Lexer

import sys, re

import ply.yacc as yacc
import ply.lex as lex
from ply.lex import TOKEN


reserved = {
    "hostName":"hostName",
    "port":"port",
    "openServer(hostName, port)": "openServer(hostName, port)",
    "openClient(hostName, port)":"openClient(hostName, port)",
    "closeServers()": "closeServers()"

}

#Create Tokens
tokens = list(reserved.values())

t_ignore = r' '

def t_method(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'hostName'
    return t


def t_error(t):
    print("Unrecognized Character(s)")
    print(t)
    t.lexer.skip(1)


lexer = lex.lex()

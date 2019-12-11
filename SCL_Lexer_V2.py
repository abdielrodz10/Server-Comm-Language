# ServerCommLanguage (SCL) Lexer
import ply.lex as lex
import re

# tokens
tokens = [
    'EQUALS', 'ID', 'DOT', 'IP', 'PORT',
    'COMMA', 'LP', 'RP',
]

reserved = {
    'new': 'NEW',
    'disconnect': 'DISCONNECT',
    'connect': 'CONNECT',
    'server': 'SERVER',
    'servers': 'SERVERS',
    'client': 'CLIENT',
    'clients': 'CLIENTS',
    'show': 'SHOW',
    'all': 'ALL',
    'to': 'TO',
    'remove': 'REMOVE'
}

tokens += reserved.values()


# general regex
def t_IP(t):
    r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    return t


def t_PORT(t):
    r'\d+'
    return t


def t_ID(t):
    r'\w+'
    value = t.value.lower()
    # check reserved words
    if reserved.get(value):
        t.value = str(t.value)
        t.type = reserved.get(value, t.type)
    else:
        t.type = 'ID'
    return t


# ignored
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Lexer
lexer = lex.lex(reflags=re.UNICODE)

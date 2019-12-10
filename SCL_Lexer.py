# ServerCommLanguage (SCL) Lexer
import ply.lex as lex
from ply.lex import TOKEN
import re

reserved = {
    'OPERATION_0ARG': ['DELETE ALL', 'DISCONNECT ALL'],
    'OPERATION_1ARG': ['DELETE', 'DISCONNECT'],
    'OPERATION_2ARG': ['NEW SERVER', 'NEW CLIENT', 'CONNECT']
}

# tokens
tokens = [
    'EQUALS', 'ID', 'DOT', 'IP',
    'COMMA', 'LP', 'RP',
] + list(reserved)


# custom methods regex
operation_0arg = re.compile('|'.join(reserved['OPERATION_0ARG']))
operation_1arg = re.compile('|'.join(reserved['OPERATION_1ARG']))
operation_2arg = re.compile('|'.join(reserved['OPERATION_2ARG']))


# custom method tokens
@TOKEN(operation_0arg.pattern)
def t_OPERATION_0ARG(t):
    return t


@TOKEN(operation_1arg.pattern)
def t_OPERATION_1ARG(t):
    return t


@TOKEN(operation_2arg.pattern)
def t_OPERATION_2ARG(t):
    return t


# general regex

# def t_NUMBER(t):
#     r'-?\d+'
#     try:
#         t.value = int(t.value)
#     except ValueError:
#         print("Integer value too large %d", t.value)
#         t.value = 0
#     return t

def t_IP(t):
    r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    return t

# def t_STRING(t):
#     r'\"(.+?)\"'
#     return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    # t.type = reserved.get(t.value, 'ID')  # Check reserved words
    return t


# basic delimiters
t_EQUALS = r'\='
t_DOT = r'\.'
t_COMMA = r'\,'
t_LP = r'\('
t_RP = r'\)'

# ignored..
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Lexer
lexer = lex.lex(reflags=re.UNICODE)
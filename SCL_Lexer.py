# ServerCommLanguage (SCL) Lexer
import ply.lex as lex
from ply.lex import TOKEN
import re

reserved = {
    'METHOD_MAIN': ['openHost', 'openClient']
}

# tokens
tokens = [
    'INT',
    'EQUALS', 'ID', 'DOT',
    'COMMA', 'LP', 'RP', 'STRING',
] + list(reserved)


reg_method_main = re.compile('|'.join(reserved['METHOD_MAIN']))


@TOKEN(reg_method_main.pattern)
def t_METHOD_MAIN(t):
    return t

# Generic Regular Expressions

def t_INT(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\"(.+?)\"'
    return t

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
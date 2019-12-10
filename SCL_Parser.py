# ServerCommLanguage (SCL) Parser
import sys

import ply.yacc as yacc
import SCL_Lexer as scl_lex

tokens = scl_lex.tokens

# globals
servers = []
clients = []


def p_expression(p):
    '''expression : operation
                    | empty
                    '''
    p[0] = (p[1])


def p_operation(p):
    '''operation : operation_0arg
                    | operation_1arg
                    | operation_2arg
                    '''
    p[0] = (p[1])


# general operations w/o arguments
def p_operation_0arg(p):
    '''operation_0arg : OPERATION_0ARG '''
    p[0] = (p[1])

    if p[1] == 'DISCONNECT ALL':
        # TODO: Implement Op
        print('not implemented...')
    if p[1] == 'DELETE ALL':
        # TODO: Implement Op
        print('not implemented...')

    print(p[0])


# operations w/ one argument
def p_operation_1arg(p):
    '''operation_1arg : OPERATION_1ARG ID
                        | OPERATION_1ARG IP
                        '''
    p[0] = (p[1], p[2])

    if p[1] == 'DISCONNECT':
        # TODO: Implement Op
        print('not implemented...')
    elif p[1] == 'DELETE':
        # TODO Implement Op
        print('not implemented...')

    print(p[0])


# operations w/ two arguments
def p_operation_2arg(p):
    '''operation_2arg : OPERATION_2ARG ID IP '''
    p[0] = (p[1], p[2], p[3])

    if p[1] == 'NEW SERVER':
        # TODO: Implement Op
        # s = Server(p[2], p[3])
        # servers.append(s)
        print('not implemented..')
        servers.append(p[0])
    elif p[1] == 'NEW CLIENT':
        # TODO: Implement Op
        # c = Client(p[2], p[3])
        # clients.append(c)
        print('not implemented..')

    print(p[0])


# empty operation
def p_empty(p):
    '''empty : '''
    p[0] = None


# parser error
def p_error(p):
    print(p)
    print("Syntax error")


def parser():
    return yacc.yacc()

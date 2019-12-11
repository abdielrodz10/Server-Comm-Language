# ServerCommLanguage (SCL) Parser
import ply.yacc as yacc
import SCL_Lexer_V2 as scl_lex

from Client import *
from Server import *

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
    '''operation : new_server
                    | new_client
                    | connect_to_server
                    | disconnect_client
                    | disconnect_server
                    | show_clients
                    | show_servers
                    | remove
                    '''
    p[0] = (p[1])

def p_new_server(p):
    '''new_server : NEW SERVER empty
                    | NEW SERVER IP PORT
                    '''
    print('new server...')
    p[0] = p[1]

def p_new_client(p):
    '''new_client : NEW CLIENT
                    | NEW CLIENT IP PORT
                    '''
    print('new client...')
    p[0] = p[1]

def p_connect_to_server(p):
    '''connect_to_server : CONNECT CLIENT ID TO SERVER ID '''
    p[0] = p[1]

def p_disconnect_client(p):
    '''disconnect_client : DISCONNECT CLIENT ID '''
    p[0] = p[1]

def p_disconnect_server(p):
    '''disconnect_server : DISCONNECT SERVER ID '''
    p[0] = p[1]

def p_show_clients(p):
    '''show_clients : SHOW ALL CLIENTS '''
    p[0] = p[1]

def p_show_servers(p):
    '''show_servers : SHOW ALL SERVERS '''
    p[0] = p[1]

def p_remove(p):
    '''remove : REMOVE SERVER ID
                | REMOVE CLIENT ID
                '''
    p[0] = p[1]


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

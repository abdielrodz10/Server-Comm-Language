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

    if p[3] is None:
        n_server = Server()
    else:
        n_server = Server(p[3], p[4])

    servers.append(n_server)

    p[0] = p[1]


def p_new_client(p):
    '''new_client : NEW CLIENT empty
                    | NEW CLIENT IP PORT
                    '''
    if p[3] is None:
        n_client = Client()
    else:
        n_client = Client(p[3], p[4])

    clients.append(n_client)

    p[0] = p[1]


def p_connect_to_server(p):
    '''connect_to_server : CONNECT CLIENT ID TO SERVER ID '''
    p[0] = p[1]


def p_disconnect_client(p):
    '''disconnect_client : DISCONNECT CLIENT IP '''
    found = False

    for c in clients:
        if c.get_ip == p[3]:
            c.disconnect()
            found = True

    if not found:
        print('Client not found...')

    p[0] = p[1]


def p_disconnect_server(p):
    '''disconnect_server : DISCONNECT SERVER IP '''

    found = False

    for s in servers:
        if s.get_ip == p[3]:
            s.disconnect()
            found = True

    if not found:
        print('Server not found...')

    p[0] = p[1]


def p_show_clients(p):
    '''show_clients : SHOW ALL CLIENTS '''

    if len(clients) == 0:
        print('No active clients...')
    else:
        print('Active Clients: ')
        for c in clients:
            print(c.get_ip())

    p[0] = p[1]


def p_show_servers(p):
    '''show_servers : SHOW ALL SERVERS '''

    if len(servers) == 0:
        print('No active servers...')
    else:
        print('Active Servers: ')
        for s in servers:
            print(s.get_ip())

    p[0] = p[1]


def p_remove(p):
    '''remove : REMOVE SERVER IP
                | REMOVE CLIENT IP
                '''

    if p[2] == 'Server':
        for s in servers:
            if s.get_ip() == p[3]:
                s.disconnect()
                servers.remove(s)
                print('removed server')
    else:
        for c in clients:
            if c.get_ip() == p[3]:
                c.disconnect()
                clients.remove(c)
                print('removed client')

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

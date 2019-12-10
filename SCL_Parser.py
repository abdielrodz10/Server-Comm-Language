# ServerCommLanguage (SCL) Parser
import ply.yacc as yacc
import SCL_Lexer as scl_lex

tokens = scl_lex.tokens


def p_method_main(p):
    '''method_main : METHOD_MAIN LP RP '''

    print('Method No Parameter: {0}'.format(p[1]))

    if p[1] == "openHost":
        print('do openServer operations here..')
    elif p[1] == "openClient":
        print('do openClient operations here..')


def p_empty(p):
    '''empty :  '''
    p[0] = None


def p_error(p):
    print("SCL Syntax error")
    # sys.exit("Syntax error in input")


def parser():
    return yacc.yacc()

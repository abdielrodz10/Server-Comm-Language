# ServerCommLanguage (SCL) Parser

import ply.yacc as yacc
import
tokens =
names = {}




# called from ServerComm
def get_yacc_parser():
    return yacc.yacc()

def p_error(s):
    parser.parse(s)

parser = yacc.yacc()
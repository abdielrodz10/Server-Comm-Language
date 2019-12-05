# ServerCommLanguage (SCL) Parser

import ply.yacc as yacc

import SCL_Lexer as scl_lexer

# import tokens from lexer
tokens = scl_lexer.tokens

# TODO: Implement parsing rules


# called from ServerComm
def get_yacc_parser():
    return yacc.yacc()

# ServerCommLanguage (SCL) Parser

import ply.yacc as yacc

# TODO: Implement parsing rules


# called from ServerComm
def get_yacc_parser():
    return yacc.yacc()

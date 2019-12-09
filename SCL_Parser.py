# ServerCommLanguage (SCL) Parser
import SCL_Lexer as lex
from SCL_Methods import *

import ply.yacc as yacc

METHODS = ["openHost()", "openClient()"]

class Parser():
    def init(self,Methods):
        self.methods = Methods






# import tokens from lexer
# tokens = lex.lexer.expresions

# TODO: Implement parsing rules

def methods(line):
        if line == lex.lexer.METHOD:
            if line in METHODS:
                if line == "openHost()":
                    print('openhost()')
                    server_program()
                else:
                    if line == "openClient()":
                        print('openhost()')
                        client_program()

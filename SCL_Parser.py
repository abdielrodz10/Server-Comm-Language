# ServerCommLanguage (SCL) Parser
import SCL_Lexer as lex
from SCL_Methods import client_program
from SCL_Methods import server_program

import ply.yacc as yacc

METHODS = ["openHost()", "openClient()"]
class Parser():
    def init(self,Methods):
        self.methods = Methods






# import tokens from lexer
tokens = lex.lexer.expresions

# TODO: Implement parsing rules




def methods(self):
    for line in self.methods:
        if line[0] == lex.lexer.METHOD:
            if line[0] in METHODS:
                if line[0] == "openHost()":
                    server_program()
                else:
                    if line[0] == "openClient()":
                        client_program()
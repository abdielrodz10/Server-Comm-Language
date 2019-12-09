# ServerCommLanguage (SCL) Lexer
import sys
import os
import re
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font
from tkinter import *


class lexer():
    def init(self, characters):
        self.characters = characters

    HOSTNAME = 'HOSTNAME'
    PORT = 'PORT'
    METHOD = 'METHOD'
    HOST = 'HOST'
    CLIENT = 'CLIENT'


    #expresions = [
     #   (r'[A-Za-z]', HOSTNAME),
     #   (r'[0-9]*',        PORT),
       # (r'open',        METHOD),
       # (r'close',       METHOD),
       # (r'Host',          HOST),
      #  (r'Client',      CLIENT),]

def generate(self):
    pos = 0
    tokens = []
    while pos< len(self.characters):
        match = None
        for expresion in self.expresions:
            pattern, tag = expresion
            regex = re.compile(pattern)
            match = regex.match(self.characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)

                break

        if not match:
            sys.stderr.write('Unknown character: %s\n' % self.characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


def lex(self):
        return self.generate()
# ServerCommLanguage (SCL) methods and logic
import SCL_Parser

scl_parser = SCL_Parser.get_yacc_parser()
# high level server operations


def read_document(doc):
    f = open(doc, 'r')
    for line in f:
        scl_parser.parse(line)

    f.close()

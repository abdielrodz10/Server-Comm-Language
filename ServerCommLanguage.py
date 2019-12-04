# Main Language File

import SCL_Parser

scl_parser = SCL_Parser.get_yacc_parser()

while True:
    try:
        user_in = input('SCL >>')
        scl_parser.parse(user_in)
    except (KeyboardInterrupt, EOFError):
        break

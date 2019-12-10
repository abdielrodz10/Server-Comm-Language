# Main Language File

import SCL_Parser
scl_parser = SCL_Parser.parser()

# import SCL_Methods
#
# input_doc = open('input.txt', 'r')
#
# try:
#     SCL_Methods.read_document(input_doc)
# except FileNotFoundError:
#     print('Error reading file...')
#
# input_doc.close()

while True:
    try:
        user_in = input('SCL >> ')
        scl_parser.parse(user_in)
    except (KeyboardInterrupt, EOFError):
        break

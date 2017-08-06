# -*- utf-8 -*-
""" todo
1. searching for uppercase words and surround it with {{c1: :root}}
2. searching for words within quotations and surround it with {{cn: }}
3. adding <hr> after first line
4. make everything into one line"""

import re

def main():
    """ main function"""

    with open(r"root.txt", 'r') as file:
        content_list = file.readlines()


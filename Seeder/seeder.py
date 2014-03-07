#!/usr/bin/python

import argparse
import lex_parse

#arguments
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Insert a file.")

args = parser.parse_args()

print(args.file)


#opening file
try:
  f = open(args.file, 'r')

except IOError:
  print("No such file")
  

#reading file
#for line in f:
#  print line

lexer = lex_parse.build_lex()

lex_parse.input_lex(lexer,f)
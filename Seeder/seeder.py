#!/usr/bin/python

import argparse
import s_lexical

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

s_lexical.lex_parse(f)
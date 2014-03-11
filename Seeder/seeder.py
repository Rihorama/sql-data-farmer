#!/usr/bin/python

import argparse
import lex_parse as parser

#arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("file", help="Insert a file.")

args = arg_parser.parse_args()

print(args.file)


#opening file
try:
  f = open(args.file, 'r')

except IOError:
  print("No such file")
  

#reading file
#for line in f:
#  print line

parser.dsl_parser(f)
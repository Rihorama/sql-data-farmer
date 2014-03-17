#!/usr/bin/python

import argparse
import lex_parse as parser
from values_generator import filler


#arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("file", help="Insert a file.")

args = arg_parser.parse_args()




#opening file
try:
  f = open(args.file, 'r')

except IOError:
  print("No such file")
  

#reading file
#for line in f:
#  print line


table_list = parser.dsl_parser(f)

for table in table_list:
    
    #table.print_table()
    filler(table)
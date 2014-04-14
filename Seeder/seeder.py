#!/usr/bin/python

import argparse
import lex_parse as parser
from values_generator import iniciate_fk,db_filler
from printer import errprint,ERRCODE


#arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("file", help="Insert a file.")

args = arg_parser.parse_args()




#opening file
try:
    f = open(args.file, 'r')

except IOError:
    msg = "Input error: The given file of path '" + path + "' cannot be oppened."
    errprint(msg, ERRCODE["INPUT"])
  

#reading file
#for line in f:
#  print line


table_list = parser.dsl_parser(f)


#Close file
f.close()

iniciate_fk(table_list)
db_filler(table_list)

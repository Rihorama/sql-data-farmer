#!/usr/bin/python

import argparse
import os
import lex_parse as parser
from values_generator import iniciate_fk,db_filler
from printer import errprint,ERRCODE


#arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-s","--source", metavar=('PATH'), help="Custom path to a DSL file.")

args = arg_parser.parse_args()


if args.source:                      #we've been given a custom source path
    src = args.source    
else:
    home = os.path.expanduser('~')   #get the home directory for this user
    src = home + "/dsl.txt"          #creates the path representing ~/dsl.txt

#opening file
try:
    f = open(src, 'r')

except IOError:
    msg = "Input error: The source file couldn't be oppened."
    errprint(msg, ERRCODE["INPUT"])
  

#reading file
#for line in f:
#  print line


table_list = parser.dsl_parser(f)


#Close file
f.close()

iniciate_fk(table_list)
db_filler(table_list)

#!/usr/bin/python

import argparse
from dsl_gen import dsl_generator
import lex_parse as parser
from printer import errprint,ERRCODE


#arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("file", help="Insert a file.")

args = arg_parser.parse_args()




#opening given file
try:
    f = open(args.file, 'r')
except IOError:
    msg = "Input error: The given file of path '" + path + "' cannot be oppened."
    errprint(msg, ERRCODE["INPUT"])

#opening temp file 
try:
    tempf = open("tempfile", 'w')
except IOError:
    msg = "Runtime error: Did not manage to create a temporary file 'tempfile'."
    errprint(msg, ERRCODE["RUNTIME"])    
    
  

#filters the incomming dump so only useful queries remain
#creates a temporary file
starts = ("ALTER TABLE ONLY","CREATE TABLE")

query = False                       #flag saying that at the moment we are not examining lines we want
for line in f:
    li=line.strip()                  #get rid of whitespaces on both ends

    #we found a start of a desired query
    if li.startswith(starts):
        query = True
        tempf.write(line)          
    
    #query continues
    elif query:
        tempf.write(line)
        if li.endswith(";"):         #if this line edns with semicolon, the desired query ends
            query = False            #we reset the flag

          
#closing temp file for writing and opening it for reading
tempf.close()
try:
    tempf = open("tempfile", 'r')
except IOError:
    msg = "Runtime error: Did not manage to open a temporary file 'tempfile'."
    errprint(msg, ERRCODE["RUNTIME"]) 


table_list = parser.sql_parser(tempf)

for table in table_list:
    table.print_table()

dsl_generator(table_list)


#Close file
f.close()
tempf.close()

#iniciate_fk(table_list)
#db_filler(table_list)

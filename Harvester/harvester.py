#!/usr/bin/python

import argparse
from dsl_gen import dsl_generator
import lex_parse as parser
from printer import errprint,ERRCODE
import tempfile




###-------------------------
###-------------------------

#Preparses the given dump to leave only things we want
#takes only CREATE TABLE queries and ALTER TABLE ONLY
def preparse(f,tempf):
    
    create = False                       #flag saying that at the moment we are not examining lines of CREATE TABLE query
    alter = False                        #nor ALTER TABLE ONLY query
    not_yet = False                      #True if we need to wait for semicolon
    
    for line in f:
        li=line.strip()                  #get rid of whitespaces on both ends


        if li.startswith("CREATE TABLE"):
            if not li.endswith(";"): 
                create = True                #the query continues over more lines
            tempf.write(line)

        elif li.startswith("ALTER TABLE ONLY"):
            if li.endswith(";") and not "KEY" in li: #it's aparently not the alter we want
                continue                             #we skip this iteration
            elif li.endswith(";"):                   
                tempf.write(line)                    #should contain KEY then
            else:           
                alter = True
                save = line
            
        #query continues    
        elif create:
            tempf.write(line)
            if li.endswith(";"):          #if this line ends with semicolon, the desired query ends
                create = False            #we reset the flag
        
        #to filter only primary and foreign key alter queries        
        elif alter:
            if "KEY" in li:
                tempf.write(save)
                tempf.write(line)
                if li.endswith(";"):          #if this line ends with semicolon, the desired query ends
                    alter = False             #we reset the flag
                else:
                    not_yet = True            #the query is what we want but we haven't reached the semicolon yet
                    
            elif not_yet:
                tempf.write(line)
                if li.endswith(";"):          #if this line edns with semicolon, the desired query ends
                    alter = False             #we reset the flag
                    not_yet = False



###-------------------
###-------------------





DEST = None   #stores user-chosen destination for results (stdout/file)


#arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("src", help="Path to the source db dump.")

group = arg_parser.add_mutually_exclusive_group()
group.add_argument("-f", "--file", action="store_true", help="Save as a file.")
group.add_argument("-s", "--stdout", action="store_true", help="Print to stdout.")

args = arg_parser.parse_args()

#none of them was inserted
if not args.file and not args.stdout:
    arg_parser.error( 'You must choose either -f or -s argument.' )

#checking conflicting options for output
if args.file:
    DEST = "file"
else:               #stdout
    DEST = "stdout"
    


#opening given file
try:
    f = open(args.src, 'r')
except IOError:
    msg = "Input error: The given file of path '" + path + "' cannot be oppened."
    errprint(msg, ERRCODE["INPUT"])

#opening temp file 
try:
    #tempf = open("tempfile", 'w')
    tempf = tempfile.TemporaryFile()
except IOError:
    msg = "Runtime error: Did not manage to create a temporary file 'tempfile'."
    errprint(msg, ERRCODE["RUNTIME"])    
    

#Filters the dump so we get only queries we are interested in  
preparse(f,tempf)

#Close the dump file
f.close()  

#Setting the position to the start of temp file
tempf.seek(0)

#Parse what's in temp file
table_list = parser.sql_parser(tempf)


#for table in table_list:
#    table.print_table()

#generating the DSL file
dsl_generator(table_list,DEST)


#Close file
tempf.close()






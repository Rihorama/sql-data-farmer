
from printer import errprint,ERRCODE
import sys
import os


FILL_CNT = 10
NULL_FILL = 20


DTYPE_DICT = {
    'bigint' : 'BIGINT',
    'bit' : 'BIT',
    'bit varying' : 'VARBIT',
    'boolean' : 'BOOL',
    'box' : 'BOX',
    'character varying' : 'VARCHAR',
    'character' : 'CHAR',
    'circle' : 'CIRCLE',
    'integer' : 'INT',
    #'line' : 'LINE',
    'lseg' : 'LSEG',
    'path' : 'PATH',
    'point' : 'POINT',
    'polygon' : 'POLYGON',
    'smallint' : 'SMALLINT',
    'text' : 'TEXT',
    }

#creates a DSL line describing attribute's data type
def get_dtype_line(attr):
    
    if attr.data_type in DTYPE_DICT.keys():
        line = "\t\tTYPE " + DTYPE_DICT[attr.data_type]
    else:
        line = "\t\tTYPE " + attr.data_type
    
    x = "("
    flag = False
    for param in attr.parameters:
        flag = True
        x = x + str(param)
    x = x + ")"
    
    if flag:
        line = line + x
        
    return line


#creates a DSL line describing fill method
def get_fill_line(attr):
    
    line = "\t\tFILL "
    
    if attr.foreign_key:
        ref = attr.fk_table.name + ":" + attr.fk_attribute.name
        line = line + "fm_reference(" + ref + ")"
    else:
        line = line + "fm_basic()" 
        
    return line

#TODO: Check constraint compatibility and iniciate their count
#creates a constraint line if necessary
def get_constr_line(attr):
    
    if not attr.constraint_flag or (attr.not_null and attr.constraint_cnt == 1):
        return ""
    
    line = "\t\tCONSTRAINT "
    
    if attr.null:
        line = line + "null(" + NULL_CHANCE + ") "
    if attr.primary_key:
        line = line + "primary_key "
    if attr.foreign_key:
        line = line + "foreign_key "
    if attr.unique:
        line = line + "unique "
        
    return line
        


#A function that generates the dsl file
#according to the given table list
def dsl_generator(table_list,DEST):
    
    #iniciates
    initiate_gen(table_list)
    
    if(DEST == "file"):
        home = os.path.expanduser('~')   #get the home directory for this user
        pth = home + "/dsl.txt"          #creates the path representing ~/dsl.txt
        try:
            fd = open(pth, 'w')
        except IOError:
            msg = "Runtime error: Did not manage to create a destination file '~/dsl.txt'."
            errprint(msg, ERRCODE["RUNTIME"])             
    else:    
        fd = sys.stdout
    
    
    for table in table_list:
        fd.write("TABLE:" + table.name + "(" + str(FILL_CNT) + ")\n")
        
        for attr in table.attr_list:
            fd.write("\t::" + attr.name + "\n")            
            fd.write(get_dtype_line(attr) + "\n")
            fd.write(get_fill_line(attr) + "\n")
            fd.write(get_constr_line(attr) + "\n")
            
        
        fd.write("\n")    

#Does everything necessary for the generator to work
#checks constraint compatibility for each attribute
def initiate_gen(table_list):
    
    for table in table_list:
        
        for attr in table.attr_list:
            
            if attr.constraint_flag and attr.constraint_cnt > 1:
                #TODO:check if unique and primary key can be together
                check1 = attr.unique and attr.primary_key
                check2 = attr.null and attr.primary_key
                check3 = attr.null and attr.not_null
                
                check = check1 or check2 or check3
                
                if check:
                    msg = "Input error: Not compatible constraints used for attribute '" \
                          + attr.name + "', table '" + table.name + "'.\n"
                    errprint(msg, ERRCODE["INPUT"]) 
            
            
            
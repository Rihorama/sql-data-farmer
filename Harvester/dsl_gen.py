
from printer import errprint,ERRCODE


FILL_CNT = 10
NULL_FILL = 20
DTYPE_DICT = {
    'character varying' : 'VARCHAR',
    'character' : 'CHAR',
    'boolean' : 'BOOL',
    'integer' : 'INT',   
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
    
    if not attr.constraint_flag:
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
def dsl_generator(table_list):
    
    #iniciates
    initiate_gen(table_list)
    
    for table in table_list:
        print "TABLE:" + table.name + "(" + str(FILL_CNT) + ")"
        
        for attr in table.attr_list:
            print "\t::" + attr.name
            
            print get_dtype_line(attr)
            print get_fill_line(attr)
            print get_constr_line(attr)
            
            print "\n\n"
            

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
            
            
            
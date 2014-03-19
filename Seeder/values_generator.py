
import class_table
from method_basic import fm_basic
from method_regex import fm_regex
import sys




# Returns a string concatenated of generated values for each attribute
def get_values(table):
    
    values = ""

    for attr in table.attr_list:
                
        new_val = None
        
        func = 'new_val = ' + attr.fill_method + '(table,attr)'
        
        try: 
            exec func  #new_val = fill_method(attributes)
        except AttributeError:
            sys.stderr.write("Internal error. Not defined fill method passed." \
                             "Recovery not possible, the functionality of Seeder is inconsistent from now on.\n")            
            exit()
        
        values = values + str(new_val) + ", "
   
    values = values[:-2]       #removes the ',' from the end of the string  
    
    return values
    
    
    
#takes the table and creates an insert string
def filler(table):
    
    for i in range(0,table.fill_count):
        values = get_values(table)
        string = "INSERT INTO " + table.name + "\n" + "VALUES (" + values + ");\n"
        print string
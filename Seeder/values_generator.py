
import class_table
from method_basic import fm_basic
from method_regex import fm_regex
from method_textbank import fm_textbank, textbank_close
import sys
import random
from printer import errprint, ERRCODE


TABLE_DICT = {}    #dictionary of all tables (name:object)



#TODO: pripadne vyresit smazani seznamu promennych, kdyz uz nejsou treba


# Finds the value list for the attribute that the foreign key points to
# and randomly chooses and returns one value from it.
def get_foreign(attr):
    
    #gets list of the desired values
    val_list = attr.fk_attribute.values_list
    
    length = len(val_list)
    i = random.randint(0,length)          #randomly chooses one index
    
    return val_list[i]



# Returns a string concatenated of generated values for each attribute
def get_values(table):
    
    values = ""

    for attr in table.attr_list:
                
        new_val = None
        
        if attr.constraint_type == "foreign_key":
            new_val = get_foreign(attr)
            
        else:
        
            func = 'new_val = ' + attr.fill_method + '(table,attr)'
            
            try: 
                exec func  #new_val = fill_method(attributes)
            except AttributeError:
                sys.stderr.write("Internal error. Not defined fill method passed." \
                                 "Recovery not possible, the functionality of Seeder is inconsistent from now on.\n")            
                exit()            
            
        values = values + str(new_val) + ", "  #concatenates the new value with the rest and divides with a ','
        
        if attr.fk_pointed:
            attr.values_list.append(new_val)      #we will need these values for filling foreign key attributes
        
        
        
    values = values[:-2]       #removes the ',' from the end of the string  
    
    return values    
   


#checks if the table foreign keys point only to already filled tables
#if yes, adds the table to the FILLABLE_LIST and returns True, else False
def table_check(table):
    
    flag = True                         #all ok so far
    
    for attr in table.attr_list:
        if attr.constraint_type == "foreign_key":
            if not attr.fk_table.solved:    #this attribute can't be filled as the foreign table hasn't been solved yet
                flag = False                #problem found
                break
        
    return flag





#takes the table and creates an insert string
def table_filler(table):  
    
    if not table_check(table):   #checks if we know enough to fill this table
        return True              #means there is an unifnished table
    
    for i in range(0,table.fill_count):
        values = get_values(table)
        string = "INSERT INTO " + table.name + "\n" + "VALUES (" + values + ");\n"
        print string
        
    textbank_close()  #closes the file if it's opened
    table.solved = True
    return False                 #no problems with this table
    



#main filling loop for all tables
def db_filler(table_list):
    
    i = True
    while i:    
        i = False  #changed to true if a table is left unfilled
        
        for table in table_list:        
            if table.solved == False:       #this table hasn't been filled yet
                y = table_filler(table) #of one is true, it remains true
                i = y or i

  
  #TODO: make some kind of timeout with a message if it exceedes
  
  
##
#INICIALIZATION
##
            
#makes a dictionary table_name:object
#
def create_table_dict(table_list):

    global TABLE_DICT

    for table in table_list:
        TABLE_DICT[table.name] = table
        
        
#for every attribute that is a FK iniciates its variables fk_table and fk_attribute
#with the correct objects using TABLE_DICT
#till this function there are only string names in these variables
def iniciate_fk(table_list):
    
    global TABLE_DICT    
    create_table_dict(table_list) 
    
    
    for table in table_list:   
        if table.fk:              #if this table contains foreign keys
            
            for attr in table.attr_list:    #we cycle over its attributes
                
                if attr.constraint_type == "foreign_key":
                                        
                    ftable_name = attr.fk_table     #stores the name of the foreign table and its attribute
                    fattr_name = attr.fk_attribute
                    
                    
                    #checks if this table actually exists in our dictionary
                    if ftable_name in TABLE_DICT:
                        ftable = TABLE_DICT[ftable_name]  #foreign table object
                    else:
                        msg = "Input error: The given foreign table '" + ftable_name + "' doesn't exist."
                        errprint(msg, ERRCODE["INPUT"])

                    #we know the table exists, now let's try to find the attribute
                    fattr = None
                    for f_attribute in ftable.attr_list:
                        if f_attribute.name == fattr_name: #this is the attribute foreign key points to
                            fattr = f_attribute            #foreign attribute object
                            break
                    
                    if fattr == None:
                        msg = "Input error: The given foreign attribute '" + fattr_name + "' doesn't exist in table '" \
                               + ftable_name + "'."
                        errprint(msg, ERRCODE["INPUT"])
                        
                    if fattr.data_type != attr.data_type:       #types do not correspond
                        msg = "Input error: The foreign-key-type attribute '" + attr.name + "'s data type doesn't correspond with " \
                              "the data type of the attribute it references to.\n"
                        errprint(msg, ERRCODE["INPUT"])
                        
                    #now we have both objects, we can store them in the variables
                    attr.fk_table = ftable
                    attr.fk_attribute = fattr
                    attr.fk_attribute.fk_pointed = True
                    attr.fk_attribute.fk_times += 1       #increments count of "how many points at me"


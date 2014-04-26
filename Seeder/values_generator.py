
import class_table
from method_basic import fm_basic
from method_regex import fm_regex
from method_textbank import fm_textbank, textbank_close
import sys
import random
from printer import errprint, ERRCODE


TABLE_DICT = {}    #dictionary of all tables (name:object)



#TODO: pripadne vyresit smazani seznamu promennych, kdyz uz nejsou treba

#checks if the given value has not been used to fill this attribute yet.
#returns True, if it's OK, False if it has been used
def check_unique(attr,value):
    
    if value in attr.values_list:
        return False
    
    return True



# Finds the value list for the attribute that the foreign key points to
# and randomly chooses and returns one value from it.
def get_foreign(attr):   
    
    if not attr.fk_assigned: #we encounter this attr for the first time
        if attr.unique:
            attr.fk_values = attr.fk_attribute.values_list[:]  #duplicates the values list
        else:
            attr.fk_values = attr.fk_attribute.values_list #only assigns the existing list
        
        attr.fk_assigned = True   #sets the flag - list of values has been set
        
        
    #gets list of the desired values to easily work with
    val_list = attr.fk_values
    
    length = len(val_list)
    #length_self = len(attr.values_list)    I have no idea where did this come from xD
    
    
    if length == 0:
        i = 0                                   #we have one item left (unique-fk combo issue only)
    else:
        i = random.randint(0,length-1)          #randomly chooses one index, minus 1 counts with empty endline
    
    
    if attr.unique:
        if len(val_list) != 0:       #we have something to take from
            value = val_list[i]
            del val_list[i]          #removes the value so we can't use it again
        else:
            msg = "Input error: Unique foreign key attribute '" + attr.name + "' cannot be filled " \
            + "as the source attribute '" \
            + attr.fk_attribute.name + "' doesn't offer enough unique values.\n" \
            + "NOTE: Seeder can only work with values it's generating in this run - not with any others.\n"
            errprint(msg, ERRCODE["INPUT"])
    else:
        value = val_list[i] #we don't care if it's repeated

    return value



# Returns a string concatenated of generated values for each attribute
def get_values(table):
    
    values = ""

    for attr in table.attr_list:
        
        new_val = None
        
        if attr.foreign_key:
            new_val = get_foreign(attr)  
            
        elif attr.serial:
            new_val = "DEFAULT"      #next sequence  
            
        else:        
            func = 'new_val = ' + attr.fill_method + '(table,attr)'
            
            try: 
                exec func  #new_val = fill_method(attributes)
            except AttributeError:
                msg = "Internal error. Trouble using '" + attr.fill_method + "' method on attribute '" \
                      + attr.name + "', table '" + table.name + "'.\n" \
                      + "NOTE: This may also be caused by a non existing method inserted.\n"
                errprint(msg, ERRCODE["INTERNAL"])            
        
        
        
        #unique and fk combo solved separately, rest must be solved here
        test1 = attr.unique and not attr.foreign_key
        
        #NOTE: serial is unique by its sequence, if it overflows because of low capacity, it's user's problem
        test2 = attr.unique and not attr.serial
        test3 = attr.primary_key and not attr.serial
        
        
        #if one test true, we must ensure the inserted value hasn't been used yet
        if test1 or test2 or test3:            
            timeout = 0            
            while not check_unique(attr,new_val):      #validity check if there is unique/primary key constraint
                if timeout >= 100:
                    msg = "Runtime error: The timeout for finding new unique value for attribute '" + attr.name + "' exceeded.\n" \
                          "Tip: Check if the given fill method offers enough unique values.\n"      
                    errprint(msg, ERRCODE["RUNTIME"])
                
                exec func                              #we call the method again (and again)
                timeout += 1
        
        
        
        #NULL appearance chance
        if attr.null == 'null':            
            chance = random.randint(0,100)
            if chance < attr.constraint_parameters[0]:
                new_val = 'NULL'
                


        values = values + str(new_val) + ", "     #concatenates the new value with the rest and divides with a ','
        
        if attr.fk_pointed or attr.unique:        #we will need these values either for filling foreign key attributes
            attr.values_list.append(new_val)      #or to make sure each inserted value is unique   
            
            
        
    values = values[:-2]       #removes the ',' from the end of the string once we end
    
    return values    
   


#checks if the table foreign keys point only to already filled tables
#if yes, adds the table to the FILLABLE_LIST and returns True, else False
def table_check(table):
    
    flag = True                         #all ok so far
    
    for attr in table.attr_list:
        if attr.foreign_key:
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
        textbank_close(table)  #closes the file if it's opened
        
    
    table.solved = True
    return False                 #no problems with this table
    



#main filling loop for all tables
def db_filler(table_list):
    
    iniciate_fk(table_list)  #calls the iniciatiation
    
    i = True
    while i:    
        i = False  #changed to true if a table is left unfilled
        
        for table in table_list:            
            if table.solved == False:       #this table hasn't been filled yet
                y = table_filler(table) 
                i = y or i                  #if one is true, it remains true
                
                
            

  
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
                
                #first compatibility-of-constraints check
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
                
                
                #and the main part, getting the foreign key dependences done
                if attr.foreign_key:
                                        
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


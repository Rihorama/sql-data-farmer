#-------TABLE CLASS---------

  
class Table:
    name = None          # table name
    fill_count = None    # how many insertions to this table
    attr_list = []       # list of Attribute objects associated with this table
    attr_count = None
    attr_fill = []       # an array supposed to consist arrays with fill values for each attribute
    fk = False           # flag for having at least one foreign key
    solved = False       # flag if the table has already been filled or not
    
    def print_table(self):
        print("Table name: " + self.name + ", Fill count: " + str(self.fill_count) + " Attribute cnt: " + str(self.attr_count))
        
        for attr in self.attr_list:
            print("Attribute " + attr.name + ", " + attr.data_type, attr.parameters, " Fill: " + attr.fill_method)
            
            
    def count_attributes(self):
        self.attr_count = len(self.attr_list)

        
        
class Attribute:
    name = None
    data_type = None
    parameters = []
    fill_method = None
    fill_parameters = []
    
    constraint_flag = False
    constraint_type = None
    
    #if this is a foreign key
    fk_table = None            #table where the foreign key points
    fk_attribute = None        #attribute where the foreign key points
    
    #if this is foreign-key-pointed
    fk_pointed = False
    fk_times = 0       #how many other attributes point to this one
    values_list = []           #this will store all values used for filling if neccessary
        
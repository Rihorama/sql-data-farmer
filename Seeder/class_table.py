#-------TABLE CLASS---------

  
class Table:
    
    def __init__(self):
        self.name = None          # table name
        self.fill_count = None    # how many insertions to this table
        self.attr_list = []       # list of Attribute objects associated with this table
        self.attr_count = None
        self.fk = False           # flag for having at least one foreign key
        self.solved = False       # flag if the table has already been filled or not

    
    def print_table(self):
        print("Table name: " + self.name + ", Fill count: " + str(self.fill_count) + " Attribute cnt: " + str(self.attr_count))
        
        for attr in self.attr_list:
            print("Attribute " + attr.name + ", " + attr.data_type, attr.parameters, " Fill: " + attr.fill_method)
            
            
    def count_attributes(self):
        self.attr_count = len(self.attr_list)

        
        
class Attribute:    

    def __init__(self):
        self.name = None
        self.data_type = None
        self.parameters = []
        self.fill_method = None
        self.fill_parameters = []
        
        self.constraint_flag = False
        self.constraint_type = ""
        self.unique = False
        self.constraint_parameters = []
        
        #if this is a foreign key
        self.fk_table = None            #table where the foreign key points
        self.fk_attribute = None        #attribute where the foreign key points
        
        #if this is foreign-key-pointed
        self.fk_pointed = False
        self.fk_times = 0               #how many other attributes point to this one
        
        self.values_list = []           #this will store all values used for filling if neccessary
        
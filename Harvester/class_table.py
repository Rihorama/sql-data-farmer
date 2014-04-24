#-------TABLE CLASS---------

  
class Table:
    
    def __init__(self):
        self.name = None          # table name
        #self.fill_count = None    # how many insertions to this table
        self.attr_list = []       # list of Attribute objects associated with this table
        self.attr_count = None
        #self.fk = False           # flag for having at least one foreign key
        #self.solved = False       # flag if the table has already been filled or not

    
    def print_table(self):
        print("Table name: " + self.name)
        
        for attr in self.attr_list:
            print("Attribute:", attr.name , attr.data_type, attr.parameters)
            
            if attr.constraint_flag:
                if attr.null:
                    constr = "NULL"
                    print("Constraint: " + constr)
                if attr.not_null:
                    constr = "NOT NULL"
                    print("Constraint: " + constr)
                if attr.primary_key:
                    constr = "PRIMARY KEY"
                    print("Constraint: " + constr)
                if attr.foreign_key:
                    constr = "FOREIGN KEY"
                    print("Constraint: " + constr)

                
            if attr.fk_table != None:
                print("FK Table: " + attr.fk_table.name + " FK Attribute: " + attr.fk_attribute.name)
            
            
    def count_attributes(self):
        self.attr_count = len(self.attr_list)

        
        
class Attribute:    

    def __init__(self):
        self.name = None
        self.data_type = None
        self.parameters = []
        
        self.constraint_flag = False
        self.constraint_cnt = 0
        
        self.null = False
        self.unique = False
        self.not_null = False
        self.primary_key = False
        self.foreign_key = False
        
        #if this is a foreign key
        self.fk_table = None            #table where the foreign key points
        self.fk_attribute = None        #attribute where the foreign key points
        
        #self.fill_method = None
        #self.fill_parameters = []
        
        #if this is foreign-key-pointed
        #self.fk_pointed = False
        #self.fk_times = 0               #how many other attributes point to this one
        
        #self.values_list = []           #this will store all values used for filling if neccessary
     
     
    #sets the flag for the certain constraint    
    def set_constraint(self,constr):
                
        if constr == 'NULL':
            self.null = True
        elif constr == 'NOT NULL':
            self.not_null = True
        elif constr == 'PRIMARY KEY':
            self.primary_key = True
        elif constr == 'UNIQUE':
            self.unique = True
        else:
            self.foreign_key = True
        
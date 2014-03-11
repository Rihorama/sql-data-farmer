#-------TABLE CLASS---------

  
class Table:
    name = None
    attr_list = []
    
    def print_table(self):
        print("Table name: " + self.name)
        
        for attr in self.attr_list:
            print("Attribute " + attr.name + ", " + attr.data_type)
  

        
        
class Attribute:
    name = None
    data_type = None
    
    ref_table = None
    ref_attribute = None
        
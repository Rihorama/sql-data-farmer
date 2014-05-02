
from method_basic import fm_basic
import random
import class_table



#According to fill method parameter uses either fm_basic or given default value
#Parameter equals to percentage of default chance. Anything greater than 99 will
#always use default value.
def fm_default(table,attr):
    
    default = attr.default_value
    chance = attr.fill_parameters[0]       #given chance percentage    
    rnd = random.randint(0,100)            #random chance
    
    if rnd <= chance:
        value = default
        
    else:
        value = fm_basic(table,attr)
        
        
    return value
    
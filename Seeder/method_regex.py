
import class_table
import exrex
import random
import sys

#

#User-controlled fill function
#Uses the given regex and returns a correct string
#Now accepting CHAR, VARCHAR, TEXT and INT (SMALLINT and BIGINT as well)
def fm_regex(table, attr):
        
    
    regex = attr.fill_parameters[0]
    regex = regex[1:-1]              #cuts the quotes
   
    value = exrex.getone(regex)

    
    
    #NOTE: If the given regex allows shorter results than the given length,
    #      the final result will be created by adding empty space by db.
    #      On contrary - if the given regex produced longer result, it will be cut
    if attr.data_type == "CHAR":        
        length = attr.parameters[0]
        
        while len(value) < length:
            value = value + exrex.getone(regex)
        
        value = value[:length]
        value = "'" + str(value) + "'"
        
        
    elif attr.data_type == "VARCHAR":
        length = attr.parameters[0]
        
        value = value[:length]
        value = "'" + str(value) + "'"
        
    elif attr.data_type == "TEXT":
        value = "'" + str(value) + "'"
    
    
    return value

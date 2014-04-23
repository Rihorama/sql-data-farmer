
import os
import class_table
import exrex
import random
import sys
from method_textbank import fm_textbank

FOUR_BYTE_MAX = 2147483647 

# Max range lower than 8: one word will be generated in this range. 
# Max range greater or equal to 8: more words generated.
# Vowels and consonants take turns to be at least readable.
# Least possible length is 2 characters.
def basic_varchar(table, attr):
    
    if not attr.parameters :
        sys.stderr.write("Internal error. Parameter of attribute " + attr.name + " disappeared." \
                         "Recovery not possible, the functionality of Seeder is inconsistent from now on.\n")
        exit()
        
    max_range = attr.parameters[0]  #the only param states the max range
    min_range = 2
    
    #to prevent provoking users
    if max_range == 1:
        min_range = 1
    
    
    #the regular expression to be used will be chosen according to the max range
    if max_range < 8:     #product will be one word
        regex = r'[BCDFGHJKLMNPQRSTVWXZ][aeiouy]([bcdfghjklmnpqrstvwxz][aeiouy])+'        
    else:
        regex = r'[BCDFGHJKLMNPQRSTVWXZ][aeiouy]([bcdfghjklmnpqrstvwxz][aeiouy]){1,2} (([bcdfghjklmnpqrstvwxz][aeiouy]){1,3})+'
        

    string = exrex.getone(regex)
    x = random.randint(2,max_range) #randomly generates varchar length for this iteration from range 
    
    value = string[:x]                #cuts the obtained string
    
     #checks for white space at the end of string and deletes it if yes
    if string[-1:] == ' ':
        string = string[:-1]

    return "\'" + value + "\'"   #for string values


    
#TODO:change error printing here to the one using printer   
#returns array of bit values of the given length
def basic_bit(table, attr):
    
    if not attr.parameters :
        sys.stderr.write("Internal error. Parameter of attribute " + attr.name + " disappeared." \
                         "Recovery not possible, the functionality of Seeder is inconsistent from now on.\n")
        exit()
          
    length = attr.parameters[0]
    regex = '[01]{' + str(length) + '}'    

    value = exrex.getone(regex) 

    return value




#Char will be filled with random alfanumerical strings of given length
def basic_char(table, attr):
    
    if not attr.parameters :
        sys.stderr.write("Internal error. Parameter of attribute " + attr.name + " disappeared." \
                         "Recovery not possible, the functionality of Seeder is inconsistent from now on.\n")
        exit()

        
    length = attr.parameters[0]    
    regex = r'[a-zA-Z0-9_]+'  
        
    string = exrex.getone(regex)

    #if the generated string was too short
    while len(string)<length:
        string = string + exrex.getone(regex)
    
    value = string[:length]           #cuts the obtained string
   
    return "\'" + value + "\'"
    
    

def basic_bool(table, attr):
        
    if ((random.randint(0,9))%2) == 0:  #if random value is even -> True
        value = True
    else:
        value = False

    return value




def basic_int(table, attr):
    
    flag = True
    regex = r'[-]?\d+'
    value = exrex.getone(regex)
    
    while(int(value) > FOUR_BYTE_MAX or int(value) < -FOUR_BYTE_MAX):           
        value = value[:-1]  #fitting the value to allowed range
         
    if value == "-0":
        value = "0"
  
    return value


def basic_text(table, attr):
    
    path = os.path.dirname(sys.argv[0]) + "/Textbank/sentence.txt"
    
    if len(attr.fill_parameters) == 0:     #the path hasn't been added yet
        attr.fill_parameters.append(path)  #here we put the textbank path as a parameters so it can use fm_textbank
    
    value = fm_textbank(table,attr)
    return value



#Basic fill function
#Recognizes the data type and uses it's basic method
def fm_basic(table, attr):
        
    
    #supported types for now: VARCHAR, BIT, CHAR, BOOLEAN, INT
    if attr.data_type == "VARCHAR":
        value = basic_varchar(table, attr)
        
    elif attr.data_type == "BIT":
        value = basic_bit(table, attr)
        
    elif attr.data_type == "CHAR":
        value = basic_char(table, attr)
        
    elif attr.data_type == "BOOL":
        value = basic_bool(table, attr)
        
    elif attr.data_type == "INT":
        value = basic_int(table, attr)
        
    elif attr.data_type == "TEXT":
        value = basic_text(table, attr)
        
    return value

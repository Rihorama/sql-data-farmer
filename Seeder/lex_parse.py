#!/usr/bin/python


import sys
import ply.lex as lex
import ply.yacc as yacc
import class_table as table
import re
from printer import debug
from printer import errprint
from printer import ERRCODE


sys.path.insert(0,"../..")


#TODO: Check newlines at the end of every error message

#table variables
table_list = []
new_table = None

attr_list = []
new_attribute = None

#error flag
err = False
    

##
#function to see the tokens
##
def input_lex(lexer, data):
  
    #data = f.read() #reads the file to string
  
    lexer.input(data)
  
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print tok



##
#function to check valid parameters for fill method
##
def check_valid(attr):
    
    method = attr.fill_method
    
    if method == 'fm_regex':
        
        check_regex_compatibility(attr)           #check if regex method can be used with given data type
        try:
            re.compile(str(attr.fill_parameters[0]))   #check if the given parameter is a valid regex
        except re.error:
            msg = "Semantic Error: Wrong parameter given to fill method '" + new_attribute.fill_method \
                  + "' in table '" + new_table.name + "', attribute '" + new_attribute.name + "'.\n"
            errprint(msg, ERRCODE["SEMANTIC"])
            
            
    elif method == 'fm_textbank':
        if not attr.data_type in ("VARCHAR", "CHAR"):        
        
            msg = "Semantic Error: The given fill method '" + new_attribute.fill_method \
                + "' incompatible with the given data type '" + new_attribute.data_type \
                    + "' in table '" + new_table.name + "', attribute '" + new_attribute.name + "'.\n"
            errprint(msg, ERRCODE["SEMANTIC"])
            
    
    elif method == 'fm_reference':        
        
        global new_table
        global FK_FLAG
        
        string = attr.fill_parameters[0]
        pos = string.find(":")
        
        if pos == -1:       #didn't find the colon
            msg = "Semantic Error: Wrong parameter given to fill method '" + new_attribute.fill_method \
                + "' in table '" + new_table.name + "', attribute '" + new_attribute.name + "'.\n"
            errprint(msg, ERRCODE["SEMANTIC"])
        
        new_table.fk = True                   #sets the flag that table contains a foreign key
        attr.constraint_flag = True
        attr.constraint_type = "foreign_key"
        attr.fk_table = string[0:pos]     #gets what is before the colon
        attr.fk_attribute = string[(pos+1):]


##
#function to check if the fm_method is used in combination with allowed data types
##
def check_regex_compatibility(attr):
    
    if not attr.data_type in ("VARCHAR", "CHAR", "INT"):        
        
        msg = "Semantic Error: The given fill method '" + new_attribute.fill_method \
               + "' incompatible with the given data type '" + new_attribute.data_type \
                  + "' in table '" + new_table.name + "', attribute '" + new_attribute.name + "'.\n"
        errprint(msg, ERRCODE["SEMANTIC"])



##
#---------THE PARSER------------
## takes f - file descriptor

def dsl_parser(f):
    
    
    
    

    #----LEXER PART-------

    #list of reserved words
    reserved = {
        'TABLE' : 'TABLE',
        'TYPE' : 'TYPE',
        'FILL' : 'FILL',
        'CONSTRAINT' : 'CONSTRAINT',
        
        'unique' : 'CONSTR_NOPARAM',
        'primary_key' : 'CONSTR_NOPARAM',
        'foreign_key' : 'CONSTR_NOPARAM',
        
        'VARCHAR' : 'TYPE_1PARAM',   #CHARACTER VARYING
        'BIT' :     'TYPE_1PARAM', 
        'CHAR' : 'TYPE_1PARAM',      #CHARACTER
        'BOOLEAN' : 'TYPE_NOPARAM',      #BOOL
        'INT' : 'TYPE_NOPARAM',          #INT, INT4
        
        'fm_basic' : 'FILL_METHOD_NOPARAM',
        'fm_regex' : 'FILL_METHOD_1PARAM',
        'fm_textbank' : 'FILL_METHOD_1PARAM',
        'fm_reference' : 'FILL_METHOD_1PARAM',
        
    }

    # List of token names.   This is always required
    tokens = [
        'IDENTIFIER',
        'NUMBER',
        'DOUBLE_COLON',
        'COLON',
        'EOL',
        'LPAREN',
        'RPAREN',
        'REGEX',
        'PATH',
    ] + list(reserved.values())
    
    literals = [ ',' ]

    # Tokens
    t_DOUBLE_COLON   = r'\:\:'
    t_COLON  = r'\:'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    
    
    # A rule for regular expressions
    def t_REGEX(t):
        r'r\'[ 0-9A-Za-z#$%=@!{},`~&*()<>?.:;_|^/+\t\r\n\[\]"-]*\''
        return t

    # A rule for Identifier tokens
    def t_IDENTIFIER(t):
        r'[a-zA-Z][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
        return t

    # A regular expression rule for numbers
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)    
        return t

    # A rule for New Line - to tokenize and count as well
    def t_EOL(t):
        r'\n'
        t.lexer.lineno += len(t.value)
        return t
    
    # A rule for file path
    def t_PATH(t):
        r'[a-zA-Z_0-9/\-\.]+'
        return t
    
    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        print ("Illegal character '%s' at line '%s'" %(t.value[0], t.lineno))
        
        global err
        err = True    #sets the flag

        t.lexer.skip(1)
        
    # Build the lexer
    lexer = lex.lex(reflags=re.IGNORECASE)  #will be case insensitive

    
            
    #input_lex(lexer, f.read())
    #f.seek(0)
    
    
    global err
    if err:
        exit()




    #------PARSER PART--------

    #Rules
    
    def p_dsl(p):
        'dsl : tableBlock moreBlocks'        
        debug("dsl")
        

    def p_moreBlocks(p):
        '''moreBlocks : moreBlocks tableBlock
                      | empty'''
                      
        global new_table
        global attr_list        
        new_table.attr_list = attr_list   # adds complete list of attributes
        new_table.count_attributes()      # stores the count of attributes in table.attr_count
        debug("moreBlocks")
        

    def p_tableBlock(p):
        'tableBlock : tableHeader attributeBlock moreAttributes'        
        table_list.append(new_table)
        debug("tableBlock")
                    
    def p_moreAttributes(p): 
        '''moreAttributes : moreAttributes attributeBlock
                          | empty'''
        debug("moreAttributes")
        

    def p_tableHeader(p):
        'tableHeader : TABLE COLON IDENTIFIER LPAREN NUMBER RPAREN endline'
        
        global new_table
        new_table = table.Table() # creates new table instance
        new_table.fill_count = p[5]
        new_table.name = p[3]     # coresponds to the IDENTIFIER token
        
        global attr_list
        attr_list = []            # inicializes empty list for this table
        debug("tableHeader")
        

    def p_attributeBlock(p):
        '''attributeBlock : attributeName dataType fillMethod
                          | attributeName dataType fillMethod constraintPart'''
        
        global new_attribute
        global attr_list        
        attr_list.append(new_attribute)       #appends the new attribute
        new_attribute.constraint_flag = False #nulls the flag
        debug("attributeBlock")
        

    def p_attributeName(p):
        'attributeName : DOUBLE_COLON IDENTIFIER endline'
        
        global new_attribute
        new_attribute = table.Attribute()   #new attribute instance
        new_attribute.name = p[2]
        debug("attributeName")
        

    def p_dataType(p):
        'dataType : TYPE dtypes endline'
        debug("dataType")
    
    
    def p_dtypes(p):
        '''dtypes : TYPE_NOPARAM
                  | TYPE_1PARAM LPAREN NUMBER RPAREN'''
                  
        global new_attribute
        new_attribute.data_type = p[1]
        new_attribute.parameters = []             #inicializes to no parameters
        
        if len(p) == 5:                           #stands for "DTYPE (1_param)"
            new_attribute.parameters.append(p[3]) #appends the parameter
            
        debug("dtypes")
        

    def p_fillMethod(p):
        '''fillMethod : FILL FILL_METHOD_NOPARAM LPAREN RPAREN endline
                      | FILL FILL_METHOD_1PARAM LPAREN parameter RPAREN endline'''
        
        global new_attribute
        global new_table
        new_attribute.fill_method = p[2].lower()    #lower case to be sure
        debug("fillMethod")
        
        if len(p) == 7:     #one parameter
            new_attribute.fill_parameters = []          #clears the list
            new_attribute.fill_parameters.append(p[4])
            
            
        #check validity of parameters
        check_valid(new_attribute)
        
    def p_constraintPart(p):
        '''constraintPart : CONSTRAINT CONSTR_NOPARAM endline'''
        
        global new_attribute
        
        if p[2] == "foreign_key":
            
            if new_attribute.constraint_type != "foreign_key":      #this means the given fill method doesn't correspond
                
                msg = "Semantic Error: Foreign key constraint stated but wrong fill method '" + new_attribute.fill_method \
                + "' given.\n"
                errprint(msg, ERRCODE["SEMANTIC"])


    def p_parameters(p):
        '''parameters : parameters parameter
                      | empty'''
        debug("parameters")
                    
    def p_parameter(p):
        '''parameter : PATH
                     | REGEX
                     | IDENTIFIER
                     | IDENTIFIER COLON IDENTIFIER'''
        p[0] = p[1]                 #returns the value in p[0]
        debug("parameter")
        
        if len(p) == 4:      #IDENTIFIER COLON IDENTIFIER variant
            p[0] = p[1] + ":" + p[3]   #concatenates so it can be passed together
        
        
    def p_endline(p):
        'endline : EOL extraEndline'
        debug("endline")
        
    def p_extraEndline(p):
        '''extraEndline : EOL extraEndline
                        | empty'''
        debug("extraEndline")
        
        
    def p_empty(p):
        'empty :'
        pass
        
        
    def p_error(p): 
        print("Syntax error. Trouble with " + repr(str(p.value)) + " on line " + str(p.lineno))
        
        global err
        err = True     #sets the flag
        #print "Bad function call at line", p.lineno(1)

    #build parser
    yacc.yacc()
    
    #parse the given file
    yacc.parse(f.read())
    
    if err:
        exit()
        
    
    return table_list  #returns the tables we've recognized
    
    
    
    



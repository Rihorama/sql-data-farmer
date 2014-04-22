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
name_dict = {}       #dictionary that helps reach table object by its name
new_table = None

#attribute variables
attr_list = []
new_attribute = None
param_list = []

alter_table = None
alter_attr = None


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
#---------THE PARSER------------
## takes f - file descriptor

def sql_parser(f):
    
    
    
    

    #----LEXER PART-------

    #list of reserved words
    reserved = {
        'CREATE' : 'CREATE',     
        'TABLE' : 'TABLE',
        'ALTER' : 'ALTER',
        'ONLY' : 'ONLY',
        'CONSTRAINT' : 'CONSTRAINT',
        'REFERENCES' : 'REFERENCES',
        'ADD' : 'ADD',
        
        'bigint' : 'DTYPE_SOLO',        #SOLO: this word alone is a data type
        'bigserial' : 'DTYPE_SOLO',
        'bit' : 'DTYPE_BOTH_1PARAM',    #BOTH: can be either solo or PART1
        'varying' : 'DTYPE_PART2',      #PART2: second part of a two-word data type
        'boolean' : 'DTYPE_SOLO',
        'box' : 'DTYPE_SOLO',
        'bytea' : 'DTYPE_SOLO',
        'character' : 'DTYPE_BOTH_1PARAM', #1PARAM: one mandatory parameter
        'cidr' : 'DTYPE_SOLO',
        'circle' : 'DTYPE_SOLO',
        'date' : 'DTYPE_SOLO',
        'double' : 'DTYPE_PART1',
        'precision' : 'DTYPE_PART2',
        'inet' : 'DTYPE_SOLO',
        'integer' : 'DTYPE_SOLO',
        'interval' : 'DTYPE_2PARAM',    #2PARAM: two mandatory parameters
        'line' : 'DTYPE_SOLO',
        'lseg' : 'DTYPE_SOLO',
        'macaddr' : 'DTYPE_SOLO',
        'money' : 'DTYPE_SOLO',
        'numeric' : 'DTYPE_SOLO_1PARAM2',    #1PARAM2: One mandatory set of two params
        'path' : 'DTYPE_SOLO',
        'point' : 'DTYPE_SOLO',
        'polygon' : 'DTYPE_SOLO',
        'real' : 'DTYPE_SOLO',
        'smallint' : 'DTYPE_SOLO',
        'serial' : 'DTYPE_SOLO',
        'text' : 'DTYPE_SOLO',
        'time' : 'DTYPE_1PARAM',       #NOTE: time and timestamp not allowing "with/without
        'timestamp' : 'DTYPE_SOLO',    #      time zone" at the moment
        'tsquery' : 'DTYPE_SOLO',
        'tsvector' : 'DTYPE_SOLO',
        'txid_snapshot' : 'DTYPE_SOLO',
        'uuid' : 'DTYPE_SOLO',
        'xml' : 'DTYPE_SOLO',
        
        'NOT' : 'NOT',
        'NULL': 'NULL',         #stands for part 2 or solo
        'PRIMARY' : 'PRIMARY',
        'FOREIGN' : 'FOREIGN',
        'KEY' : 'KEY',
        'UNIQUE' : 'UNIQUE',
        
    }

    # List of token names.   This is always required
    tokens = [
        'IDENTIFIER',
        'NUMBER',
        'EOL',
        'LPAREN',
        'RPAREN',
        'SEMICOLON',
        'COMMA',
    ] + list(reserved.values())
    
    # Tokens
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_SEMICOLON = r';'
    t_COMMA = r','
    
    
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
    
    # A string containing ignored characters (spaces, tabs and newlines)
    t_ignore  = ' \t\n'

    # Error handling rule
    def t_error(t):
        print ("Not supported character '%s' at line '%s'" %(t.value[0], t.lineno))
        
        global err
        err = True    #sets the flag

        t.lexer.skip(1)
        
    # Build the lexer
    lexer = lex.lex()  #will be case insensitive

    
            
    #input_lex(lexer, f.read())
    #f.seek(0)
    
    
    global err
    if err:
        exit()




    #------PARSER PART--------

    #Rules
    
    def p_root(p):
        'root : tableBlock moreBlocks moreAlterBlocks'        
        debug("dsl")
        

    def p_moreBlocks(p):
        '''moreBlocks : moreBlocks tableBlock
                      | empty'''
        debug("moreBlocks")
        
        global table_list
        global new_table
        
        table_list.append(new_table)
        

    def p_tableBlock(p):
        'tableBlock : tableHeader attributeBlock moreAttributes SEMICOLON'        
        debug("tableBlock")
        
                    
    def p_moreAttributes(p): 
        '''moreAttributes : moreAttributes attributeBlock
                          | empty'''
        debug("moreAttributes")
        

    def p_tableHeader(p):
        'tableHeader : CREATE TABLE IDENTIFIER LPAREN'
        debug("tableHeader")
        
        global new_table
        global name_dict
        
        new_table = table.Table() # creates new table instance
        new_table.name = p[3]
        
        name_dict[new_table.name] = new_table
        

    def p_attributeBlock(p):
        '''attributeBlock : IDENTIFIER dtypes COMMA
                          | IDENTIFIER dtypes constraintPart COMMA
                          | IDENTIFIER dtypes RPAREN
                          | IDENTIFIER dtypes constraintPart RPAREN'''
        debug("attributeBlock")
        
        global new_table
        global new_attribute
        
        new_attribute.name = p[1]
        new_table.attr_list.append(new_attribute)

    
    
    def p_dtypes(p):
        '''dtypes : dtypeSolo
                  | dtypeTwopart'''
            
        debug("dtypes")
        
        global new_attribute
        global param_list      #inicializes param_list
        
        new_attribute = table.Attribute()
        new_attribute.data_type = p[1]
        new_attribute.parameters = param_list 
        
    
    
    def p_dtypeSolo(p):
        '''dtypeSolo : DTYPE_SOLO
                     | DTYPE_BOTH_1PARAM
                     | DTYPE_BOTH_1PARAM LPAREN parameter RPAREN
                     | DTYPE_SOLO_1PARAM2 LPAREN parameter COMMA parameter RPAREN'''
        debug("dtypeSolo")
        
        p[0] = p[1]
        
        global param_list
        param_list = []   #inicializes param_list
        
        if len(p) == 5:   #variant: DTYPE_BOTH_1PARAM LPAREN parameter RPAREN
            param_list.append(p[3])
            
        elif len(p) == 7: #variant: DTYPE_SOLO_1PARAM2 LPAREN parameter COMMA parameter RPAREN 
            param_list.append(p[3])
            param_list.append(p[5])
            
            
    
    def p_dtypeTwopart(p):
        '''dtypeTwopart : DTYPE_BOTH_1PARAM DTYPE_PART2
                        | DTYPE_PART1 DTYPE_PART2
                        | DTYPE_BOTH_1PARAM DTYPE_PART2 LPAREN parameter RPAREN'''
        debug("dtypeTwopart")
        
        p[0] = p[1] + ' ' + p[2]      #creates one string from the two-part name
        
        global param_list
        param_list = []
        
        if len(p) == 6:   #variant: DTYPE_BOTH_1PARAM DTYPE_PART2 LPAREN parameter RPAREN
            param_list.append(p[4])
    
    
    
    def p_constraintPart(p):
        '''constraintPart : constraintPart constraints
                          | empty'''
        debug("constraintPart")
                          
                          
    def p_constraints(p):
        '''constraints : NOT NULL
                       | NULL
                       | UNIQUE'''
        debug("constraints")
        
        if len(p) == 3:
            constr = p[1] + ' ' + p[2]
        else:
            constr = p[1]
        
        global new_attribute
        new_attribute.constraint_flag = True
        new_attribute.constraint_cnt += 1    #increments the cnt
        new_attribute.set_constraint(constr)

                   
                    
    def p_parameter(p):
        '''parameter : NUMBER'''        
        debug("parameter")
        
        p[0] = p[1]

    
    
    
    
    def p_moreAlterBlocks(p):
        '''moreAlterBlocks : moreAlterBlocks alterBlock
                           | empty'''

        debug("moreAlterBlocks")
        

    def p_alterBlock(p):
        'alterBlock : alterHeader alterBody SEMICOLON'        

        debug("alterBlock")
        
        
    def p_alterHeader(p):
        'alterHeader : ALTER TABLE ONLY IDENTIFIER'
        debug("alterHeader")
        
        global alter_table
        if not p[4] in name_dict.keys():
            msg = "Input error: Table '" + p[10] + "'given in ALTER part couldn't be found.\n"
            errprint(msg, ERRCODE["INPUT"])
        alter_table = name_dict[p[4]]
        
        
    def p_alterBody(p):
        '''alterBody : ADD CONSTRAINT IDENTIFIER PRIMARY KEY LPAREN IDENTIFIER RPAREN
                     | ADD CONSTRAINT IDENTIFIER FOREIGN KEY LPAREN IDENTIFIER RPAREN REFERENCES IDENTIFIER LPAREN IDENTIFIER RPAREN'''        
        debug("alterBody")
        
        global alter_attr
        global alter_table
        
        alter_attr = None
        constr = p[4] + ' ' + p[5]
        
        for attr in alter_table.attr_list:
            if attr.name == p[7]:     #p[7] stands for the attribute name in both cases
                alter_attr = attr
                break
        
        #did we find anything?
        if alter_attr == None:
            msg = "Input error: Couldn't find the given attribute name '" + p[7] \
                    + "' in the list of attributes of table '" + alter_table.name \
                    + "' while processing a " + constr + ".\n"
            errprint(msg, ERRCODE["INPUT"]) 
         
         
        alter_attr.constraint_flag = True
        alter_attr.constraint_cnt += 1    #increments the cnt
        alter_attr.set_constraint(constr)      
        
        #for foreign key
        if p[4] == 'FOREIGN':
            
            #existence of foreign table check
            if not p[10] in name_dict.keys():
                msg = "Input error: Foreign table '" + p[10] + "' couldn't be found.\n"
                errprint(msg, ERRCODE["INPUT"])       
                
            alter_attr.fk_table = name_dict[p[10]]  #gets the foreign table object
            
            for attr in alter_attr.fk_table.attr_list:
                if attr.name == p[12]:
                    alter_attr.fk_attribute = attr
                    break
            
            #existence of foreign attribute check
            if alter_attr.fk_attribute == None:
                msg = "Input error: Foreign attribute '" + p[12] \
                        + "' couldn't be found in table '" + p[10] \
                        + "' while processing a " + constr + ".\n"
                errprint(msg, ERRCODE["INPUT"])       
        
        
        
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
    
    
    
    



#!/usr/bin/python


import sys
import ply.lex as lex
import ply.yacc as yacc
import class_table as table


sys.path.insert(0,"../..")


#table variables
table_list = []
new_table = None

attr_list = []
new_attribute = None
    

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

def dsl_parser(f):
    
    
    
    

    #----LEXER PART-------

    #list of reserved words
    reserved = {
        'TABLE' : 'TABLE',
        'TYPE' : 'TYPE',
        'FILL' : 'FILL',
        'CONSTRAINT' : 'CONSTRAINT'
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
    ] + list(reserved.values())

    # Tokens
    t_DOUBLE_COLON   = r'\:\:'
    t_COLON  = r'\:'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'

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

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        print ("Illegal character '%s' at line '%s'" % t.value[0], t.lineno)
        t.lexer.skip(1)
        
    # Build the lexer
    lexer = lex.lex()

    '''
    data = TABLE:tabulka(50)
            ::atribut
            TYPE sedm
            FILL ahaha()
            
    input_lex(lexer, f.read())'''
    




    #------PARSER PART--------

    #Rules
    
    def p_dsl(p):
        'dsl : tableBlock moreBlocks'        
        for table in table_list:
            table.print_table()
        

    def p_moreBlocks(p):
        '''moreBlocks : moreBlocks tableBlock
                      | empty'''
                      
        global new_table
        global attr_list        
        new_table.attr_list = attr_list   #adds complete list of attributes
        

    def p_tableBlock(p):
        'tableBlock : tableHeader attributeBlock moreAttributes'        
        table_list.append(new_table)
        
                    
    def p_moreAttributes(p): 
        '''moreAttributes : moreAttributes attributeBlock
                          | empty'''  
        

    def p_tableHeader(p):
        'tableHeader : TABLE COLON IDENTIFIER LPAREN NUMBER RPAREN endline'
        
        global new_table
        new_table = table.Table() # creates new table instance
        new_table.name = p[3]     # coresponds to the IDENTIFIER token
        
        global attr_list
        attr_list = []            # inicializes empty list for this table
        

    def p_attributeBlock(p):
        'attributeBlock : attributeName dataType fillMethod'
        
        global new_attribute
        global attr_list        
        attr_list.append(new_attribute)
        

    def p_attributeName(p):
        'attributeName : DOUBLE_COLON IDENTIFIER endline'
        
        global new_attribute
        new_attribute = table.Attribute()   #new attribute instance
        new_attribute.name = p[2]
        

    def p_dataType(p):
        'dataType : TYPE IDENTIFIER endline'
        
        global new_attribute
        new_attribute.data_type = p[2]
        

    def p_fillMethod(p):
        'fillMethod : FILL IDENTIFIER LPAREN parameters RPAREN endline'
        

    def p_parameters(p):
        '''parameters : parameters parameter
                      | empty'''
        
                    
    def p_parameter(p):
        'parameter : IDENTIFIER'
        
        
    def p_endline(p):
        'endline : EOL extraEndline'
        
    def p_extraEndline(p):
        '''extraEndline : EOL extraEndline
                        | empty'''
        
        
    def p_empty(p):
        'empty :'
        pass
        
        
    def p_error(p): 
        print("Syntax error. Trouble with " + repr(str(p.value)) + " on line " + str(p.lineno))

    #build parser
    yacc.yacc()
    
    #parse the given file
    yacc.parse(f.read())
    
    
    
    



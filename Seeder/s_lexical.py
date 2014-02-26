"""f = file descriptor"""

import token_class, sys

TOKEN_LIST = list()  #list of tokens
LINE_COUNTER = 1     #keeps the no. of currently parsed line


def lex_parse (f):
  
  char = f.read(1)               #first character 
  while(char):
    
    if(char.isalpha()):
      f.seek(-1,1)               #returns fd to just read position
      token_identifier(f)        #function to handle identifier tokens
      
    elif(char.isdigit()):
      f.seek(-1,1)               #returns fd to just read position
      token_number(f)            #function to handle number tokens
      
    elif(char == '\n' or char == '\r'):
      f.seek(-1,1)               #returns fd to just read position
      token_endline(f)           #function to handle endline tokens
      
    elif(char == ':'):
      token_colon(f)             #function to handle colon tokens
      
    elif(char == '('):
      token = token_class.Token()            #token object
      token.set_type('L_BRACKET')            #sets token type
      token.set_value('(')                   #sets the value
      token.set_line(LINE_COUNTER) #sets the line
      TOKEN_LIST.append(token)
      
    elif(char == ')'):
      token = token_class.Token()            #token object
      token.set_type('R_BRACKET')            #sets token type
      token.set_value(')')                   #sets the value
      token.set_line(LINE_COUNTER) #sets the line
      TOKEN_LIST.append(token)
      
    elif(char == ' '):
      pass
    
    else:
      lexical_error(char)
      
      
    char = f.read(1)
  
  for token in TOKEN_LIST:
    print(token.token_type, token.token_value, token.token_line)
    
    
    
###------------
###---IDENTIFIER
###-----------
def token_identifier(f):
  
  token = token_class.Token()            #token object
  value = ""
  
  while(1):
    char = f.read(1)
    
    if(char.isalpha() or char.isdigit() or char == '_'):
      value = value + char
      
    else:
      if(char):                    #only if we didn't reach EOF
        f.seek(-1,1)               #returns fd to the just-read position
      
      if(value == 'TABLE'):
	token.set_type('TABLE')
      
      elif(value == 'TYPE'):
	token.set_type('TYPE')
	
      elif(value == 'FILL'):
	token.set_type('FILL')
	
      elif(value == 'CONSTRAINT'):
	token.set_type('CONTRAINT')
      
      elif(value == 'FILTER'):
	token.set_type('FILTER')
	
      elif(value == 'ASSERT'):
	token.set_type('ASSERT')
	
      else:
        token.set_type('IDENTIFIER')   #sets token type
        
      token.set_value(value)       #sets the value
      token.set_line(LINE_COUNTER) #sets the line
      TOKEN_LIST.append(token)     #adds to the list
      return

    
###------------
###---NUMBER
###-----------
def token_number(f):
  
  token = token_class.Token()            #token object
  value = ""
  
  while(1):
    char = f.read(1)
    
    if(char.isdigit()):
      value = value + char
      
    else:
      if(char):                    #only if we didn't reach EOF
        f.seek(-1,1)               #returns fd to the just-read position
      
      token.set_type('NUMBER')   #sets token type
      token.set_value(value)       #sets the value
      token.set_line(LINE_COUNTER) #sets the line
      TOKEN_LIST.append(token)     #adds to the list
      return



###------------
###---COLON
###-----------
def token_colon(f):
  
  token = token_class.Token()            #token object
  value = ":"                            #one colon for sure
  char = f.read(1)
  
  if(char == ':'):              #is it double colon?
    value = "::"
    token.set_type('DOUBLE_COLON')   #sets token type
  
  else:
    if(char):                    #only if we didn't reach EOF
      f.seek(-1,1)               #returns fd to the just-read position
    token.set_type('COLON')   #sets token type
  
  token.set_value(value)       #sets the value
  token.set_line(LINE_COUNTER) #sets the line
  TOKEN_LIST.append(token)     #adds to the list
  
  
  
###------------
###---ENDLINE
###-----------  
def token_endline(f):
  
  global LINE_COUNTER
  
  token = token_class.Token()            #token object
  value = ""
  char = f.read(1)
  
  if(char == '\n'):              #is it double colon?
    value = char
  
  elif(char == '\r'):
    char = f.read(1)
    
    if(char == '\n'):
      value = "\r\n"
      
    else:
      lexical_error('\r')     
      
  token.set_type('ENDLINE')    #sets token type
  token.set_value(value)       #sets the value
  token.set_line(LINE_COUNTER) #sets the line
  TOKEN_LIST.append(token)     #adds to the list
  
  LINE_COUNTER = LINE_COUNTER + 1
  
  
###------------
###---LEXICAL ERROR
###-----------
def lexical_error(char):
  print("Lexical error at line " + str(LINE_COUNTER) + "! Unsuported char: \'" + char + "\'")
  sys.exit()

  
  
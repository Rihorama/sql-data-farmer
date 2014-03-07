import ply.lex as lex



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
    'NEWLINE',
    'L_PAREN',
    'R_PAREN'
] + list(reserved.values())


def build_lex():
    # Regular expression rules for simple tokens
    t_DOUBLE_COLON   = r'\:\:'
    t_COLON  = r'\:'
    t_L_PAREN  = r'\('
    t_R_PAREN  = r'\)'

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
    def t_NEWLINE(t):
        r'\n'
        t.lexer.lineno += len(t.value)
        return t

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    # Build the lexer
    #global LEXER
    lexer = lex.lex()
    return lexer



##
#takes the file descriptor, converts the file to a string and feed the lexer
##
def input_lex(lexer, f):
  
    data = f.read() #reads the file to string
  
    lexer.input(data)
  
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print tok
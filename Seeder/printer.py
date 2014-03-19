import sys


#TODO: check the syntax ret val
ERRCODE = {
    "OK" : 0,
    "LEXICAL" : 1,
    "SYNTACTIC" : 2,
    "SEMANTIC" : 3,
    }
          






##
#Debug printer
##
def debug(msg):

    #print msg
    pass



##
#ERROR printer
##
def errprint(message,ret_value):

    sys.stderr.write(message)
    sys.exit(ret_value)
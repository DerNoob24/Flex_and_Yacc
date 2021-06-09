import ply.yacc as yacc
from Flex_and_Yacc_Python.tokens.tokens import tokens
from Flex_and_Yacc_Python.syntax.rules.expressions import *
from Flex_and_Yacc_Python.syntax.rules.terms import *
from Flex_and_Yacc_Python.syntax.rules.variables import *
from Flex_and_Yacc_Python.syntax.rules.conditions import *

# Error handling


def p_error(p):
    if p is not None:
        print("Syntax error on line " + str(p.lineno) +
              " at position " + str(p.lexpos) + "\n")


parser = yacc.yacc(debug=True)

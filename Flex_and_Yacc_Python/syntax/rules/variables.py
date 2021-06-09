from Flex_and_Yacc_Python.syntax.rules.saved_variables import saved_variables


def p_variable_int(p):
    '''variable : INTEGER CHARS ASSIGNMENT expression'''
    if type(p[4]) is not int:
        wrong_assignment_error(p)
    saved_variables.update({p[2]: int(p[4])})
    print(saved_variables)


def p_variable_string(p):
    'variable : STRING CHARS ASSIGNMENT expression'
    if type(p[4]) is not str:
        wrong_assignment_error(p)
    saved_variables.update({p[2]: p[4].strip("'\"")})
    print(saved_variables)


def p_variable_bool(p):
    '''variable : BOOLEAN CHARS ASSIGNMENT TRUE
                | BOOLEAN CHARS ASSIGNMENT FALSE'''
    saved_variables.update({p[2]: p[4] == "true"})
    print(saved_variables)


def p_variable_varConcat(p):
    'variable : CHARS ASSIGNMENT expression'
    if not (p[1] in saved_variables and type(p[3]) == type(saved_variables[p[1]])):
        if not (type(p[3]) is float and type(saved_variables[p[1]] is (float or int))):
            wrong_reassignment_error(p)

    savedVariableType = type(saved_variables[p[1]])
    if savedVariableType is str:
        saved_variables.update({p[1]: p[3].strip("'\"")})
    elif savedVariableType is int:
        saved_variables.update({p[1]: int(p[3])})
    elif savedVariableType is float:
        saved_variables.update({p[1]: float(p[3])})

    print(saved_variables)


def p_variable_reassign_bool(p):
    '''variable : CHARS ASSIGNMENT TRUE
                | CHARS ASSIGNMENT FALSE'''
    if not (p[1] in saved_variables and type(saved_variables[p[1]]) is bool):
        wrong_reassignment_error(p)
    saved_variables.update({p[1]: p[3] == "true"})
    print(saved_variables)


def wrong_assignment_error(p):
    print("Wrong dataType for assignment")
    print("Syntax error on line " + str(p.lineno(1)) + "\n")
    raise SyntaxError


def wrong_reassignment_error(p):
    print("Wrong dataType for reassignment")
    print("Syntax error on line " + str(p.lineno(1)) + "\n")
    raise SyntaxError

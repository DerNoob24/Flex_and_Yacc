def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    '''expression : expression MINUS term
                | MINUS term'''
    if len(p) == 4:
        p[0] = p[1] - p[3]
    else:
        p[0] = -1*p[2]


def p_exprossion_increase(p):
    'expression : expression PLUS PLUS'
    p[0] = p[1] + 1


def p_expression_decrease(p):
    'expression : expression MINUS MINUS'
    p[0] = p[1] - 1


def p_expression_braces(p):
    'expression : ROUND_START expression ROUND_END'
    p[0] = (p[2])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_expression_variable(p):
    'expression : variable'
    p[0] = p[1]


def p_expression_int(p):
    'expression : INTEGER'
    print("I am a int")


# IF ELSE STATEMENT

def p_if_statement(p):
    'expression : IF ROUND_START condition ROUND_END CURLY_START expression CURLY_END'
    if p[3]:
        p[0] = p[6]


def p_if_else_statement(p):
    'expression : IF ROUND_START condition ROUND_END CURLY_START expression CURLY_END ELSE CURLY_START expression CURLY_END'
    if p[3]:
        p[0] = p[6]
    else:
        p[0] = p[10]


# FOR STATEMENT geht zwar mehrfach durch macht aber p8 nur einmal und kann nicht mit der laufvariable arbeiten

def p_for_loop(p):
    'expression : FOR ROUND_START CHARS IN NUMBER ROUND_END CURLY_START expression CURLY_END'
    for p[3] in range(p[5]):
        print(p[3])
        p[8]


def p_for_else_loop(p):
    'expression : FOR ROUND_START CHARS IN NUMBER ROUND_END CURLY_START expression CURLY_END ELSE CURLY_START expression CURLY_END'
    for p[3] in range(p[5]):
        print(p[3])
        p[8]
    else:
        p[0] = p[12]


# WHILE STATEMENT
def p_while_loop(p):
    'expression : WHILE ROUND_START condition ROUND_END CURLY_START expression CURLY_END'
    while p[3]:
        p[6]

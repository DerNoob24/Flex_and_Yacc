saved_variables = {}


def getVariable(name, line):
    if name in saved_variables:
        return saved_variables.get(name)
    else:
        print("Varaible not initiated")
        print("Syntax error on line " + str(line) + "\n")
        raise SyntaxError

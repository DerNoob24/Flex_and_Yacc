reserved = {
    'int': 'INTEGER',
    'float': 'FLOAT',
    'string': 'STRING',
    'bool': 'BOOLEAN',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    '==': 'EQUAL',
    '!=': 'NOT_EQUAL',
    'in': 'IN',
    'vars': 'VARS',
    '++': 'INC',
    '--': 'DEC'
}

tokens = [
    'OR',
    'AND',
    'ASSIGNMENT',
    'PLUS',
    'MULTIPLICATION',
    'DIVISION',
    'MODULO',
    'MINUS',
    'INVERSE',
    'RIGHT_GREATER',
    'LEFT_GREATER',
    'CHARS',
    'QUOTED_CHARS',
    'NUMBER',
    'ROUND_START',
    'ROUND_END',
    'CURLY_START',
    'CURLY_END',
    'COMMENT',
    'SEMICOLON'
] + list(reserved.values())
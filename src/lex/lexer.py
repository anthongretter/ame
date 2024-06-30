import ply.lex as lex


reserved = {
    'def': "DEF",
    'if': "IF",
    'else': "ELSE",
    'print': "PRINT",
    'for': "FOR",
    'int': "INT",
    'float': "FLOAT",
    'string': "STRING",
    'read': "READ",
    'return': "RETURN",
    'call': "CALL"
}

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'ASSIGN',
    'EQUAL',
    'DIFF',
    'GREATER',
    'GREATEREQUAL',
    'LESS',
    'LESSEQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'SEMICOLON',
    'INT_CONSTANT',
    'STRING_CONSTANT',
    'FLOAT_CONSTANT',
    'ID'
) + tuple(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LESS = r'<'
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_DIFF = r'\!='
t_ASSIGN = r'='
t_EQUAL = r'=='
t_MOD = r'\%'

# To ignore
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

def t_INT_CONSTANT(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t


def t_FLOAT_CONSTANT(t):
    r'[+-]?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_STRING_CONSTANT(t):
    r"'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\""
    t.value = str(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caractere {t.value[0]} desconhecido em {t.lexer.lineno},{t.lexer.col_offset}")


lexer = lex.lex()

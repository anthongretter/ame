#
#   COMPILADOR DA LINGUAGEM AME (BASEADA EM X++ - src/resources/ConvCC-2024-1.txt)
#   DISCIPLINA INE5426 - CONSTRUÇÃO DE COMPILADORES - 2024/1
#   
#   Autores: 
#   A - Anthon Porath Gretter (20204787)
#   M - Matheus Antonio de Souza (21203363)
#   E - Eduardo de Moraes (19203167)
#
#   MODIFICAÇÕES DA GRAMÁTICA:
#   1 - Toda chamada de função é precedida pela palavra reservada "call" - Ex: x = call funcao(parametro);
#   2 - Todo return deve retornar um identificador - Ex: return x;
#
import ply.lex as lex

SEPS = {'+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=',
        '(', ')', '{', '}', '[', ']', ',', ';'}

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
    'call': "CALL",
    'new': "NEW",
    'null': "NULL",
    'break': "BREAK"
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
    'SEMICOLUMN',
    'INT_CONSTANT',
    'STRING_CONSTANT',
    'FLOAT_CONSTANT',
    'IDENT'
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
t_SEMICOLUMN = r'\;'
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
    r'[-]?\d+'
    t.value = int(t.value)
    return t


def t_FLOAT_CONSTANT(t):
    r'[-]?\d+\.\d*'
    t.value = float(t.value)
    return t


def t_STRING_CONSTANT(t):
    r"'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\""
    t.value = str(t.value)
    return t


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.linestart = t.lexer.lexpos

def t_error(t):
    print(f"ERRO: Caractere {t.value[0]} desconhecido na linha {t.lexer.lineno} coluna {t.lexer.lexpos - t.lexer.linestart + 1}")
    quit()

lexer = lex.lex()
lexer.linestart = 0


TABELA : dict = {'PROGRAM': {'$': ('&',), 'if': ('STATEMENT',), 'comma': '-', 'read': ('STATEMENT',), 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': ('STATEMENT',), 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': ('STATEMENT',), 'break': ('STATEMENT',), 'ident': ('STATEMENT',), 'semicolumn': ('STATEMENT',), 'divide': '-', 'float_constant': '-', 'return': ('STATEMENT',), 'equal': '-', 'rparen': '-', 'string': ('STATEMENT',), 'lbracket': '-', 'minus': '-', 'def': ('FUNCLIST',), 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': ('STATEMENT',), 'rbracket': '-', 'for': ('STATEMENT',), 'float': ('STATEMENT',), 'less': '-', 'greaterequal': '-', 'times': '-'}, 'FUNCLIST': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': ('FUNCDEF', 'FUNCLISTSUF'), 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'FUNCLISTSUF': {'$': ('&',), 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': ('FUNCLIST',), 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'FUNCDEF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': ('def', 'ident', 'lparen', 'PARAMLIST', 'rparen', 'lbrace', 'STATELIST', 'rbrace'), 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'PARAMLIST': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': ('&',), 'string': ('string', 'ident', 'PARAMLISTSUF'), 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': ('int', 'ident', 'PARAMLISTSUF'), 'rbracket': '-', 'for': '-', 'float': ('float', 'ident', 'PARAMLISTSUF'), 'less': '-', 'greaterequal': '-', 'times': '-'}, 'PARAMLISTSUF': {'$': '-', 'if': '-', 'comma': ('comma', 'PARAMLIST'), 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': ('&',), 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'STATEMENT': {'$': '-', 'if': ('IFSTAT', 'semicolumn'), 'comma': '-', 'read': ('READSTAT', 'semicolumn'), 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': ('lbrace', 'STATELIST', 'rbrace'), 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': ('PRINTSTAT', 'semicolumn'), 'break': ('break', 'semicolumn'), 'ident': ('ATRIBSTAT', 'semicolumn'), 'semicolumn': ('semicolumn',), 'divide': '-', 'float_constant': '-', 'return': ('RETURNSTAT', 'semicolumn'), 'equal': '-', 'rparen': '-', 'string': ('VARDECL', 'semicolumn'), 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': ('VARDECL', 'semicolumn'), 'rbracket': '-', 'for': ('FORSTAT', 'semicolumn'), 'float': ('VARDECL', 'semicolumn'), 'less': '-', 'greaterequal': '-', 'times': '-'}, 'VARDECL': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': ('string', 'ident', 'DECAUX'), 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': ('int', 'ident', 'DECAUX'), 'rbracket': '-', 'for': '-', 'float': ('float', 'ident', 'DECAUX'), 'less': '-', 'greaterequal': '-', 'times': '-'}, 'ATRIBSTAT': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': ('LVALUE', 'assign', 'ATRIBSTATSUF'), 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'ATRIBSTATSUF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': ('EXPRESSION',), 'greater': '-', 'null': ('EXPRESSION',), 'lbrace': '-', 'mod': '-', 'new': ('ALLOCEXPRESSION',), 'lparen': ('EXPRESSION',), 'string_constant': ('EXPRESSION',), 'print': '-', 'break': '-', 'ident': ('EXPRESSION',), 'semicolumn': '-', 'divide': '-', 'float_constant': ('EXPRESSION',), 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': ('EXPRESSION',), 'def': '-', 'plus': ('EXPRESSION',), 'lessequal': '-', 'call': ('FUNCCALL',), 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'FUNCCALL': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': ('call', 'ident', 'lparen', 'PARAMLISTCALL', 'rparen'), 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'PARAMLISTCALL': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': ('ident', 'PARAMLISTCALLSUF'), 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'PARAMLISTCALLSUF': {'$': '-', 'if': '-', 'comma': ('comma', 'PARAMLISTCALL'), 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': ('&',), 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'PRINTSTAT': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': ('print', 'EXPRESSION'), 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'READSTAT': {'$': '-', 'if': '-', 'comma': '-', 'read': ('read', 'LVALUE'), 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'RETURNSTAT': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': ('return', 'ident'), 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'IFSTAT': {'$': '-', 'if': ('if', 'lparen', 'EXPRESSION', 'rparen', 'STATEMENT', 'IFSTATSUF'), 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'IFSTATSUF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': ('else', 'STATEMENT'), 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'FORSTAT': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': ('for', 'lparen', 'ATRIBSTAT', 'semicolumn', 'EXPRESSION', 'semicolumn', 'ATRIBSTAT', 'rparen', 'STATEMENT'), 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'STATELIST': {'$': '-', 'if': ('STATEMENT', 'STATEMENTSUF'), 'comma': '-', 'read': ('STATEMENT', 'STATEMENTSUF'), 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': ('STATEMENT', 'STATEMENTSUF'), 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': ('STATEMENT', 'STATEMENTSUF'), 'break': ('STATEMENT', 'STATEMENTSUF'), 'ident': ('STATEMENT', 'STATEMENTSUF'), 'semicolumn': ('STATEMENT', 'STATEMENTSUF'), 'divide': '-', 'float_constant': '-', 'return': ('STATEMENT', 'STATEMENTSUF'), 'equal': '-', 'rparen': '-', 'string': ('STATEMENT', 'STATEMENTSUF'), 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': ('STATEMENT', 'STATEMENTSUF'), 'rbracket': '-', 'for': ('STATEMENT', 'STATEMENTSUF'), 'float': ('STATEMENT', 'STATEMENTSUF'), 'less': '-', 'greaterequal': '-', 'times': '-'}, 'STATEMENTSUF': {'$': '-', 'if': ('STATELIST',), 'comma': '-', 'read': ('STATELIST',), 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': ('STATELIST',), 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': ('STATELIST',), 'break': ('STATELIST',), 'ident': ('STATELIST',), 'semicolumn': ('STATELIST',), 'divide': '-', 'float_constant': '-', 'return': ('STATELIST',), 'equal': '-', 'rparen': '-', 'string': ('STATELIST',), 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': ('&',), 'assign': '-', 'int': ('STATELIST',), 'rbracket': '-', 'for': ('STATELIST',), 'float': ('STATELIST',), 'less': '-', 'greaterequal': '-', 'times': '-'}, 'ALLOCEXPRESSION': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': ('new', 'ALLOCEXPRESSIONSUF'), 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'ALLOCEXPRESSIONSUF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': ('string', 'ALLOCAUX'), 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': ('int', 'ALLOCAUX'), 'rbracket': '-', 'for': '-', 'float': ('float', 'ALLOCAUX'), 'less': '-', 'greaterequal': '-', 'times': '-'}, 'EXPRESSION': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': ('NUMEXPRESSION', 'EXAUX'), 'greater': '-', 'null': ('NUMEXPRESSION', 'EXAUX'), 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': ('NUMEXPRESSION', 'EXAUX'), 'string_constant': ('NUMEXPRESSION', 'EXAUX'), 'print': '-', 'break': '-', 'ident': ('NUMEXPRESSION', 'EXAUX'), 'semicolumn': '-', 'divide': '-', 'float_constant': ('NUMEXPRESSION', 'EXAUX'), 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': ('NUMEXPRESSION', 'EXAUX'), 'def': '-', 'plus': ('NUMEXPRESSION', 'EXAUX'), 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'NUMEXPRESSION': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': ('TERM', 'NUMAUX'), 'greater': '-', 'null': ('TERM', 'NUMAUX'), 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': ('TERM', 'NUMAUX'), 'string_constant': ('TERM', 'NUMAUX'), 'print': '-', 'break': '-', 'ident': ('TERM', 'NUMAUX'), 'semicolumn': '-', 'divide': '-', 'float_constant': ('TERM', 'NUMAUX'), 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': ('TERM', 'NUMAUX'), 'def': '-', 'plus': ('TERM', 'NUMAUX'), 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'TERM': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': ('UNARYEXPR', 'TERMSUF'), 'greater': '-', 'null': ('UNARYEXPR', 'TERMSUF'), 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': ('UNARYEXPR', 'TERMSUF'), 'string_constant': ('UNARYEXPR', 'TERMSUF'), 'print': '-', 'break': '-', 'ident': ('UNARYEXPR', 'TERMSUF'), 'semicolumn': '-', 'divide': '-', 'float_constant': ('UNARYEXPR', 'TERMSUF'), 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': ('UNARYEXPR', 'TERMSUF'), 'def': '-', 'plus': ('UNARYEXPR', 'TERMSUF'), 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'TERMSUF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': ('&',), 'int_constant': '-', 'greater': ('&',), 'null': '-', 'lbrace': '-', 'mod': ('mod', 'UNARYEXPR'), 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': ('divide', 'UNARYEXPR'), 'float_constant': '-', 'return': '-', 'equal': ('&',), 'rparen': ('&',), 'string': '-', 'lbracket': '-', 'minus': ('&',), 'def': '-', 'plus': ('&',), 'lessequal': ('&',), 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': ('&',), 'for': '-', 'float': '-', 'less': ('&',), 'greaterequal': ('&',), 'times': ('times', 'UNARYEXPR')}, 'UNARYEXPR': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': ('FACTOR',), 'greater': '-', 'null': ('FACTOR',), 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': ('FACTOR',), 'string_constant': ('FACTOR',), 'print': '-', 'break': '-', 'ident': ('FACTOR',), 'semicolumn': '-', 'divide': '-', 'float_constant': ('FACTOR',), 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': ('minus', 'FACTOR'), 'def': '-', 'plus': ('plus', 'FACTOR'), 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'FACTOR': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': ('int_constant',), 'greater': '-', 'null': ('null',), 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': ('lparen', 'NUMEXPRESSION', 'rparen'), 'string_constant': ('string_constant',), 'print': '-', 'break': '-', 'ident': ('LVALUE',), 'semicolumn': '-', 'divide': '-', 'float_constant': ('float_constant',), 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'LVALUE': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': ('ident', 'LVAUX'), 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'LVAUX': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': ('&',), 'int_constant': '-', 'greater': ('&',), 'null': '-', 'lbrace': '-', 'mod': ('&',), 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': ('&',), 'float_constant': '-', 'return': '-', 'equal': ('&',), 'rparen': ('&',), 'string': '-', 'lbracket': ('lbracket', 'NUMEXPRESSION', 'rbracket', 'LVAUXSUF'), 'minus': ('&',), 'def': '-', 'plus': ('&',), 'lessequal': ('&',), 'call': '-', 'else': '-', 'rbrace': '-', 'assign': ('&',), 'int': '-', 'rbracket': ('&',), 'for': '-', 'float': '-', 'less': ('&',), 'greaterequal': ('&',), 'times': ('&',)}, 'LVAUXSUF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': ('&',), 'int_constant': '-', 'greater': ('&',), 'null': '-', 'lbrace': '-', 'mod': ('&',), 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': ('&',), 'float_constant': '-', 'return': '-', 'equal': ('&',), 'rparen': ('&',), 'string': '-', 'lbracket': ('LVAUX',), 'minus': ('&',), 'def': '-', 'plus': ('&',), 'lessequal': ('&',), 'call': '-', 'else': '-', 'rbrace': '-', 'assign': ('&',), 'int': '-', 'rbracket': ('&',), 'for': '-', 'float': '-', 'less': ('&',), 'greaterequal': ('&',), 'times': ('&',)}, 'DECAUX': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': ('lbracket', 'int_constant', 'rbracket', 'DECAUX'), 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'ALLOCAUX': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': '-', 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': '-', 'string': '-', 'lbracket': ('lbracket', 'NUMEXPRESSION', 'rbracket', 'ALLOCAUXSUF'), 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'ALLOCAUXSUF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': '-', 'int_constant': '-', 'greater': '-', 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': '-', 'rparen': ('&',), 'string': '-', 'lbracket': ('ALLOCAUX',), 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': '-', 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': '-', 'greaterequal': '-', 'times': '-'}, 'EXAUX': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': ('diff', 'NUMEXPRESSION'), 'int_constant': '-', 'greater': ('greater', 'NUMEXPRESSION'), 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': ('equal', 'NUMEXPRESSION'), 'rparen': ('&',), 'string': '-', 'lbracket': '-', 'minus': '-', 'def': '-', 'plus': '-', 'lessequal': ('lessequal', 'NUMEXPRESSION'), 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': '-', 'for': '-', 'float': '-', 'less': ('less', 'NUMEXPRESSION'), 'greaterequal': ('greaterequal', 'NUMEXPRESSION'), 'times': '-'}, 'NUMAUX': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': ('&',), 'int_constant': '-', 'greater': ('&',), 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('&',), 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': ('&',), 'rparen': ('&',), 'string': '-', 'lbracket': '-', 'minus': ('minus', 'TERM', 'NUMAUXSUF'), 'def': '-', 'plus': ('plus', 'TERM', 'NUMAUXSUF'), 'lessequal': ('&',), 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': ('&',), 'for': '-', 'float': '-', 'less': ('&',), 'greaterequal': ('&',), 'times': '-'}, 'NUMAUXSUF': {'$': '-', 'if': '-', 'comma': '-', 'read': '-', 'diff': ('NUMAUX',), 'int_constant': '-', 'greater': ('NUMAUX',), 'null': '-', 'lbrace': '-', 'mod': '-', 'new': '-', 'lparen': '-', 'string_constant': '-', 'print': '-', 'break': '-', 'ident': '-', 'semicolumn': ('NUMAUX',), 'divide': '-', 'float_constant': '-', 'return': '-', 'equal': ('NUMAUX',), 'rparen': ('NUMAUX',), 'string': '-', 'lbracket': '-', 'minus': ('NUMAUX',), 'def': '-', 'plus': ('NUMAUX',), 'lessequal': ('NUMAUX',), 'call': '-', 'else': '-', 'rbrace': '-', 'assign': '-', 'int': '-', 'rbracket': ('NUMAUX',), 'for': '-', 'float': '-', 'less': ('NUMAUX',), 'greaterequal': ('NUMAUX',), 'times': '-'}}
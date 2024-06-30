from src.utils import Singleton
from ply.lex import LexToken
from src.lex.lexer import lexer
from dataclasses import dataclass


@dataclass
class IdLex:
    datatype: str
    value: str
    lineno: int
    index: int

    def __str__(self):
        return f"{self.__class__.__name__}({self.datatype},{self.value},{self.lineno},{self.index})"


class SymbolTable(metaclass=Singleton):

    def __init__(self):
        self.l: list[IdLex] = []

    def add(self, id: IdLex):
        self.l.append(id)

    def __str__(self):
        return "\n".join([str(t) for t in self.l])

    def __contains__(self, item: IdLex) -> bool:
        return item.value in [i.value for i in self.l]


class Lexer:

    @staticmethod
    def read(input: str) -> (list[LexToken], SymbolTable):
        lexer.input(input)
        symtable = SymbolTable()
        tokens = []

        while True:
            tok = lexer.token()

            if not tok: break
            elif tok.type == "IDENT":
                if not tok in symtable:
                    symtable.add(IdLex(None, tok.value, tok.lineno, tok.lexpos))

            tokens.append(tok)

        return tokens, symtable


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
from src.utils import Singleton
from ply.lex import LexToken
from src.lex.lexer import lexer
from dataclasses import dataclass


@dataclass
class IdLex:
    datatype: str
    magnitude: int
    value: str
    lineno: int
    index: int

    def __str__(self):
        return f"{self.__class__.__name__}(data={self.datatype},mag={self.magnitude},vallex={self.value},line={self.lineno},column={self.index})"


class SymbolTable(metaclass=Singleton):

    def __init__(self):
        self.l: list[IdLex] = []

    def add(self, id: IdLex):
        self.l.append(id)

    # Poor performance asf
    def index(self, vallex: str) -> int:
        return [n for n, il in enumerate(self.l) if vallex == il.value][0]

    def addtype(self, vallex: str, type: str):
        self.l[self.index(vallex)].datatype = type

    def addmag(self, vallex: str, mag: int):
        self.l[self.index(vallex)].magnitude = mag

    def get(self, vallex: str) -> IdLex:
        i = self.index(vallex)
        return self.l[i]

    def __str__(self):
        return "\n".join([str(t) for t in self.l])

    def __contains__(self, item: IdLex) -> bool:
        return item.value in [i.value for i in self.l]


class Lexer:

    @staticmethod
    def find_column(inputa, token):
        line_start = inputa.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    @staticmethod
    def read(input: str) -> tuple[list[LexToken], SymbolTable]:
        lexer.input(input)
        symtable = SymbolTable()
        tokens = []

        while True:
            tok = lexer.token()

            if not tok:
                break
            
            tok.lexpos = Lexer.find_column(input, tok)
            if tok.type == "IDENT":
                if not tok in symtable:
                    symtable.add(IdLex(None, 0, tok.value, tok.lineno, tok.lexpos))

            tokens.append(tok)

        return tokens, symtable

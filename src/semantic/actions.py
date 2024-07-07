from src.lex.lexer import reserved
from src.lex.lexicalstructs import SymbolTable
from dataclasses import dataclass


@dataclass
class SemanticAction:
    func: callable
    args: list

    def addcauda(self, c):
        self.args = c

    def __str__(self):
        return f"{self.__class__.__name__}({self.args})"

class DEC:

    @staticmethod
    def a(l):
        SymbolTable().addtype(l[1].vallex, reserved['int'])

    @staticmethod
    def b(l, t):
        SymbolTable().addmag(t[0].vallex, l[2].magnitude)

    @staticmethod
    def c(l, t):
        SymbolTable().addtype(t[0].vallex, reserved['float'])

    @staticmethod
    def d(l, t):
        SymbolTable().addmag(t[0].vallex, l[1].magnitude)

    @staticmethod
    def e(l, t):
        SymbolTable().addtype(t[0].vallex, reserved['string'])

    @staticmethod
    def f(l):
        SymbolTable().addmag(l[0].vallex, l[1].magnitude)

    @staticmethod
    def g(l):
        l[0].magnitude = l[1].magnitude + 1

    @staticmethod
    def h(l):
        l[0].magnitude = 0


class EXPA:
    pass

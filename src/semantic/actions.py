from src.lex.lexer import reserved
from src.lex.lexicalstructs import SymbolTable
from dataclasses import dataclass


@dataclass
class SemanticAction:
    func: callable
    args: list


class DEC:

    @staticmethod
    def a(l):
        SymbolTable().addtype(l[1].vallex, reserved['int'])

    @staticmethod
    def b(l):
        SymbolTable().addmag(l[1].vallex, l[2].magnitude)

    @staticmethod
    def c(l):
        SymbolTable().addtype(l[1].vallex, reserved['float'])

    @staticmethod
    def d(l):
        SymbolTable().addmag(l[0].vallex, l[1].magnitude)

    @staticmethod
    def e(l):
        SymbolTable().addtype(l[0].vallex, reserved['string'])

    @staticmethod
    def f(l):
        SymbolTable().addmag(l[0].vallex, l[1].magnitude)

    @staticmethod
    def g(l):
        l[0].magnitude = l[1].magnitude + 1

    @staticmethod
    def h(l):
        l[0].magnitude = l[1].magnitude + 1

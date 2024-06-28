from dataclasses import dataclass
from utils import Singleton
from constants import *


@dataclass
class LexToken:
    type: str
    lexvalue: str
    line: int
    index: int

    def __str__(self):
        return f"{self.__class__.__name__}({self.type},{self.lexvalue},{self.line},{self.index})"

    def __hash__(self):
        return hash(self.type + self.lexvalue + str(self.line) + str(self.index))


class SymbolTable(Singleton):

    def __init__(self):
        super().__init__(self)
        self.tokens: set[LexToken] = set()

    def add(self, token: LexToken):
        self.tokens.add(token)

    def addraw(self, type: str, lexvalue: str, line: int, index: int):
        self.tokens.add(LexToken(type, lexvalue, line, index))

    def __contains__(self, item):
        return item in self.tokens


# Variáveis globais
tabela_simbolos = SymbolTable()


def print_tabela_simbolos():
    print('Tabela de símbolos:')
    for token in tabela_simbolos.tokens:
        print(token)


with open('exemplo.txt', 'r') as exemplo:
    temp: dict = RESERVED_WORDS_DIAG
    symbol = ""
    index = 0

    for i, line in enumerate(exemplo, 1):
        for char in line:
            index += 1
            symbol += char

            try:
                if char.isdigit():

                temp = temp[char]
            except KeyError:
                # Not found, so it's an ID
                temp = RESERVED_WORDS_DIAG
                look_for_reserved = False
                if char is '"':
                    is_string = True
                    continue

            if is_string:
                if char is '"':
                    SymbolTable().addraw("STRING_CONSTANT", symbol, i, index)

            if char in SEPS:
                if symbol.startswith('"') and symbol.endswith('"'):
                    SymbolTable().addraw("STRING_CONSTAT", symbol, i, index)
                if symbol.startswith("_") or symbol[0].isalpha():
                    SymbolTable().addraw("ID", symbol, i, index)


            # for c in simbolo:
            #     try:
            #         c = RESERVED_WORDS_DIAG[c]
            #     except KeyError:


            # if caractere in ESPACOS or caractere in DELIMITADORES or caractere in OPERADORES:
            #     if simbolo != "":
            #         if not simbolo in PALAVRAS_RESERVADAS:
            #             if not simbolo in tabela_simbolos:
            #                 tabela_simbolos[simbolo] = {i}
            #             else:
            #                 tabela_simbolos[simbolo].add(i)
            #         simbolo = ""
            # elif (caractere.isdigit() and simbolo != "") or caractere.isalpha():
            #     simbolo += caractere

print_tabela_simbolos()

from dataclasses import dataclass
from src.utils import Singleton
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


class SymbolTable(metaclass=Singleton):

    def __init__(self):
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


def which_symbol(lexvalue: str) -> str:
    print(lexvalue)
    if lexvalue.startswith('"') or lexvalue.startswith("'"):
        return "STRING_CONSTANT"

    elif lexvalue[0].isdigit():
        try:
            int(lexvalue)
            return "INT_CONSTANT"
        except ValueError:
            float()
            return "STRING_CONSTANT"

    return "ID"


with open('../test/exemplo.txt', 'r') as exemplo:
    trie: dict = RESERVED_WORDS_DIAG
    look_for_reserved = True
    symbol = ""
    index = 0

    for i, line in enumerate(exemplo, 1):
        for char in line:

            if look_for_reserved:
                try:
                    trie = trie[char]
                    index += 1
                    symbol += char
                    continue
                except KeyError:
                    # Found
                    if "$" in trie.keys():
                        SymbolTable().addraw(trie["$"], symbol, i, index)
                        look_for_reserved = False
                        symbol = ""

                        if char in SEPS:
                            trie = trie[char]
                            look_for_reserved = True

                    trie = RESERVED_WORDS_DIAG

            if char in [" ", "\n"]:
                if symbol == "":
                    continue
                else:
                    type = which_symbol(symbol)
                    SymbolTable().addraw(type, symbol, i, index)
                    symbol = ""

            else:
                index += 1
                symbol += char

                if char in SEPS:
                    trie = trie[char]
                    look_for_reserved = True
                    symbol = ""

                # if symbol == "":
                #     # if char in [" ", "\n"]:
                #     #     continue
                #     # symbol += char
                #     continue
                #
                #
                # symbol = ""
                # index += 1
                # continue



print_tabela_simbolos()

from src.utils import Singleton
from ply.lex import LexToken
from src.lex.lexer import lexer


class SymbolTable(metaclass=Singleton):

    def __init__(self):
        self.tokens: list[LexToken] = []

    def populate(self, input: str):
        lexer.input(input)

        while True:
            tok = lexer.token()
            if not tok:
                break

            self.tokens.append(tok)

    def __str__(self):
        return "\n".join([str(t) for t in self.tokens])

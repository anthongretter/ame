from src.lex.lexicalstructs import Lexer, SymbolTable


if __name__ == "__main__":
    with open('src/resources/exemplo.txt', 'r') as exemplo:
        tokens, symbol_table = Lexer.read(exemplo.read())

    print(tokens)
    print(SymbolTable())

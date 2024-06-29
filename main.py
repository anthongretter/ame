from src.lex.symboltable import SymbolTable


if __name__ == "__main__":
    symbol_table = SymbolTable()

    with open('src/resources/exemplo.txt', 'r') as exemplo:
        symbol_table.populate(exemplo.read())

    print(symbol_table)

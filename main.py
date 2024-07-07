from src.lex.lexicalstructs import Lexer, SymbolTable
from src.syntax.syntaxer import Syntaxer, ResultadoAnalise
from src.syntax.tabela_ll1_parseamento import TABELA

if __name__ == "__main__":
    with open('src/resources/arvere.ame', 'r') as exemplo:
        tokens, symbol_table = Lexer.read(exemplo.read())

    # syntaxer = Syntaxer(tokens, symbol_table)

    # print(tokens)
    # print(symbol_table)
    
    maquina = Syntaxer(tokens, TABELA)
    print(maquina)
    res = maquina.analise()
    if res == ResultadoAnalise.SUCESSO:
        print('Análise sintática concluída com sucesso')

    print(SymbolTable())

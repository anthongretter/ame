from src.lex.lexicalstructs import Lexer, SymbolTable
from src.syntax.syntaxer import Syntaxer, ResultadoAnalise
from src.syntax.tabela_ll1_parseamento import TABELA

if __name__ == "__main__":
    with open('src/resources/merge.ame', 'r') as exemplo:
        tokens, symbol_table = Lexer.read(exemplo.read())
        # FIXME: RESOLVER PROBLEMAS NO LEXICO
        # - NÃO ESTÁ LENDO FLOATS - NÃO RECONHECE CHAR '.'
        # - NÃO RECONHECE EXPRESSÕES SEM SEPARAÇÃO POR ESPAÇOS 
        #   - EX: 'a= 2+ 2' NÃO É RECONHECIDO
        #   - EX: 'a= 2 + 2' É RECONHECIDO

    # syntaxer = Syntaxer(tokens, symbol_table)

    # print(tokens)
    # print(symbol_table)
    
    maquina = Syntaxer(tokens, TABELA)
    print(maquina)
    res = maquina.analise()
    if res == ResultadoAnalise.SUCESSO:
        print('Análise sintática concluída com sucesso')

    
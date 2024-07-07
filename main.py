import argparse
from src.lex.lexicalstructs import Lexer, SymbolTable
from src.syntax.syntaxer import Syntaxer, ResultadoAnalise
from src.syntax.tabela_ll1_parseamento import TABELA

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processa um arquivo .ame")
    parser.add_argument('path_to_file', type=str, help='O caminho ao arquivo a ser processado')
    args = parser.parse_args()

    with open(args.path_to_file, 'r') as exemplo:
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

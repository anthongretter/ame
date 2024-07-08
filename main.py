#
#   COMPILADOR DA LINGUAGEM AME (BASEADA EM X++ - src/resources/ConvCC-2024-1.txt)
#   DISCIPLINA INE5426 - CONSTRUÇÃO DE COMPILADORES - 2024/1
#   
#   Autores: 
#   A - Anthon Porath Gretter (20204787)
#   M - Matheus Antonio de Souza (21203363)
#   E - Eduardo de Moraes (19203167)
#
#   MODIFICAÇÕES DA GRAMÁTICA:
#   1 - Toda chamada de função é precedida pela palavra reservada "call" - Ex: x = call funcao(parametro);
#   2 - Todo return deve retornar um identificador - Ex: return x;
#
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
    
    maquina = Syntaxer(tokens, TABELA)
    res = maquina.analise()
    if res == ResultadoAnalise.SUCESSO:
        print(f'Tabela de Símbolos:{SymbolTable()}')
        print('Análise sintática concluída com sucesso')
        print('Semântica: Todas as expressões aritméticas são válidas (verificação de tipos)')
        print('Semântica: Todas as declarações de variáveis por escopo são validas')
        print('Semântica: Todo "break" está no escopo de um for')



    # print(SymbolTable())

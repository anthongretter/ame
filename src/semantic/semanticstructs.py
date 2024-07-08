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

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from src.utils import Singleton
from src.lex.lexicalstructs import SymbolTable
import src.lex.lexer as lexer
from ply.lex import LexToken


@dataclass
class Node:
    vallex: str | LexToken
    left: Node
    right: Node

    def __repr__(self, depth=1):
        return_string = [str(self.vallex)]
        for child in [self.left, self.right]:
            if child is None: continue
            return_string.extend(["\n", " " * (depth+1), child.__repr__(depth+1)])
        return "".join(return_string)
    
    def __check_state(self, types_f: set, mag: int, ct: LexToken):
        if len(types_f) > 1:
            if "string" in types_f:
                # error mismatch
                raise Exception(f"Operacao com tipos incompativeis em {ct.value} linha {ct.lineno} coluna {ct.lexpos}")
            elif "float" in types_f and SymbolTable().get(self.left.vallex).datatype != "float":
                # error x (int) = 4.3 + 2 (float)
                raise Exception(f"esperado int, mas obteve float em {ct.value} linha {ct.lineno} coluna {ct.lexpos}")
        if ct.magnitude != mag:
            raise Exception(f"Operacao dimensoes de arrays com {ct.value} linha {ct.lineno} coluna {ct.lexpos}")
            
    
    def validate_datatype(self):
        types_found = set()
        queue = [self]
        mag = None

        print(f"Analisando a seguinte arvore de expressao:")
        print(self)
        print()

        while queue:
            d = queue.pop(0)
            for child in [d.left, d.right]:
                if child == None:
                    continue
                elif isinstance(child.vallex, str):
                    match child:
                        case "INT_CONSTANT": types_found.add("int")
                        case "FLOAT_CONSTAT": types_found.add("float")
                        case "STRING_CONSTANT": types_found.add("string")
                        case _: queue.append(child)
                    continue
                
                ident = SymbolTable().get(child.vallex.value)
                child.vallex = ident
                
                if mag == None:
                    mag = ident.magnitude

                types_found.add(child.vallex.datatype)
                self.__check_state(types_found, mag, child.vallex)
                queue.append(child)
        
        print("Arvore aprovada")
        print()


class PilhaEscopoBreak(metaclass=Singleton):
    def __init__(self):
        self.pilha = []

    def pop(self):
        return self.pilha.pop()
    
    def push(self, e):
        self.pilha.append(e)
    
    def peek(self) -> bool:
        if len(self.pilha) == 0:
            return False
        else:
            return True

if __name__ == "__main__":
    raiz = Node('a', Node('b', None, None), Node('c', None, Node('d', None, None)))
    print(raiz)

class PilhaEscopoVariaveis(metaclass=Singleton):
    def __init__(self):
        self.pilha = [[]]
    
    def fim_escopo(self):
        self.pilha.pop()

    def novo_escopo(self):
        self.pilha.append([])

    def insert(self, ident) -> bool: #Caso já haja ident no escopo, 
        if ident in self.pilha[-1]:
            return True
        else:
            self.pilha[-1].append(ident)
            return False
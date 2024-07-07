from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from src.utils import Singleton
from src.lex.lexicalstructs import SymbolTable
import src.lex.lexer as lexer
from ply.lex import LexToken


# class ResultadoSemantica(Enum):
#     SUCESSO = 0
#     ERRO_MISMATCH = 1
#     SUCESSO = 2

class ExpTree(metaclass=Singleton):

    def __init__(self):
        self.reset()

    def reset(self):
        self.d = {}
        self.p = None




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
    
    def validate_datatype(self):
        types_found = set()
        queue = [self]
        print("Analisando a seguinte arvore de expressao...")
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

                types_found.add(child.vallex.datatype)
                queue.append(child)
        
        if len(types_found) > 1:
            if "string" in types_found:
                # error mismatch
                raise Exception("Operacao com tipos incompativeis")
            elif "float" in types_found and SymbolTable().get(self.left.vallex).datatype != "float":
                # error x (int) = 4.3 + 2 (float)
                raise Exception("esperado int, mas obteve float")
        else:
            print("Aprovada")
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
        self.pilha = []
    
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
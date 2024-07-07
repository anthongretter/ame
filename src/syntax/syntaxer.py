import pprint
from ply.lex import LexToken
from enum import Enum

from src.semantic.actions import SemanticAction
from src.utils import Singleton, SingletonSymbol


class ResultadoAnalise(Enum):
    ERRO_TERMINAL = 0
    ERRO_NAO_TERMINAL = 1
    SUCESSO = 2

class NaoTerminal(metaclass=SingletonSymbol):
    def __init__(self, nome):
        self.nome = nome
        self.attrs = {}

    def __str__(self):
        return f'NT({self.nome})'
    
    def __repr__(self):
        return f'NT({self.nome})'
        
class Terminal(metaclass=SingletonSymbol):
    def __init__(self, nome: str):
        self.nome = nome
        self.attrs = {}
    
    def __str__(self):
        return f'T({self.nome})'
    
    def __repr__(self):
        return f'T({self.nome})'

class Producao:
    def __init__(self, cabeca: NaoTerminal, cauda: list[any]): #NT ou T ou AcaoSemantica
        self.cabeca = cabeca
        self.cauda = cauda
    
    def add_elemento(self, elemento):
        self.cauda.append(elemento)

    def eh_vazio(self):
        return len(self.cauda) == 0
    
    def __str__(self):
        return f'{self.cauda}'

class Syntaxer(metaclass=Singleton):
    def __init__(self, entrada: list[LexToken], tabela: dict[str, dict[str, tuple]]):
        self.pilha = [] # a pilha possui objetos do tipo NaoTerminal, Terminal e AcaoSemantica
        self.entrada = entrada # a entrada possui objetos do tipo LexToken
        self.index = 0
        self.tabela = {}
        fim_de_entrada = LexToken()
        fim_de_entrada.type = '$'
        fim_de_entrada.value = '$'
        fim_de_entrada.lineno = -1
        fim_de_entrada.lexpos = -1
        self.entrada.append(fim_de_entrada)
        self.pilha.append(Terminal('$'))
        self.pilha.append(NaoTerminal('PROGRAM'))
        self.tabela = self.gerar_tabela(tabela)

        # print(self)

    def gerar_tabela(self, tabela_ll1):
        # TABELA
        tabela = {}
        for cabeca in tabela_ll1.keys():
            tabela[cabeca] = {}
            for cauda in tabela_ll1[cabeca]:
                cab = NaoTerminal(cabeca)
                aux = []
                
                for elemento in tabela_ll1[cabeca][cauda]:
                    if elemento == '-':
                        continue                        
                        
                    if callable(elemento):
                        aux.append(SemanticAction(elemento, None))
                    elif elemento.isupper():
                        aux.append(NaoTerminal(elemento))
                        # pprint.pprint(SingletonSymbol._instances, indent=4)
                        # input()
                    else:
                        aux.append(Terminal(elemento))
                
                if len(aux) != 0:
                    for e in aux:
                        if isinstance(e, SemanticAction):
                           e.addcauda([cab] + list(filter(lambda ele: not isinstance(ele, SemanticAction), aux))) 

                    tabela[cabeca][cauda] = Producao(cab, aux)

        return tabela
        
    def __str__(self):
        tabela_str = ""
        for cabeca in self.tabela.keys():
            tabela_str += f"[{cabeca}]\n"
            for cauda in self.tabela[cabeca].keys():
                if len(self.tabela[cabeca][cauda].cauda) == 0:
                    continue
                tabela_str += f" >'{cauda}' -> {self.tabela[cabeca][cauda].cauda}"
                tabela_str += "\n"
            tabela_str += "\n"
        return f'Pilha: {self.pilha}\nEntrada: {self.entrada}\nTabela: {tabela_str}'

    def empilha(self, simbolo):
        self.pilha.append(simbolo)

    def desempilha(self):
        return self.pilha.pop()

    def topo_pilha(self):
        return self.pilha[-1]

    def consome_entrada(self):
        self.index += 1
    
    def topo_entrada(self):
        return self.entrada[self.index]

    def analise(self) -> ResultadoAnalise:
        while True:
            X = self.topo_pilha()
            a = self.topo_entrada()
            # print('-----------')
            # print(f'pilha: {self.pilha}')
            # print(f'token: {a}')
            # input()
            if isinstance(X, Terminal):
                if X.nome == a.type.lower():
                    if X.nome == '$':
                        break
                    else:
                        self.desempilha()
                        self.consome_entrada()
                elif X.nome == '&':
                    self.desempilha()
                else:
                    print(f'Erro ao ler o token {a.value} na linha {a.lineno} e coluna {a.lexpos}! (Terminal)')
                    return ResultadoAnalise.ERRO_TERMINAL
                
            elif isinstance(X, NaoTerminal):
                if a.type.lower() in self.tabela[X.nome]:
                    # print(f'Empilhando {self.tabela[X.nome][a.type.lower()]}')
                    self.desempilha()

                    # TODO verificar isso
                    if self.tabela[X.nome][a.type.lower()].cauda == []:
                        print(f'Erro ao ler o token {a.value} na linha {a.lineno} e coluna {a.lexpos}! (NaoTerminal - Empilhando vazio)')
                        return ResultadoAnalise.ERRO_NAO_TERMINAL
                    
                    for i in self.tabela[X.nome][a.type.lower()].cauda[::-1]:
                        self.empilha(i)
                else:
                    print(f'Erro ao ler o token {a.value} na linha {a.lineno} e coluna {a.lexpos}! (NaoTerminal)')
                    return ResultadoAnalise.ERRO_NAO_TERMINAL
            elif isinstance(X, SemanticAction):
                # print(X.args)
                # print(self.entrada[self.index])
                # print("HIST:", self.entrada[0:self.index+1][::-1])
                # input()
                X.func(X.args, self.entrada[0:self.index+1][::-1])
                self.desempilha()
            else:
                raise Exception(f'Erro (OBJETO NA PILHA NÃO RECONHECIDO) {X}')
        
        # print(NaoTerminal("NUMEXPRESSION").attrs['node'])
        return ResultadoAnalise.SUCESSO

# M = {}
# M['PROGRAM']['def'] = [acaosemantica1, funclist_nt]

# 'PROGRAM': {'$': ('&',), 'if': ('STATEMENT',), 'def': ('FUNCLIST',)


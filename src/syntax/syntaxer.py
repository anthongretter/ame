from ply.lex import LexToken
from enum import Enum

class ResultadoAnalise(Enum):
    ERRO_TERMINAL = 0
    ERRO_NAO_TERMINAL = 1
    SUCESSO = 2

class NaoTerminal:
    def __init__(self, nome):
        self.nome = nome
        self.val = 0
        self.p = 0
        self.i = 0
        self.s = 0 #novo atributo
        # self.ação = False

    def __str__(self):
        return f'NT({self.nome})'
    
    def __repr__(self):
        return f'NT({self.nome})'
        
class Terminal:
    def __init__(self, nome):
        self.nome = nome
        # self.ação = False
    
    def __str__(self):
        return f'T({self.nome})'
    
    def __repr__(self):
        return f'T({self.nome})'
        
# class Ação_Semântica:
#     def __init__(self, função, lista_parâmetros):
#         self.função = função
#         self.parâmetros = lista_parâmetros
#         # self.ação = True

class Syntaxer:
    def __init__(self, entrada: list[LexToken], tabela: dict[str, dict[str, tuple]]):
        self.pilha = [] # a pilha possui objetos do tipo NaoTerminal, Terminal e AcaoSemantica
        self.entrada = entrada # a entrada possui objetos do tipo LexToken
        self.tabela = {}
        fim_de_entrada = LexToken()
        LexToken.type = '$'
        LexToken.value = '$'
        LexToken.lineno = -1
        LexToken.lexpos = -1
        self.entrada.append(fim_de_entrada)
        self.pilha.append(Terminal('$'))
        self.pilha.append(NaoTerminal('PROGRAM'))
        self.tabela = self.gerar_tabela(tabela)

        # print(self)

    def gerar_tabela(self, tabela_ll1):
        # TABELA
        tabela = {}
        for cabeça in tabela_ll1.keys():
            tabela[cabeça] = {}
            for cauda in tabela_ll1[cabeça]:
                tabela[cabeça][cauda] = []
                for i in tabela_ll1[cabeça][cauda]:
                    if i == '-':
                        pass
                    elif i.isupper():
                        tabela[cabeça][cauda].append(NaoTerminal(i))
                    else:
                        tabela[cabeça][cauda].append(Terminal(i))
        return tabela
        
    def __str__(self):
        tabela_str = ""
        for cabeça in self.tabela.keys():
            tabela_str += f"[{cabeça}]\n"
            for cauda in self.tabela[cabeça].keys():
                if len(self.tabela[cabeça][cauda]) == 0:
                    continue
                tabela_str += f" >'{cauda}' -> {self.tabela[cabeça][cauda]}"
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
        return self.entrada.pop(0)
    
    def topo_entrada(self):
        return self.entrada[0]

    def analise(self) -> ResultadoAnalise:
        while True:
            X = self.topo_pilha()
            a = self.topo_entrada()
            print('-----------')
            print(f'pilha: {self.pilha}')
            print(f'token: {a}')
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
                    print(f'Empilhando {self.tabela[X.nome][a.type.lower()]}')
                    self.desempilha()

                    # TODO verificar isso
                    if self.tabela[X.nome][a.type.lower()] == []:
                        print(f'Erro ao ler o token {a.value} na linha {a.lineno} e coluna {a.lexpos}! (NaoTerminal - Empilhando vazio)')
                        return ResultadoAnalise.ERRO_NAO_TERMINAL
                    
                    for i in self.tabela[X.nome][a.type.lower()][::-1]:
                        self.empilha(i)
                else:
                    print(f'Erro ao ler o token {a.value} na linha {a.lineno} e coluna {a.lexpos}! (NaoTerminal)')
                    return ResultadoAnalise.ERRO_NAO_TERMINAL
            # TODO: elif isinstance(X, AcaoSemantica):
            else:
                raise Exception(f'Erro (OBJETO NA PILHA NÃO RECONHECIDO) {X}')
        
        return ResultadoAnalise.SUCESSO

# M = {}
# M['PROGRAM']['def'] = [acaosemantica1, funclist_nt]

# 'PROGRAM': {'$': ('&',), 'if': ('STATEMENT',), 'def': ('FUNCLIST',)


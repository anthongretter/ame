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
from src.lex.lexer import reserved
from src.lex.lexicalstructs import SymbolTable
from src.semantic.semanticstructs import Node, PilhaEscopoBreak, PilhaEscopoVariaveis
from dataclasses import dataclass


class SemanticAction:

    def __init__(self, func, args):
        self.func: callable = func
        self.args: list = args

    def addcauda(self, c):
        self.args = c

    def __str__(self):
        return f"{self.func.__name__}"

    def __repr__(self) -> str:
        return f"{self.func.__name__}"


class DEC:

    @staticmethod
    def a(l, t_anteriores):
        # addtype(ident.vallex, int.vallex)
        SymbolTable().addtype(t_anteriores[0].value, t_anteriores[1].value)

    @staticmethod
    def b(l, t_anteriores):
        SymbolTable().addmag(t_anteriores[(l[3].attrs['magnitude']*3) + 1].value, l[3].attrs['magnitude'])

    @staticmethod
    def c(l, t_anteriores):
        SymbolTable().addtype(t_anteriores[0].value, t_anteriores[1].value)

    @staticmethod
    def d(l, t_anteriores):
        SymbolTable().addmag(t_anteriores[(l[3].attrs['magnitude']*3) + 1].value, l[3].attrs['magnitude'])

    @staticmethod
    def e(l, t_anteriores):
        SymbolTable().addtype(t_anteriores[0].value, t_anteriores[1].value)

    @staticmethod
    def f(l, t_anteriores: list):
        SymbolTable().addmag(t_anteriores[(l[3].attrs['magnitude']*3) + 1].value, l[3].attrs['magnitude'])

    @staticmethod
    def g(l, t_anteriores):
        l[0].attrs['magnitude'] = l[4].attrs['magnitude'] + 1

    @staticmethod
    def h(l, t_anteriores):
        l[0].attrs['magnitude'] = 0

    @staticmethod
    def i(l, t_anteriores):
        SymbolTable().addtype(t_anteriores[0].value, t_anteriores[1].value)

    @staticmethod
    def j(l, t_anteriores):
        SymbolTable().addtype(t_anteriores[0].value, t_anteriores[1].value)

    @staticmethod
    def k(l, t_anteriores):
        SymbolTable().addtype(t_anteriores[0].value, t_anteriores[1].value)

    @staticmethod
    def l(l, t_anteriores):
        SymbolTable().addtype(t_anteriores[0].value, t_anteriores[1].value)


class EXPA:

    @staticmethod
    def zb(l, t_anteriores):
        l[0].attrs['node'] = Node("ASSIGN", l[1].attrs['node'], l[3].attrs['node'])
        # l[0].attrs['node'].validate_datatype()

    @staticmethod
    def za(l, t_anteriores):
        l[0].attrs['node'] = l[1].attrs['node']

    @staticmethod
    def a(l, t_anteriores):
        l[2].attrs['left'] = l[1].attrs['node']

    @staticmethod
    def aa(l, t_anteriores):
        l[0].attrs['node'] = l[2].attrs['node']
        l[0].attrs['node'].validate_datatype()

    @staticmethod
    def b(l, t_anteriores):
        l[2].attrs['left'] = l[1].attrs['node']

    @staticmethod
    def c(l, t_anteriores):
        l[0].attrs['node'] = l[2].attrs['node']

    @staticmethod
    def d(l, t_anteriores):
        l[2].attrs['left'] = l[1].attrs['node']

    @staticmethod
    def e(l, t_anteriores):
        l[0].attrs['node'] = l[2].attrs['node']

    @staticmethod
    def f(l, t_anteriores):
        l[3].attrs['left'] = l[2].attrs['node']

    @staticmethod
    def g(l, t_anteriores):
        l[0].attrs['node'] = Node('PLUS', l[0].attrs['left'], l[3].attrs['node'])

    @staticmethod
    def h(l, t_anteriores):
        l[3].attrs['left'] = l[2].attrs['node']

    @staticmethod
    def i(l, t_anteriores):
        l[0].attrs['node'] = Node('MINUS', l[0].attrs['left'], l[3].attrs['node'])
        
    @staticmethod
    def j(l, t_anteriores):
        l[0].attrs['node'] = l[0].attrs['left']
    
    @staticmethod
    def k(l, t_anteriores):
        l[0].attrs['node'] = l[1].attrs['node']

    @staticmethod
    def l(l, t_anteriores):
        l[0].attrs['node'] = l[0].attrs['left']

    @staticmethod
    def m(l, t_anteriores):
        l[0].attrs['node'] = l[2].attrs['node']

    @staticmethod
    def n(l, t_anteriores):
        l[0].attrs['node'] = l[2].attrs['node']

    @staticmethod
    def o(l, t_anteriores):
        l[0].attrs['node'] = l[1].attrs['node']

    @staticmethod
    def p(l, t_anteriores):
        l[0].attrs['node'] = Node('TIMES', l[0].attrs['left'], l[3].attrs['node'])
    
    @staticmethod
    def pp(l, t_anteriores):
        l[3].attrs['left'] = l[2].attrs['node']  

    @staticmethod
    def q(l, t_anteriores):
        l[0].attrs['node'] = Node('DIVIDE', l[0].attrs['left'], l[3].attrs['node'])

    @staticmethod
    def qq(l, t_anteriores):
        l[3].attrs['left'] = l[2].attrs['node'] 

    @staticmethod
    def r(l, t_anteriores):
        l[0].attrs['node'] = Node('MOD', l[0].attrs['left'], l[3].attrs['node'])

    @staticmethod
    def rr(l, t_anteriores):
        l[3].attrs['left'] = l[2].attrs['node']

    @staticmethod
    def s(l, t_anteriores):
        l[0].attrs['node'] = l[0].attrs['left']

    @staticmethod
    def t(l, t_anteriores):
        l[0].attrs['node'] = Node('INT_CONSTANT', None, None)

    @staticmethod
    def u(l, t_anteriores):
        l[0].attrs['node'] = Node("FLOAT_CONSTANT", None, None)

    @staticmethod
    def v(l, t_anteriores):
        l[0].attrs['node'] = Node("STRING_CONSTANT", None, None)

    @staticmethod
    def w(l, t_anteriores):
        l[0].attrs['node'] = Node(reserved['null'], None, None)

    @staticmethod
    def x(l, t_anteriores):
        l[0].attrs['node'] = l[1].attrs['node']

    @staticmethod
    def y(l, t_anteriores):
        l[0].attrs['node'] = l[2].attrs['node']

    @staticmethod
    def z(l, t_anteriores):
        l[0].attrs['node'] = Node(l[2].attrs['ident'], None, None)

    @staticmethod
    def zz(l, t_anteriores):
        l[2].attrs['ident'] = t_anteriores[1]

    @staticmethod
    def ab(l, t_anteriores):
        l[0].attrs['node'] = Node('LESS', l[0].attrs['left'], l[2].attrs['node'])

    @staticmethod
    def ac(l, t_anteriores):
        l[0].attrs['node'] = Node('GREATER', l[0].attrs['left'], l[2].attrs['node'])

    @staticmethod
    def ad(l, t_anteriores):
        l[0].attrs['node'] = Node('LESSEQUAL', l[0].attrs['left'], l[2].attrs['node'])

    @staticmethod
    def ae(l, t_anteriores):
        l[0].attrs['node'] = Node('GREATEREQUAL', l[0].attrs['left'], l[2].attrs['node'])

    @staticmethod
    def af(l, t_anteriores):
        l[0].attrs['node'] = Node('EQUAL', l[0].attrs['left'], l[2].attrs['node'])

    @staticmethod
    def ag(l, t_anteriores):
        l[0].attrs['node'] = Node('DIFF', l[0].attrs['left'], l[2].attrs['node'])

    @staticmethod
    def ah(l, t_anteriores):
        l[0].attrs['node'] = l[0].attrs['left']

class BREAK:
    @staticmethod
    def a(l, t_anteriores):
        pilha = PilhaEscopoBreak()
        # pilha.push(l[0].attrs['prox'])
        pilha.push('temp')
    
    @staticmethod
    def b(l, t_anteriores):
        pilha = PilhaEscopoBreak()
        try:
            pilha.pop() # Se falhar, erro de sintaxe (nao tem fechamento de loop, nao deveria acontecer em etapa semantica)
        except:
            raise Exception(f'Na linha {t_anteriores[0].lineno} e coluna {t_anteriores[0].lexpos}:\n>> Fechamento de escopo de FOR sem abertura.')


    @staticmethod
    def c(l, t_anteriores):
        pilha = PilhaEscopoBreak()
        if not pilha.peek():
            # Se falhar, erro semantico
            raise Exception(f'"break" na linha {t_anteriores[0].lineno} e coluna {t_anteriores[0].lexpos}:\n>> "break" fora de escopo de um for.')

class ESCOPOVAR:
    @staticmethod
    def a(l, t_anteriores):
        pilha = PilhaEscopoVariaveis()
        pilha.novo_escopo()

    @staticmethod
    def b(l, t_anteriores):
        pilha = PilhaEscopoVariaveis()
        pilha.fim_escopo()
    
    @staticmethod
    def c(l,  t_anteriores):
        pilha = PilhaEscopoVariaveis()
        if pilha.insert(t_anteriores[0].value):
            raise Exception(f'{t_anteriores[0].value} na linha {t_anteriores[0].lineno} coluna {t_anteriores[0].lexpos}:\nIdentificador já declarado em escopo.')

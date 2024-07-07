class Produção:
    def  __init__(self, cabeça, cauda):
        self.cabeça = cabeça
        self.cauda = cauda
    
class Variável:
    def __init__(self, nome):
        self.nome = nome
        self.val = 0
        self.p = 0
        self.i = 0
        self.s = 0 #novo atributo
        self.ação = False
        
class Terminal:
    def __init__(self, nome):
        self.nome = nome
        self.ação = False
        
class Ação_Semântica:
    def __init__(self, função, lista_parâmetros):
        self.função = função
        self.parâmetros = lista_parâmetros
        self.ação = True

def É_terminal(X, T):
    for i in T:
        if i.nome == X.nome:
            return True
    return False

def f1(l):
    l[0].val = l[1].val
    
def f2(l):
    l[0].p = 0
    
def f3(l):
    l[0].p = l[1].p + 1
    
def f4(l):
    l[0].i = l[1].i

def f5(l):
    l[0].val = l[1].val 
    
def f6(l):
    l[0].val = l[1].val + pow(2, l[0].i - l[0].s) #alterou de atributo p para atributo s
    
def f7(l):
    l[0].i = l[0].p
    
def f8(l):
    l[0].val = 0
    
def f9(l):
    l[0].val = 1
    
def f10(l):
    l[0].p = l[1].p + 1
    
def f11(l):
    l[0].i = l[1].i
    
def f12(l):
    l[0].val = l[1].val
    
def f13(l):
    l[0].val = l[1].val + pow(2, l[0].i - l[0].s) ##alterou de atributo p para atributo s
    
def f14(l):
    l[0].i = l[0].p
    
def f15(l):
    l[0].val = 0
    
def f16(l):
    l[0].val = 1

#novas funções
def f17(l):
    l[0].s = l[1].s - 1
  
def f18(l):
    l[0].s = l[0].p
#-------------
    
S = Variável("S")
B = Variável("B")
Bp = Variável("Bp")

V = [S, B, Bp]

zM = Terminal("0M")
uM = Terminal("1M")
zm = Terminal("0m")
um = Terminal("1m")
z = Terminal("0")
u = Terminal("1")
sifrão = Terminal("$")

T = [zM, uM, zm, um, z, u, sifrão]

a1 = Ação_Semântica(f1, [S, B])
a2 = Ação_Semântica(f2, [B])
a3 = Ação_Semântica(f3, [Bp, B])
a4 = Ação_Semântica(f4, [B, Bp])
a5 = Ação_Semântica(f5, [B, Bp])
a6 = Ação_Semântica(f6, [B, Bp])
a7 = Ação_Semântica(f7, [B])
a8 = Ação_Semântica(f8, [B])
a9 = Ação_Semântica(f9, [B])
a10 = Ação_Semântica(f10, [B, Bp])
a11 = Ação_Semântica(f11, [Bp, B])
a12 = Ação_Semântica(f12, [Bp, B])
a13 = Ação_Semântica(f13, [Bp, B])
a14 = Ação_Semântica(f14, [Bp])
a15 = Ação_Semântica(f15, [Bp])
a16 = Ação_Semântica(f16, [Bp])

#novas ações
a17 = Ação_Semântica(f17, [B, Bp])
a18 = Ação_Semântica(f18, [B])
a19 = Ação_Semântica(f17, [Bp, B])
a20 = Ação_Semântica(f18, [Bp])
#-------------

M = {}
M[("S", "0M")] = Produção(S, [a2, B, a1])
M[("S", "1M")] = Produção(S, [a2, B, a1])
M[("S", "0m")] = Produção(S, [])
M[("S", "1m")] = Produção(S, [])
M[("S", "0")] = Produção(S, [a2, B, a1])
M[("S", "1")] = Produção(S, [a2, B, a1])
M[("B", "0M")] = Produção(B, [zM, a3, Bp, a4, a17, a5]) #nova ação inserida
M[("B", "1M")] = Produção(B, [uM, a3, Bp, a4, a17, a6]) #nova ação inserida
M[("B", "0m")] = Produção(B, [])
M[("B", "1m")] = Produção(B, [])
M[("B", "0")] = Produção(B, [z, a7, a8, a18]) #nova ação inserida
M[("B", "1")] = Produção(B, [u, a7, a9, a18]) #nova ação inserida
M[("Bp", "0M")] = Produção(Bp, [])
M[("Bp", "1M")] = Produção(Bp, [])
M[("Bp", "0m")] = Produção(Bp, [zm, a10, B, a11, a19, a12]) #nova ação inserida
M[("Bp", "1m")] = Produção(Bp, [um, a10, B, a11, a19, a13]) # nova ação inserida
M[("Bp", "0")] = Produção(Bp, [z, a14, a15, a20]) #nova ação inserida
M[("Bp", "1")] = Produção(Bp, [u, a14, a16, a20]) #nova ação inserida
    
pilha = [sifrão, S, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
topo = 1

i = 0
w = [uM, zm, zM, um, uM, zm, z, sifrão] #palavra

X = pilha[topo]
while(True):
    if not X.ação and X.nome == "$":
        break
    elif X.ação:
        #executa ação
        X.função(X.parâmetros)
        #desempilha
        topo = topo - 1
    elif X.nome == w[i].nome:
        #desempilha
        topo = topo - 1
        i = i + 1
    elif É_terminal(X, T):
        print("Erro. Terminal != da entrada")
        break
    elif len(M[(X.nome, w[i].nome)].cauda) == 0:
        print("Erro. Entrada vazia na tabela")
        break
    else:
        print(M[(X.nome, w[i].nome)].cabeça.nome, "->", end = '')
        cauda_atual = M[(X.nome, w[i].nome)].cauda
        for c in cauda_atual:
            if (not c.ação):
                print(c.nome, end='')
        print()
        topo = topo - 1
        j = len(cauda_atual) - 1
        while j >= 0:
            pilha[topo + 1] = cauda_atual[j]
            topo = topo + 1
            j = j - 1
    X = pilha[topo]
    
print(S.val)

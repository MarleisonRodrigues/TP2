from collections import deque
import math

#Classe Nó
class Node:
    def __init__(self):
       self.tabuleiro = []

class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""

    def __init__(self):
        self.topo = None


    def __repr__(self):
        return "[" + str(self.topo) + "]"

#Realizar os movimentos no tabuleiro     
def move(tab_original):

    """
    Checa possíveis movimentos (os nós)
    da árvore
    """
    movimentos = []
    tab = eval(tab_original) #comparar os dois tabuleiro, atual com o final 
    i = 0
    j = 0
    
    while 0 not in tab[i]: i += 1 #enquanto espaço em branco não estiver no objetivo
    j = tab[i].index(0)

    
    if i<2:         #mover o 0 para baixo  
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]   # Troca elemento de lugar com o pai.
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]
        

    if i>0:         #mover o 0 para cima
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        

    if j<2:         #mover o 0 para a direita
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
        

    if j>0:         #mover o 0 para a esquerda
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]
      
    return movimentos

#função avaliação recebe o tabuleiro
#retorna a distancia total da busca gulosa até o objetivo  
def gulosa_h1(tabuleiro):

    distance = 0 
    tab = eval(tabuleiro) 
    for i in range(3):
        for j in range(3):
            if tab[i][j] != 0:
                x, y = divmod(tab[i][j]-1, 3)  
                distance += abs(x - i) + abs(y - j) #tirando o valor absoluto e fazendo a soma deles e armazena na distancia                
    return distance #retorna a distancia 

#Usa a Busca Gulosa para resolver o quebra-cabeça pela 
#heuristica da distancia de manhattan
def Gulosa_h1(start, end):

    explorado = [] 
    filaprioridade = [[gulosa_h1(start), start]] 
    while filaprioridade: 
        i = 0
        for j in range(1,len(filaprioridade)): 
            if (filaprioridade[i][0]) > (filaprioridade[j][0]):
                i = j
        caminho = filaprioridade[i] 
        filaprioridade = filaprioridade[:i] + filaprioridade[i+1:]
        final = caminho[-1] #retira um elemento da fila
        for movimento in move(final): 
            if movimento in explorado: continue 
            novo = [caminho[0] + gulosa_h1(final)] + caminho[1:] + [movimento] 
            filaprioridade.append(novo) 
        explorado.append(final) 

        if final == end: break #se atigiu o objetivo, finaliza o laço e imprime
    print('\nNós expandidos: ', (len(explorado)-1))
    print('A distancia de Manhattan é: ', gulosa_h1(tabuleiro))
    print('Quantidade e Movimentos para chegar a solução: ')
    print(len(caminho)-1)
    return caminho[1:]

#função avaliação recebe o tabuleiro
#retorna as peças que estão fora do lugar até chegar ao objetivo  
def gulosa_h2(tabuleiro):

    misplaced = 0
    comparador = 1
    tab = eval(tabuleiro)
    for i in range(0,3):
        for j in range(0,3):
            if tab[i][j] != comparador:
                misplaced = misplaced + 1
            comparador += 1
    return misplaced

#Usa a Busca Gulosa para resolver o quebra-cabeça pela 
#heuristica das peças que estão fora do lugar
def Gulosa_h2(start, end):

    explorado = []
    filaprioridade = [[gulosa_h2(start), start]]

    while filaprioridade:
        i = 0
        for j in range(1,len(filaprioridade)):
            if (filaprioridade[i][0]) > (filaprioridade[j][0]):
                i = j
        caminho = filaprioridade[i]
        filaprioridade = filaprioridade[:i] + filaprioridade[i+1:]
        final = caminho[-1]
        for movimento in move(final):
            if movimento in explorado: continue
            novo = [caminho[0] + gulosa_h2(final)] + caminho[1:] + [movimento] 
            filaprioridade.append(novo)
        explorado.append(final)

        if final == end: break
    print('\nNós expandidos: ', (len(explorado)-1))
    print('Quantidade de peças fora do lugar: ', gulosa_h2(tabuleiro))
    print('Quantidade e Movimentos para chegar a solução: ')
    print(len(caminho)-1)
    return caminho[1:]


#função avaliação recebe o tabuleiro
#retorna a distancia total da busca até o objetivo  
def manhattan(tabuleiro):
        distance = 0
        tab = eval(tabuleiro)
       
        for i in range(3):
            for j in range(3):
                if tab[i][j] != 0:
                    x, y = divmod(tab[i][j]-1, 3)
                    distance += abs(x - i) + abs(y - j) #tirando o valor absoluto e fazendo a soma deles       
        return distance #retorna a distancia

#Usa o A* para resolver o quebra-cabeça pela 
#heuristica da distancia manhattan
def a_estrelah2(start,end):

    explorado = []
    banco = [[manhattan(start),start]]
    while banco:
        i = 0
        for j in range(1,len(banco)):
            if (banco[i][0]) > (banco[j][0]):
               i = j
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        final = caminho[-1]
        if final in explorado: continue
        for movimento in move(final):
            if movimento in explorado: continue
            novo = [caminho[0] + manhattan(movimento) + manhattan(final)] + caminho[1:] + [movimento] 
            banco.append(novo)
        explorado.append(final)
        if final == end: break

    print('\nNós expandidos: ', (len(explorado)-1))
    print('A distancia de Manhattan é: ', manhattan(tabuleiro))
    print('Quantidade e Movimentos para chegar a solução: ')
    print(len(caminho)-1)
    return caminho[1:]

#função avaliação recebe o tabuleiro
#retorna as peças estão fora do lugar até chegar ao objetivo  
def h_misplaced(tabuleiro): 

    misplaced = 0
    comparador = 1
    tab = eval(tabuleiro)
    for i in range(0,3):
        for j in range(0,3):
            if tab[i][j] != comparador:
                misplaced += 1
            comparador += 1
    return misplaced

#Usa o A* para resolver o quebra-cabeça pela 
#heuristica das peças estão fora do lugar
def a_estrelah1(start,end):
   
    explorado = []
    banco = [[h_misplaced(start),start]]
    while banco:
        i = 0
        for j in range(1,len(banco)):
            if (banco[i][0]) > (banco[j][0]):
               i = j
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        final = caminho[-1]
        if final in explorado: continue
        for movimento in move(final):
            if movimento in explorado: continue
            novo = [caminho[0] + h_misplaced(movimento) + h_misplaced(final)] + caminho[1:] + [movimento] 
            banco.append(novo)
        explorado.append(final)
        if final == end: break
    print('\nNós expandidos: ', (len(explorado)-1))
    print('Quantidade de peças fora do lugar: ', h_misplaced(tabuleiro))
    print('Quntidade e Movimentos para chegar a solução: ')
    print(len(caminho)-1)
    return caminho[1:]

#main

#preenchimento do tabuleiro inicial
raiz=Node
raiz.tabuleiro=[]

for i in range (0,3):
    local=[]
    for i in range(0,3):
        local.append(int(input('Digite um número: ')))
    raiz.tabuleiro.append(local)
print("\nO tabuleiro está: ")

for i in range (0,3):
    print(raiz.tabuleiro[i])

tabuleiro = str(raiz.tabuleiro)

obj_final = str([
                [1,2,3],
                [4,5,6],
                [7,8,0]
            ])

print ('\nO objetivo é: ')
print (obj_final)

print('\nInforme qual algoritmo de busca deseja utilizar para chegar ao objetivo: ')
print()
print("1: BUSCA GULOSA")
print("2: BUSCA A*")
print()
op = int(input('Informe uma opção: '))

if(op==1):
        print('\n___________MÉTODO DE BUSCA GULOSA___________')
        print('\nInforme qual heurística deseja utilizar na busca: ')
        print()
        print("1: Distancia de Manhattan")
        print("2: Peças Fora do Lugar")
        print()
        op2 = int(input('Informe uma opção: '))
        if(op2==1):
            print('\n___________MÉTODO DE BUSCA GULOSA - Distancia de Manhattan___________')
            for i in Gulosa_h1(tabuleiro,obj_final):
                print(i, end="\n")
        if(op2==2):
            print('\n___________MÉTODO DE BUSCA GULOSA - Peças Fora do Lugar___________')
            for i in Gulosa_h2(tabuleiro,obj_final):
                print(i, end="\n")

if(op==2):
        print('\n___________MÉTODO DE BUSCA A*___________')
        print('\nInforme qual heuristica deseja utilizar na busca: ')
        print()
        print("1: Distancia de Manhattan")
        print("2: Peças Fora do Lugar")
        print()
        op2 = int(input('Informe uma opção: '))
        if(op2==1):
            print('\n___________MÉTODO DE BUSCA EM A* -  Distancia de Manhattan___________')
            for i in a_estrelah2(tabuleiro,obj_final):
                print(i, end="\n")
        if(op2==2):
            print('\n___________MÉTODO DE BUSCA EM A* - Peças Fora do Lugar___________')
            for i in a_estrelah1(tabuleiro,obj_final):
                print(i, end="\n")


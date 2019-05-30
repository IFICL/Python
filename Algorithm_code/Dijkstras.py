#!/usr/bin/python3
from Graph import *

Inf = float('inf') 

def takeValue(x):
    return x.value

def Dijkstras(G, S_name, T_name):
    # Use the data structure implemented

    # Initialization 
    H = list()  # Create as a minheap
    S = G.GetVertex(S_name)
    T = G.GetVertex(T_name)
    for V in G.Vertex_List:
        V.Prev = None
        V.ifvisit = False
        if V == S:
            V.value = 0
        else:
            V.value = Inf
        H.append(V)
        H.sort(key = takeValue)
        
    while len(H) != 0:
        u = H.pop(0)
        u.ifvisit = True
        for v in G.Vertex_List:
            if G.AdMatrix[u.index][v.index] != None and v.ifvisit == False:
                line = G.AdMatrix[u.index][v.index]
                if v.value > u.value + line:
                    v.value = u.value + line
                    v.Prev = u
                    H.sort(key = takeValue)
    
    # Output the path and distance
    u = T
    print(S.name, 'to', u.name, 'cost:', u.value, '| Path:', u.name, end = ' ')
    while u.Prev != None:
        u = u.Prev
        print("<-", u.name, end = ' ')
    print(' ')


if __name__ == "__main__":
    G = DiGraph()
    G.AddVertex('1'); G.AddVertex('2'); G.AddVertex('3')
    G.AddVertex('4'); G.AddVertex('5'); G.AddVertex('6')
    G.AddEdge('1', '2', 2); G.AddEdge('1', '3', 8)
    G.AddEdge('2', '3', 5); G.AddEdge('2', '4', 3)
    G.AddEdge('3', '2', 6); G.AddEdge('3', '5', 0)
    G.AddEdge('4', '3', 1); G.AddEdge('4', '5', 7); G.AddEdge('4', '6', 6)
    G.AddEdge('5', '4', 4)
    G.AddEdge('6', '5', 2)
    G.Display()
    Dijkstras(G, '1', '6'); Dijkstras(G, '2', '6'); Dijkstras(G, '3', '6')
    Dijkstras(G, '4', '6'); Dijkstras(G, '5', '6'); Dijkstras(G, '6', '6')

    

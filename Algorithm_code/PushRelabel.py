#!/usr/bin/python3
from Graph import *
import copy

def takeValue(x):
    return x[1].value

def FindCondV(G, S, T, F):
    L = list()
    for u in G.Vertex_List:
        if u != S and u != T:
            Flow_in = 0; Flow_out = 0
            for v in G.Vertex_List:
                if F[v.index][u.index] > 0:
                    Flow_in = Flow_in + F[v.index][u.index] # Calculate the flow which flow into this vertex
                if F[u.index][v.index] > 0:
                    Flow_out = Flow_out + F[u.index][v.index]   # Calculate the flow which flow out from this vertex
            F_d = Flow_in - Flow_out
            if F_d > 0:
                L.append([F_d, u])
    return L
            
def Push(v, w, f_d, F, RC):
    # Push Operation
    L = []
    L.append(f_d); L.append(RC[v.index][w.index])
    d = min(L)
    # Forward
    RC[v.index][w.index] = RC[v.index][w.index] - d
    F[v.index][w.index] = F[v.index][w.index] + d
    # Backward
    RC[w.index][v.index] = RC[w.index][v.index] + d
    F[w.index][v.index] = F[w.index][v.index] - d
    print("Push: Increase", v.name, '-', w.name, 'with flow of', d)

def Relabel(V):
    # Relabel Operation to increase the height of node
    V.value = V.value + 1
    print("Relabel: Increase the height of", V.name, 'to', V.value)

def Push_Relabel(G, S_name, T_name):
    S = G.GetVertex(S_name)
    T = G.GetVertex(T_name)
    N = len(G.Vertex_List)  
    # Create a residual capacity Matrix  
    RC = copy.deepcopy(G.AdMatrix) 
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            if RC[i][j] == None:
                RC[i][j] = 0

    # Create a Flow Matrix
    F = copy.deepcopy(G.AdMatrix)
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            F[i][j] = 0

    # Initialization Invariant (1)(2) 
    for u in G.Vertex_List:
        if u == S:
            u.value = N     # Set the value as the height
        else:
            u.value = 0
    # Setting flow 
    for v in G.Vertex_List:
        if RC[S.index][v.index] > 0:
            # Forward
            F[S.index][v.index] = RC[S.index][v.index]
            RC[S.index][v.index] = 0
            # Backward
            RC[v.index][S.index] = RC[v.index][S.index] + F[S.index][v.index]
            F[v.index][S.index] = F[v.index][S.index] - F[S.index][v.index]

    # Main loop
    E = FindCondV(G, S, T, F)
    iteration = 0
    while len(E) > 0:
        print("Iteration", iteration)
        E.sort(key = takeValue)
        v = E[len(E) - 1][1]     # Find the value with the maximum height
        f_d = E[len(E) - 1][0]   # Record the flow difference
        print('There exist a excess vertex:', v.name, 'with height =', v.value, 'and excess flow =', f_d)
        DH = [] # Downhill node
        for w in G.Vertex_List:
            if RC[v.index][w.index] > 0 and v.value - w.value == 1:
                DH.append(w)
        
        if len(DH) != 0:
            Push(v, DH[0], f_d, F, RC) 
        else:
            Relabel(v)
        E = FindCondV(G, S, T, F)
        
        # if iteration == 2:
        #     break
        iteration = iteration + 1
        print(' ')
    Max_flow = 0
    for u in G.Vertex_List:
        if F[u.index][T.index] > 0:
            Max_flow = Max_flow + F[u.index][T.index]
    print('Iteration', iteration)
    print("There is no excess vertex, the program is end.")
    print("The Maximum of Flow is", Max_flow)
    return Max_flow



if __name__ == '__main__':
    G = DiGraph()
    G.AddVertex('S'); G.AddVertex('V'); G.AddVertex('W'); G.AddVertex('T')
    G.AddEdge('S', 'V', 1); G.AddEdge('S', 'W', 100)
    G.AddEdge('V', 'W', 100); G.AddEdge('V', 'T', 100)
    G.AddEdge('W', 'V', 1); G.AddEdge('W', 'T', 1)

    Flow = Push_Relabel(G, 'S', 'T')
    

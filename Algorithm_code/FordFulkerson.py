#!/usr/bin/python3
from Graph import *
import copy

def PrintM(G, M):
    # To print the Matrix of residual capacity and Flow
    N = len(G.Vertex_List)
    print("  ", end = " ")
    for i in range(0, N, 1):
        print(G.Vertex_List[i].name, end = "  ")
    print(" ")

    for i in range(0, N, 1):
        print(G.Vertex_List[i].name, end = "  "  )
        for j in range(0, N, 1):
            if M[i][j] == None:
                print("N", end = "  ")
            else:
                print(M[i][j], end = "  ")
        print("  ")


def Ford_FulkeRCon(G, S_name, T_name):
    # Initialization
    S = G.GetVertex(S_name)
    T = G.GetVertex(T_name)
    Max_flow = 0
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

    iteration = 0   # Record the iterations
    # while loop to get the flow
    while True:
        for u in G.Vertex_List:
            u.ifvisit = False
            u.Prev = None
        q = []
        q.append(S)
        
        # Run BFS in G_f to find the augmenting path
        while len(q) != 0:
            u = q.pop(0)
            for v in G.Vertex_List:
                if v.ifvisit == False and RC[u.index][v.index] > 0:
                    v.ifvisit = True
                    v.Prev = u
                    q.append(v)

        if T.ifvisit == True:
            Path = []
            tmp = T
            while tmp != S:
                edge = RC[tmp.Prev.index][tmp.index]
                Path.append(edge)
                tmp = tmp.Prev

            d = min(Path)   # the maximum flow it can increase
            tmp = T
            while tmp != S:
                # Forward
                RC[tmp.Prev.index][tmp.index] = RC[tmp.Prev.index][tmp.index] - d   # Change the residual capacity
                F[tmp.Prev.index][tmp.index] = F[tmp.Prev.index][tmp.index] + d     # change the flow
                # Backward
                RC[tmp.index][tmp.Prev.index] = RC[tmp.index][tmp.Prev.index] + d   # Change the residual capacity
                F[tmp.index][tmp.Prev.index] = F[tmp.index][tmp.Prev.index] - d     # change the flow

                tmp = tmp.Prev
            
            Max_flow = Max_flow + d

            # Print Part
            print("Iteration", iteration, ':')
            print("The Matrix of Flow F: ")
            PrintM(G, F)
            print("The Matrix of Residual Capacity RC: ")
            PrintM(G, RC)
            print(' ')
            iteration = iteration + 1
        else:
            print("The Maximum of Flow is", Max_flow)
            break   # There is no augmenting path (S, T)

    return Max_flow

if __name__ == "__main__":
    G = DiGraph()
    G.AddVertex('S'); G.AddVertex('A'); G.AddVertex('B'); G.AddVertex('T')
    G.AddEdge('S', 'A', 3); G.AddEdge('S', 'B', 2)
    G.AddEdge('A', 'B', 5); G.AddEdge('A', 'T', 2)
    G.AddEdge('B', 'T', 3)

    Flow = Ford_FulkeRCon(G, 'S', 'T')



#!/usr/bin/python3
import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.index = 0  # Work as the index in the Matrix
        self.Prev = None
        self.ifvisit = False

class UndiGraph:
    # The data structure of Undirected Graph
    def __init__(self):
        self.Vertex_List = []   
        self.AdMatrix = []  # Adjacent Matrix of graph: A[M][N] means edge M: Row, N: Column

    def AddVertex(self, u_name):
        # Create the new vertex into the graph
        u = Vertex(u_name)
        u.index = len(self.AdMatrix)
        self.Vertex_List.append(u)
        u_List = [None for i in range(0, u.index + 1, 1)]
        if u.index != 0:
            for L in self.AdMatrix:
                L.append(None)
        self.AdMatrix.append(u_List)
    
    def GetVertex(self, u_name):
        # Search the vertex by its name 
        for u in self.Vertex_List:
            if u.name == u_name:
                return u 
        return None # if not find

    def RemoveVertex(self, u_name):
        # Remove the vertex by its name
        u = self.GetVertex(u_name)
        if u.index < len(self.Vertex_List) and u != None:
            del self.Vertex_List[u.index]
            del self.AdMatrix[u.index]
            for L in self.AdMatrix:
                del L[u.index]
            print("Vertex", u.name, "has been removed.")
            for i in range(0, len(self.Vertex_List), 1):
                self.Vertex_List[i].index = i
                # reset the index of each vertex
        else: 
            print("Invalid Operation.")

    def AddEdge(self, u_name, v_name, weight):
        # Create the weighted edge in the graph. If its unweight, weight can be set as 0 or 1.
        u = self.GetVertex(u_name)
        v = self.GetVertex(v_name)
        self.AdMatrix[u.index][v.index] = weight
        self.AdMatrix[v.index][u.index] = weight

    def GetEdgeWeight(self, u_name, v_name):
        # get the weight of edge by their names
        u = self.GetVertex(u_name)
        v = self.GetVertex(v_name)
        return self.AdMatrix[u.index][v.index]

    def RemoveEdge(self, u_name, v_name):
        u = self.GetVertex(u_name)
        v = self.GetVertex(v_name)
        if u.index < len(self.Vertex_List) and v.index < len(self.Vertex_List):
            self.AdMatrix[u.index][v.index] = None
            self.AdMatrix[v.index][u.index] = None
            print("The edge (", u.name, v.name, ") is removed.")
        else:
            print("Invalid Operation.")
    
    def Display(self):
        print("  ", end = " ")
        for i in range(0, len(self.Vertex_List), 1):
            print(self.Vertex_List[i].name, end = "  ")
        print(" ")

        for i in range(0, len(self.Vertex_List), 1):
            print(self.Vertex_List[i].name, end = "  "  )
            for j in range(0, len(self.Vertex_List), 1):
                if self.AdMatrix[i][j] == None:
                    print("N", end = "  ")
                else:
                    print(self.AdMatrix[i][j], end = "  ")
            print("  ")

class DiGraph:
    # The data structure of Directed Graph
    def __init__(self):
        self.Vertex_List = []   
        self.AdMatrix = []  # Adjacent Matrix of graph
    
    def AddVertex(self, u_name):
        # Create the new vertex into the graph
        u = Vertex(u_name)
        u.index = len(self.AdMatrix)
        self.Vertex_List.append(u)
        u_List = [None for i in range(0, u.index + 1, 1)]
        if u.index != 0:
            for L in self.AdMatrix:
                L.append(None)
        self.AdMatrix.append(u_List)
    
    def GetVertex(self, u_name):
        # Search the vertex by its name 
        for u in self.Vertex_List:
            if u.name == u_name:
                return u 
        return None # if not find

    def RemoveVertex(self, u_name):
        # Remove the vertex by its name
        u = self.GetVertex(u_name)
        if u.index < len(self.Vertex_List) and u != None:
            del self.Vertex_List[u.index]
            del self.AdMatrix[u.index]
            for L in self.AdMatrix:
                del L[u.index]
            print("Vertex", u.name, "has been removed.")
            for i in range(0, len(self.Vertex_List), 1):
                self.Vertex_List[i].index = i
                # reset the index of each vertex
        else: 
            print("Invalid Operation.")

    def AddEdge(self, u_name, v_name, weight):
        # Create the weighted directed edge in the graph. If its unweight, weight can be set as 0 or 1.
        u = self.GetVertex(u_name)
        v = self.GetVertex(v_name)
        self.AdMatrix[u.index][v.index] = weight

    def GetEdgeWeight(self, u_name, v_name):
        # get the weight of edge by their names
        u = self.GetVertex(u_name)
        v = self.GetVertex(v_name)
        return self.AdMatrix[u.index][v.index]

    def RemoveEdge(self, u_name, v_name):
        u = self.GetVertex(u_name)
        v = self.GetVertex(v_name)
        if u.index < len(self.Vertex_List) and v.index < len(self.Vertex_List):
            self.AdMatrix[u.index][v.index] = None
            print("The edge (", u.name, v.name, ") is removed.")
        else:
            print("Invalid Operation.")
    
    def Display(self):
        print("  ", end = " ")
        for i in range(0, len(self.Vertex_List), 1):
            print(self.Vertex_List[i].name, end = "  ")
        print(" ")

        for i in range(0, len(self.Vertex_List), 1):
            print(self.Vertex_List[i].name, end = "  "  )
            for j in range(0, len(self.Vertex_List), 1):
                if self.AdMatrix[i][j] == None:
                    print("N", end = "  ")
                else:
                    print(self.AdMatrix[i][j], end = "  ")
            print("  ")

if __name__ == '__main__':
    G = DiGraph()
    G.AddVertex('A'); G.AddVertex('B'); G.AddVertex('C')
    G.AddEdge('A', 'B', 1)
    G.AddEdge('A', 'C', 2)
    G.AddEdge('B', 'C', 3)
    G.RemoveEdge('A', 'B')
    G.RemoveVertex('A')
    G.Display()
    print(G.GetEdgeWeight('C', 'B'))
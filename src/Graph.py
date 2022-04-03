import os
import pandas as pd
import numpy as np
import networkx as nx

class Graph:
    """Create a class of Graph"""
    def __init__(self):
        # all value range from 0 - 100 base 5
        self.nodePosVal = [i*5 for i in range(20)]
        # node initialize
        self.node : list = None
        # nodeNeighbors initialize
        self.nodeNeighbors : list = None
        # nodeWeight initialize
        self.nodeWeight : list = None
        # nodeGraph initialoze
        self.nodeGraph : nx.Graph = None
        # Dataframe of graph 
        self.grapExcel : pd.DataFrame = None
        # Dataframe of graph neighbors
        self.neighborsExcel : pd.DataFrame = None
        # Dataframe of graph weight
        self.weightExcel : pd.DataFrame = None


    def generate(self,numGen : int):
        """Generate a number of node base on input"""

        self.node = []

        # looping in range of input
        for i in range(numGen):
            # make a 4 values in list base on number, label, X axis, and Y axis
            self.node.append([1 + i, str(f'N{i + 1}'), self.nodePosVal[np.random.randint(0,19)],self.nodePosVal[np.random.randint(0,19)]])
    
        # return form the looping
        return self.node

    def neighbors(self):
        """check all connection between one node and another"""

        # Check if the node already been create if not the return / out imidieatly
        if self.node == None:
            return None
        
        # initiate base
        N = len(self.node)
        test = []
        self.nodeNeighbors = np.zeros((N,N), dtype="int")

        # looping all the neigbors this is only initialize state
        # for i in range(len(self.node) + 1):
        #     temp = []

        #     for j in range(len(self.node) + 1):
        #         temp.append(0)
        #     self.nodeNeighbors.append(temp)
        
        for i in range(len(self.node)):
            test.append(i)
        
        # check all connection in node
        for i in range(len(self.node)):
            for j in range(3):
                p1 = np.random.choice(test)
                pointer1, pointer2 = sum(self.nodeNeighbors[i]),sum(self.nodeNeighbors[p1])

                if pointer1 > 5:
                    test = [el for el in test if el != i]
                elif pointer2 > 5:
                    test = [el for el in test if el != p1]
                elif i != p1:
                    self.nodeNeighbors[i][p1] = 1
                    self.nodeNeighbors[p1][i] = 1
        
        return self.nodeNeighbors
    
    def weight(self):
        if self.node == None and self.nodeNeighbors == None and self.grapExcel == None:
            return

        N = len(self.node)
        
        self.nodeWeight = np.zeros((N,N), dtype="float64")
        
        # self.nodeWeight = []

        # for i in range(len(self.node) + 1):
        #     temp = []
        #     for j in range(len(self.node)):
        #         temp.append(0)
        #     self.nodeWeight.append(temp)
        
        for i in range(len(self.node)):
            for j in range(i):
                if self.nodeNeighbors[i][j] == 1:
                    print(j, i, sep=" ")
                    calculate = np.round(np.sqrt((self.node[j][2] - self.node[i][2])**2 + (self.node[j][3] - self.node[j][3])**2),2)
                    self.nodeWeight[i][j] = calculate
                    self.nodeWeight[j][i] = calculate

        
        
        return self.nodeWeight
    
    def graph(self):

        N = len(self.node)

        self.nodeGraph = nx.Graph()

        for i in range(N):
            for j in range(i):
                if self.weightExcel[i][j] > 0:
                    self.nodeGraph.add_weighted_edges_from([(i,j,self.nodeWeight[i,j])])
        
        return self.nodeGraph

    def grapToExcel(self):
        """Convert the previous node into a DataFrame"""
        if self.node == None:
            return
        
        df = pd.DataFrame(self.node, columns=["No", "Label", "X", "Y"])
        self.grapExcel = df
        return df
    
    def neighborsToExcel(self):
        """Generate an neigbors to Dataframe"""

        # Check if node neighbors already been created
        # if self.nodeNeighbors == None:
        #     return

        label = [f'N{i}' for i in range(len(self.node))]
        
        self.neighborsExcel = pd.DataFrame(self.nodeNeighbors, columns=label)
        self.neighborsExcel.index = label
        return self.neighborsExcel
    
    def weightToExcel(self):
        """Generate node weight to Dataframe"""

        # Check if weight already been create
        # if self.nodeWeight == None:
        #     return

        label = [f'N{i}' for i in range(len(self.node))]

        self.weightExcel = pd.DataFrame(self.nodeWeight, columns=label)
        self.weightExcel.index = label
        
        return self.weightExcel
    
    def printExcel(self, dir : str = None):
        """Print all grap node and it's neighbors into excel"""

        # Check if node neighbors and node itself already been created
        # if self.grapExcel == None or self.neighborsExcel == None:
        #     return
        
        if dir == None:
            if "excel" not in os.listdir('../TugasSearch'):
                os.mkdir("../TugasSearch/excel")
                self.grapExcel.to_excel(f'excel/graph.xlsx')
                self.neighborsExcel.to_excel(f'excel/neighbors.xlsx')
                self.weightExcel.to_excel(f'excel/weight.xlsx')
            else:
                self.grapExcel.to_excel(f'excel/graph.xlsx')
                self.neighborsExcel.to_excel(f'excel/neighbors.xlsx')
                self.weightExcel.to_excel(f'excel/weight.xlsx')
        else:
            self.grapExcel.to_excel(f'{dir}/graph.xlsx')
            self.neighborsExcel.to_excel(f'{dir}/neighbors.xlsx')
            self.weightExcel.to_excel(f'{dir}/weight.xlsx')

    def bfs(self,graph_to_search, start, end):
        queue = [[start]]
        visited = set()

        while queue:
            # Gets the first path in the queue
            path = queue.pop(0)

            # Gets the last node in the path
            vertex = path[-1]

            # Checks if we got to the end
            if vertex == end:
                return path
                
            # We check if the current node is already in the visited nodes set in order not to recheck it
            elif vertex not in visited:
                # enumerate all adjacent nodes, construct a new path and push it into the queue
                for current_neighbour in graph_to_search.get(vertex, []):
                    new_path = list(path)
                    new_path.append(current_neighbour)
                    queue.append(new_path)

                # Mark the vertex as visited
                visited.add(vertex)


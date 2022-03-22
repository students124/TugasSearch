from csv import list_dialects
import os
import pandas as pd
import numpy as np

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
        test = []
        self.nodeNeighbors = []

        # looping all the neigbors this is only initialize state
        for i in range(len(self.node) + 1):
            temp = []

            for j in range(len(self.node) + 1):
                temp.append(0)
            self.nodeNeighbors.append(temp)
        
        for i in range(len(self.node) + 1):
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
        
        self.nodeWeight = []

        for i in range(len(self.node) + 1):
            temp = []
            for j in range(len(self.node)):
                temp.append(0)
            self.nodeWeight.append(temp)
        
        for i in range(len(self.node) + 1):
            for j in range(i + 1):
                if self.nodeNeighbors[i][j] == 1:
                    calculate = np.round(np.sqrt((self.grapExcel[j][2] - self.grapExcel[i][2])**2 + (self.grapExcel[j][3] - self.grapExcel[j][3])**2),4)
                    self.nodeWeight[i][j] = calculate
                    self.nodeWeight[j][i] = calculate
        
        return self.nodeWeight

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
        if self.nodeNeighbors == None:
            return

        label = [f'N{i}' for i in range(len(self.node) + 1)]
        
        self.neighborsExcel = pd.DataFrame(self.nodeNeighbors, columns=label)
        self.neighborsExcel.index = label
        return self.neighborsExcel
    
    def weightToExcel(self):
        """Generate node weight to Dataframe"""

        # Check if weight already been create
        if self.nodeWeight == None:
            return
        
        self.weightExcel = pd.DataFrame(self.nodeWeight)
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
            else:
                self.grapExcel.to_excel(f'excel/graph.xlsx')
                self.neighborsExcel.to_excel(f'excel/neighbors.xlsx')
        else:
            self.grapExcel.to_excel(f'{dir}/graph.xlsx')
            self.neighborsExcel.to_excel(f'{dir}/neighbors.xlsx')
    

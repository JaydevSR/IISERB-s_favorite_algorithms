import numpy as np
import graphviz

## Defining classes for vertex and Graph

class vertex :
    def __init__(self,distance = 0,pre = 0):
        self.d = distance
        self.p = pre


class Graph :
    
    
    def __init__(self,vertices = 0,edges = 0):

        self.vertices = vertices
        self.edges = edges
   
    
    def single_source(self,j):
        k = list(self.edges.values())
        k = np.array(k)
        k = abs(k)
        max_edge = k.sum()
        for i in self.vertices:
            self.vertices[i].d = max_edge+1
        self.vertices[j].d = 0
        return None
            
    
    def relax(self,j):
        if self.vertices[int(j[3])].d > self.vertices[int(j[1])].d + self.edges[j]:
           self.vertices[int(j[3])].d = self.vertices[int(j[1])].d + self.edges[j]
           self.vertices[int(j[3])].p = int(j[1])
           return None
             
        
    def bellman_ford(self, j):
        self.single_source(j)
        for i in range(len(self.vertices) - 1):
            for i in self.edges:
                self.relax(i)
        for i in self.edges:
            if self.vertices[int(i[3])].d > self.vertices[int(i[1])].d + self.edges[i]:
                return False
        return self.vertices

# Taking inputs for edges and vertices for graph in order to perform Bellman Ford.
num_vertices = int(input('Input the number of vertices in the graph: '))

dict_vertices = {}

for i in range(1,num_vertices + 1):
    dict_vertices[i] = vertex()
 
d = input('The name of the vertices is numeric that is from 1 to n where n is the number of vertices.\nPress any key to continue : ')


def add_edges():
    
    invalid = 'Invalid Input, start again !'
    dict_edges = {}
    f = input('Now you have to input the details for different edges in the graph.\nPress any key to stop giving details (press c to continue): ')
    
    
    if f == 'c':
        k = True
        while k == True:
    
            edge_in= input('Start vertex of edge : ')
            if edge_in.isnumeric() != True :
                break
            
            edge_out = input('End vertex of the edge : ')
            if edge_out.isnumeric() != True:
                break
            
            weight_edge = int(input('Weight of the edge: '))
            if (str(abs(weight_edge))).isnumeric() != True:
                break
            edge_tuple= '(' + edge_in + ',' + edge_out + ')'
            
            if int(edge_tuple[1]) > num_vertices or int(edge_tuple[3]) > num_vertices:
                print(invalid)
                dict_edges = add_edges()
                return dict_edges
            
            dict_edges[edge_tuple] = weight_edge
            print(edge_tuple)
    else:
        dict_edges = add_edges()
        return dict_edges

    return dict_edges
    

dict_edges_2 = add_edges()
g = Graph(vertices = dict_vertices,edges=dict_edges_2)
s = input('Select the vertex that you want to be the source vertex: ')
g.bellman_ford(int(s))

## Plotting the Minimum Spanning Tree obtained by Bellman Ford 

f = graphviz.Digraph('finite_state_machine', filename ='bellman_ford.gv')
f.attr(rankdir ='LR', size = '8,5')
f.attr('node', shape = 'circle')

for i in g.vertices:
    if g.vertices[i].p == 0:
        continue
    else:
        f.edge(str(g.vertices[i].p),str(i),label = str(g.edges['({},{})'.format(g.vertices[i].p,i)]))


f.view()    

   

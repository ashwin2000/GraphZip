#We have the initial graph which we encode into the file 
#by using edge lists

class Edge_Graph:

    def __init__(self):
        self.visited_node={}
        self.graph={}

    #Returns the vertices in the graph
    def vertex_list(self):
        return list(self.graph.keys())

    #Returns if node has been visited
    def go(self,vertex_id):
        return self.visited_node[vertex_id]
    
    #Returns size of the graph
    def size_of_graph(self):
        return len(self.graph)

    #Function to add new edges
    def edge_append(self,vertex_id,edge):
        if vertex_id not in self.graph.keys():          
            self.visited_node[vertex_id]=0
            self.graph[vertex_id]=[]
        self.graph[vertex_id].append(edge)
    
    def set_visit(self,vertex_id):
        self.visited_node[vertex_id]=1

    #returns the edges in a graph
    def reveal_graph(self):
        return self.graph

    #deletes a node from the graph
    def remove_node(self,node):
        i=0
        while i in self.graph[node].keys():
            self.graph[i].pop(node)
        self.graph.pop(node)
    
    #returns the degree of the vertex
    def ret_degree(self,vertex_id):
        return len(self.graph[vertex_id])

    #returns all the vertices which we have visited
    def disp_route(self):
        return self.visited_node
    
    #returns the graph in a matrix form
    def matrix(self):        
        self.mat=[]
        i=0
        while i in self.graph:
            self.mat.append([0 for k in range(len(self.graph))])
            for j in self.graph[i]:        
                self.mat[i-1][j-1]=1
        return self.mat

    #returns the neighbours of a vertex
    def edge_list(self,vertex_id):
        return list(self.graph[vertex_id])
    
    #encodes the graph into a text file
    def encode(self):
        file=open("edge_list.txt","w")
        for i in self.graph.keys():
            for j in self.graph[i]:
                file.write(str(i)+","+str(j)+'\n')
        file.close()

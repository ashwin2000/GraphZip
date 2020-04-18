#we have to demonstrate our method of using cliques is 
#more memory efficient so we use another class
#The other class stores the cliques in a more efficient manner 

from edge_graph import Edge_Graph
#we need to import the previous class so that we can
#use its object here for calculating cliques

class Clique_Graph:
    def __init__(self):
        self.clique_list=[]                   #list of cliques
        self.graph={}                         #structure of the graph

    #this function reads the text file in which the graph has been encoded and 
    #then constructs our graph
    def decode(self,EG):
        file=open("edge_list.txt","r")
        line=file.readline()
        while(line):
            v1,v2=map(int,line.split(','))
            if v1 not in self.graph.keys():     
                self.graph[v1]=[]
            self.graph[v1].append(v2)
            line=file.readline()
        self.clique_list=list(self.bron_kerbosch(EG,P=set(EG.vertex_list())))
        self.clique_list=[i for i in self.clique_list if len(i)>2]    
    
    #we use this algorithm to find all the maximal cliques in the graph
    #which have a size above 2
    def bron_kerbosch(self,EG,R=set(),P=set(),X=set()):
        if not P and not X:
            yield R
        while P:
            v=P.pop()
            yield from self.bron_kerbosch(EG,
                                    R.union([v]),
                                    P.intersection(EG.edge_list(v)),
                                    X.intersection(EG.edge_list(v)))
            
            X.add(v)

    def view_cliques(self):
        return self.clique_list

    def view_graph(self):
        return self.graph

    #this function encodes the graph into the clique format and
    #in doing so saves us some memory
    def encode(self):
        file=open("edge_list.txt","r")
        fwrite=open("clique_edge_list.txt","w")
        line=file.readline()
        for i in self.clique_list:
            for j in i:
                fwrite.write(str(j)+",")
            fwrite.write('\n')
        while(line):
            v1,v2=map(int,line.split(','));flag=1
            for i in self.clique_list:
                if v1 in i and v2 in i:
                    flag=0
            if(flag!=0):
                fwrite.write(str(v1)+","+str(v2)+"\n")
            line=file.readline()

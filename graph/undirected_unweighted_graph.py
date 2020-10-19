class Graph:
    def __init__(self):
        self.numberOfVertices = 0
        self.adjacentLists = {}

    def addVertex(self, vertex):
        self.adjacentLists[vertex] = []
        self.numberOfVertices += 1

    # Undirected unweighted graph
    def addEdge(self, vertex1, vertex2):
        self.adjacentLists[vertex1].append(vertex2)
        self.adjacentLists[vertex2].append(vertex1)

    def showConnections(self):
        for vertex in self.adjacentLists:
            print(vertex, end= '-->')
            for adj in self.adjacentLists[vertex]:
                print(adj, end= ' ')
            print()

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()
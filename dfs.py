class Graph:
    def __init__(self):
        self.edges = list()
        self.vertices = list()


    def addEdge(self, fromVertex, toVertex):
        if fromVertex not in self.vertices:
            self.vertices.append(fromVertex)
        if toVertex not in self.vertices:
            self.vertices.append(toVertex)
        self.vertices.sort()

        try:
            self.edges[fromVertex].append(toVertex)
            self.edges[fromVertex].sort()
        except IndexError:
            while len(self.edges) <= fromVertex:
                self.edges.append([])
            self.edges[fromVertex].append(toVertex)
            self.edges[fromVertex].sort()

    def DFS(self, startVertex):
        stack = [startVertex]
        visited = list()
        while len(stack):
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                if len(self.edges) > vertex:
                    stack.extend(self.edges[vertex])
        print(visited)

    def BFS(self, startVertex):
        queue = [startVertex]
        visited = list()
        while len(queue):
            vertex = queue[0]
            queue  = queue[1:]
            if vertex not in visited:
                visited.append(vertex)
                if len(self.edges) > vertex:
                    queue.extend(self.edges[vertex])
        print(visited)

    def disp(self):
        print(self.vertices)
        print(self.edges)


g = Graph()
g.addEdge(1, 2)
# g.addEdge(0, 2)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(3, 4)
# print(g.edges[0])
g.BFS(0)

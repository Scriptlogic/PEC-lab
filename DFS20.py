class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def DFS(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                if node in self.graph:
                    for neighbour in reversed(self.graph[node]):
                        if neighbour not in visited:
                            stack.append(neighbour)

g = Graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Depth First Traversal (starting from vertex 2)")
g.DFS(2)
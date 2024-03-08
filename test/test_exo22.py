class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_edge(self, node, neighbors):
        self.graph_dict[node] = neighbors

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph_dict[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

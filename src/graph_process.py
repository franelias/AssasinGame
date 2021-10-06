

from networkx.classes.graph import Graph


class GraphProcess:
    def __init__(self, graph: Graph, maxDistance):
        self.graph = graph
        self.maxDistance = maxDistance

    def adjustGraph(self):
        delete = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                if self.graph[node][neighbor]["distance"] > self.maxDistance:
                    delete.append((node, neighbor))

        self.graph.remove_edges_from(delete)

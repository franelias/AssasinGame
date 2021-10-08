class GraphProcess:
    def __init__(self, graph):
        self.graph = graph

    def adjustGraph(self):
        for _ in self.graph:
            self.graph.neighbor = sorted(
                self.graph.neighbor, key=lambda k: k[1])

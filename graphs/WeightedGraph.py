from graphs.WeightedEdge import WeightedEdge

class WeightedGraph:

    def __init__(self, V):
        """
        Constructor responsible to initialize the WeightedGraph structure
        # Graph based on 0-index array (e.g Graph(3) == V{0, 1, 2})

        Args:
            param1: V is the number of vertices of the Graph
        
        Raises:
            TypeError: V is not an integer
        """
        try:
            self._V = V
            self._adj = [[] for i in range(self._V)]
        except TypeError:
            pass

    def add_edge(self, v, w, weight):
        """
        Method responsible for adding an weight edge in an undirected style

        Args:
            param1: v is the first vertice
            param2: w is the second vertice
            param2: weight of the edge
        
        Raises:
            TypeError: v is not an integer
            IndexError: v is out of bounds
        """
        
        try:
            edge = WeightedEdge(v, w, weight)
            self._adj[v].append(edge)
            self._adj[w].append(edge)

        except (TypeError, IndexError):
            pass
            
    def len(self):
        """
        Method responsible for returning the length (# of vertices)
        """
        return self._V

# WeightedGraph.py

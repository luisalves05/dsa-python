
import sys
sys.path.append('..')

import unittest
from graphs.Graph import Graph
from graphs.BFS import BFS

class TestBFS(unittest.TestCase):

    def setUp(self):
        self.G = Graph(6) 
        self.G.add_edge(1, 2)
        self.G.add_edge(1, 3)
        self.G.add_edge(1, 4)
        self.G.add_edge(2, 4)
        self.G.add_edge(3, 4)
        self.G.add_edge(0, 5)
    
    def testing_path_to(self):
        bfs = BFS(self.G, 4)
        self.assertEqual(bfs.path_to(self.G, 1), [1, 4])
        self.assertEqual(bfs.path_to(self.G, 2), [2, 4])    
        self.assertEqual(bfs.path_to(self.G, 0), None)
        
    def testing_has_path_to(self):
        bfs = BFS(self.G, 4)    
        self.assertEqual(bfs.has_path_to(self.G, 1), True)
        self.assertEqual(bfs.has_path_to(self.G, 2), True)
        self.assertEqual(bfs.has_path_to(self.G, 0), False)

if __name__ == "__main__":
    unittest.main()

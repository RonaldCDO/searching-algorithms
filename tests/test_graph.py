import unittest
from data_structure.graph import Graph

class TestGraph(unittest.TestCase):
    def test_agg_edge(self):
        graph = Graph()
        graph.add_edge(u='A', v='B')
        self.assertIn('A', graph.graph)
        self.assertIn('B', graph.graph['A'])

    def test_graph_structure(self):
        graph = Graph()
        graph.add_edge(u='A', v='B')
        graph.add_edge(u='A', v='C')
        expected = {'A': ['B', 'C']}
        self.assertEqual(dict(graph.graph), expected)

    def test_print_graph(self):
        graph = Graph()
        graph.add_edge(u='X', v='Y')

        from io import StringIO
        from unittest.mock import patch

        with patch('sys.stdout', new=StringIO()) as fake_out:
            graph.print_graph()
            self.assertIn('X -> Y', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()

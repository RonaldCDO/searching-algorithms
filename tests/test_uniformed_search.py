import unittest
from search_algorithm.uninformed_search import USearch
from io import StringIO
from unittest.mock import patch


class TestUniformedSearch(unittest.TestCase):
    def test_dfs(self):
        graph = USearch()
        graph.add_edge(u='A', v='B')
        graph.add_edge(u='A', v='C')
        graph.add_edge(u='B', v='C')
        graph.add_edge(u='B', v='D')
        graph.add_edge(u='C', v='D')
        with patch('sys.stdout', new=StringIO()) as fake_out:
            graph.dfs('A')
            self.assertIn('A B C D', fake_out.getvalue())
            graph.dfs('B')
            self.assertIn('B C D', fake_out.getvalue())
            graph.dfs('C')
            self.assertIn('C D', fake_out.getvalue())


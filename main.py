from search_algorithm.uninformed_search import USearch

def main() -> None:
    graph = USearch()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'E')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'A')
    graph.add_edge('C', 'D')
    graph.add_edge('D', 'E')
    graph.dfs('B')



if __name__ == "__main__":
    main()

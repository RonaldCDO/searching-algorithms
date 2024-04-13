from collections import defaultdict
from typing import Dict, List

class Graph:
    def __init__(self):
        self.graph: Dict[str, List[str]] = defaultdict(list)

    def add_edge(self, u: str, v: str) -> None:
        self.graph[u].append(v)

    def print_graph(self) -> None:
        for node in self.graph:
            for neighboor in self.graph[node]:
                print(f"{node} -> {neighboor}")

from data_structure.graph import  Graph

class USearch(Graph):
    def dfs_util(self, v: str, visited_stack: set):
        visited_stack.add(v)
        print(v, end= ' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited_stack:
                self.dfs_util(v=neighbour, visited_stack=visited_stack)

    def dfs(self, v: str):
        visited_stack = set()

        self.dfs_util(v=v, visited_stack=visited_stack)

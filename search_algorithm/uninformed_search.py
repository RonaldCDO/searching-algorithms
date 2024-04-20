from data_structure.graph import  Graph

class USearch(Graph):
    def dfs_util(self, v: str, visited_arr: set):
        visited_arr.add(v)
        print(v, end= ' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited_arr:
                self.dfs_util(v=neighbour, visited_arr=visited_arr)

    def dfs(self, v: str):
        visited_arr = set()

        self.dfs_util(v=v, visited_arr=visited_arr)

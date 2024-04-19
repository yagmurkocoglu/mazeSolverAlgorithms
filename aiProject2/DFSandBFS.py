from queue import Queue, LifoQueue

class SearchAlgorithm:
    def __init__(self, is_dfs=False):
        if is_dfs:
            self.frontier = LifoQueue()
        else:
            self.frontier = Queue()
        self.maxLenOfFrontier = 0

    def operate(self):
        node = self.frontier.get()
        return node

    def append(self, node):
        self.frontier.put(node)
        if self.getLengthOfFrontier() > self.maxLenOfFrontier:
            self.maxLenOfFrontier = self.getLengthOfFrontier()

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)

# Kullanım
search_algo_dfs = SearchAlgorithm(is_dfs=True)
search_algo_bfs = SearchAlgorithm()

# BFS
search_algo = search_algo_bfs
# DFS
search_algo = search_algo_dfs

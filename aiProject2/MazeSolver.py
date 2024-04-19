from A_star_search import A_StarSearch
from DFSandBFS import SearchAlgorithm
from greedy_best_first_search import GreedyBestFirstSearch
from uniform_cost_search import UniformCostSearch
from graph_search import GraphSearch
from IO import IO
from iterative_deepening_search import IterativeDeepeningSearch

#dfs23
#bfs23
#ucs18
#a*18
#ıds23
#greedy23

class MazeSolver:
    def __init__(self, filename):
        self.grid, self.goalNodes, self.startState = IO().readTheMazeInput(filename)

    def solve_maze(self, strategy):
        graph_search = GraphSearch(strategy, self.grid.copy(), self.startState, self.goalNodes)
        graph_search.search()
        return graph_search

    def print_solution(self, graph_search, strategy_name):
        print(f"Strategy Name: {strategy_name}")
        print(f"Cost of Solution: {graph_search.cost}")
        print("Solution Path: ", end="")
        graph_search.printPath(graph_search.lastNode)
        print(f"\nExpanded Nodes: {len(graph_search.exploredSet)}")
        print("\n" + "-" * 30)

    def run_all_strategies(self):
        strategies = {
            "DFS": SearchAlgorithm(is_dfs=True),
            "BFS": SearchAlgorithm(),
            "IDS": IterativeDeepeningSearch(),
            "Uniform Cost": UniformCostSearch(),
            "Greedy Best": GreedyBestFirstSearch(),
            "A*": A_StarSearch()
        }

        for strategy_name, strategy in strategies.items():
            graph_search = self.solve_maze(strategy)
            self.print_solution(graph_search, strategy_name)


if __name__ == "__main__":
    print("Maze Solving Strategies Comparison\n")
    maze_solver = MazeSolver('given_input.json')
    maze_solver.run_all_strategies()

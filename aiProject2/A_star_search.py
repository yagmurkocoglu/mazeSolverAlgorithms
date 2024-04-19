from queue import PriorityQueue as PQ


class A_StarSearch:
    def __init__(self):
        self.frontier = PQ()
        self.maxLenOfFrontier = 0

    def operate(self):
        node = self.frontier.get()
        return node[1]

    def append(self, node):
        self.frontier.put((node.heuristicCost + node.cost, node))
        if self.getLengthOfFrontier() > self.maxLenOfFrontier:
            self.maxLenOfFrontier = self.getLengthOfFrontier()

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        retList = []
        priorityQIterator = list(self.frontier.queue)
        for frtNode in priorityQIterator:
            retList.append(frtNode[1])
        return retList

    def calculateHeuristicValues(self, grid, goalSquares):
        for row in grid:
            for node in row:
                for goalNode in goalSquares:
                    total = abs(node.verticalIndex - goalNode.verticalIndex) + abs(node.horizontalIndex - goalNode
                                                                                   .horizontalIndex)
                    if total < node.heuristicCost:
                        node.heuristicCost = total

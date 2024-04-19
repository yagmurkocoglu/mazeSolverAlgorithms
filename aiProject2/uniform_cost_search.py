from queue import PriorityQueue as PQ


class UniformCostSearch:
    def __init__(self):
        self.frontier = PQ()

    def operate(self):
        if not self.frontier.empty():
            node = self.frontier.get()
            return node[1]
        else:
            return None

    def append(self, node):
        self.frontier.put((node.cost, node))

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        retList = []
        priorityQIterator = list(self.frontier.queue)
        for frtNode in priorityQIterator:
            retList.append(frtNode[1])
        return retList

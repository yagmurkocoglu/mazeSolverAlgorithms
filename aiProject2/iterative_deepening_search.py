from queue import LifoQueue as LQ


class IterativeDeepeningSearch:
    def __init__(self):
        self.frontier = LQ()

    def operate(self):
        if not self.frontier.empty():
            node = self.frontier.get()
            return node
        else:
            return None

    def append(self, node):
        self.frontier.put(node)

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)

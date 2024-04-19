import json
import math

class Node:
    def __init__(self, status, eastWall, westWall, northWall, southWall, verticalIndex, horizontalIndex):
        self.status = status
        self.eastWall = eastWall
        self.westWall = westWall
        self.northWall = northWall
        self.southWall = southWall
        self.verticalIndex = verticalIndex
        self.horizontalIndex = horizontalIndex
        self.cost = 0
        self.successor = None
        self.heuristicCost = math.inf

    def __gt__(self, other):
        if self.cost > other.cost:
            True
        else:
            False


class IO:

    def readTheMazeInput(self, fileName):
        try:
            with open(fileName) as f:
                data = json.load(f)

                if "nodes" not in data or "horizontal" not in data:
                    raise ValueError("Invalid file format: 'nodes' and 'horizontal' must be present.")

                nodes = data["nodes"]
                horizontal = data["horizontal"]
                goalSquares = []
                nodeList = []
                nodeRow = []
                startNode = []
                j = 0
                i = 0

                for node in nodes:
                    nodeRow.append(Node(node["status"], node["eastWall"],
                                        node["westWall"], node["northWall"],
                                        node["southWall"], j, i))
                    i += 1
                    if nodeRow[-1].status == 'S':
                        startNode = [nodeRow[-1].verticalIndex, nodeRow[-1].horizontalIndex]
                    if nodeRow[-1].status == 'G':
                        goalSquares.append(nodeRow[-1])
                    if i == horizontal:
                        nodeList.append(nodeRow.copy())
                        nodeRow.clear()
                        i = 0
                        j += 1

                return nodeList, goalSquares, startNode

        except FileNotFoundError:
            print(f"Error: File '{fileName}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file '{fileName}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return None, None, None  # Dosya okuma işlemi başarısız olduğunda None döndür

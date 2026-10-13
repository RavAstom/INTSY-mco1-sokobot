def is_solved(boxes, goals):
    for box in boxes:
        if box not in goals:
            return False
    return True


def heuristic(boxes, goals):
    total = 0
    for box in boxes:
        closest = None
        for goal in goals:
            distance = abs(box[0] - goal[0]) + abs(box[1] - goal[1])
            if closest is None or distance < closest:
                closest = distance
        total += closest
    return total


def dead_squares(width, height, walls, goals):
    dead = set()
    for row in range(height):
        for col in range(width):
            if (row, col) in walls or (row, col) in goals:
                continue
            wall_up = (row - 1, col) in walls
            wall_down = (row + 1, col) in walls
            wall_left = (row, col - 1) in walls
            wall_right = (row, col + 1) in walls
            if (wall_up or wall_down) and (wall_left or wall_right):
                dead.add((row, col))
    return dead
    
# Some sort of state thingy (don't know if this would work for us)

def __init__(self, value, parent,
                 start = 0,
                 goal = 0):

        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path[:]
            self.path.append(value)
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

class aStar_solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal
    
    
    
    def solve(self):
        
        # pretent startState mean something
    
        count = 0
        self.priorityQueue.put((0,count,startState))
        
        while(not self.path and self.priorityQueue.qsize()):
           # something 
    

class SokoBot:
    def solveSokobanPuzzle(self, width, height, mapData, itemsData):
        player = None
        boxes = []
        goals = []
        walls = set()

        for row in range(height):
            for col in range(width):
                tile = itemsData[row][col]
                if tile == '@':
                    player = (row, col)
                elif tile == '$':
                    boxes.append((row, col))

                if mapData[row][col] == '.':
                    goals.append((row, col))
                elif mapData[row][col] == '#':
                    walls.add((row, col))

        print("player:", player)
        print("boxes:", boxes)
        print("goals:", goals)
        print("walls:", sorted(walls))
        print("solved:", is_solved(boxes, goals))
        print("heuristic:", heuristic(boxes, goals))
        print("dead squares:", sorted(dead_squares(width, height, walls, goals)))

        return ""

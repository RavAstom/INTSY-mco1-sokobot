import heapq

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
    alive = set(goals)
    to_visit = list(goals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(to_visit) > 0:
        current = to_visit.pop()
        for d_row, d_col in directions:
            box = (current[0] + d_row, current[1] + d_col)
            player = (current[0] + 2 * d_row, current[1] + 2 * d_col)
            if box in alive or box in walls or player in walls:
                continue
            if player[0] < 0 or player[0] >= height or player[1] < 0 or player[1] >= width:
                continue
            alive.add(box)
            to_visit.append(box)

    dead = set()
    for row in range(height):
        for col in range(width):
            if (row, col) not in walls and (row, col) not in alive:
                dead.add((row, col))
    return dead

class aStar_solver:
    def __init__(self, player, boxes, goals, walls, dead):

        self.player = player
        self.boxes = sorted(boxes)
        self.goals = goals
        self.walls = walls
        self.dead = dead

    def solve(self):
        start_f = heuristic(self.boxes, self.goals)
        open_list = [[start_f, 0, self.player, self.boxes, ""]]
        heapq.heapify(open_list)
        visited = {}
        visited[(self.player, tuple(self.boxes))] = 0

        while len(open_list) > 0:
            current = heapq.heappop(open_list)

            g = current[1]
            player = current[2]
            boxes = current[3]
            path = current[4]

            if is_solved(boxes, self.goals):
                return path

            moves = [("u", -1, 0), ("d", 1, 0), ("l", 0, -1), ("r", 0, 1)]

            for move in moves:
                letter = move[0]
                next_pos = (player[0] + move[1], player[1] + move[2])

                if next_pos in self.walls:
                    continue

                new_boxes = list(boxes)
                if next_pos in boxes:
                    beyond = (next_pos[0] + move[1], next_pos[1] + move[2])
                    if beyond in self.walls or beyond in boxes or beyond in self.dead:
                        continue
                    new_boxes.remove(next_pos)
                    new_boxes.append(beyond)
                    new_boxes.sort()

                key = (next_pos, tuple(new_boxes))
                new_g = g + 1
                if key not in visited or new_g < visited[key]:
                    visited[key] = new_g
                    new_f = new_g + heuristic(new_boxes, self.goals)
                    heapq.heappush(open_list, (new_f, new_g, next_pos, new_boxes, path + letter))

        return ""

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

        dead = dead_squares(width, height, walls, goals)
        solver = aStar_solver(player, boxes, goals, walls, dead)
        return solver.solve()

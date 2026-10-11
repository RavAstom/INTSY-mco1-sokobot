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

        return ""
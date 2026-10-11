def is_solved(boxes, goals):
    for box in boxes:
        if box not in goals:
            return False
    return True


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

        return ""
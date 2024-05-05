import random

def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]
    stack = [(1, 1)]
    maze[1][1] = " "
    while stack:
        x, y = stack[-1]
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 < nx < width-1 and 0 < ny < height-1 and maze[ny][nx] == "#"]
        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            maze[ny][nx] = " "
            maze[(ny + y) // 2][(nx + x) // 2] = " "
            stack.append((nx, ny))
        else:
            stack.pop()
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    width, height = 21, 21
    maze = generate_maze(width, height)
    print_maze(maze)

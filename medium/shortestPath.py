"""
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at a food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

"""
from collections import deque
def shortestPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    start = None
    dist = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "*":
                start = (i,j)
                break

    q = deque([start, dist])
    visited = set()
    while q:
        (x,y), dist = q.popleft()

        if x<0 or x>=rows or y<0 or y>=cols:
            continue

        if (x,y) in visited:
            continue
        else:
            visited.add((x,y))

        if matrix[x][y] == "X":
            continue

        if matrix[x][y] == "#":
            return dist

        q.append(((x+1,y), dist+1))
        q.append(((x-1,y), dist+1))
        q.append(((x,y+1), dist+1))
        q.append(((x,y-1), dist+1))
    return -1



# OTHER SOLUTION

# def getFood(grid):
        
#     rows = len(grid)
#     cols = len(grid[0])
#     start = None 
#     dist = 0
        
#     for i in range(rows):
#       for j in range(cols):
#         if grid[i][j] == "*":
#           start = ((i,j))
#           break
                    
#     q = deque([(start,dist)])
#     visited = set()
  
#     while q:        
#       (x,y),dist = q.popleft()
#       for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
#         new_x = x+a
#         new_y = y+b
            

#         if 0<=new_x<rows and 0<=new_y<cols:
#           if grid[new_x][new_y] == "#":
#             return dist+1
            
#           if grid[new_x][new_y] == 'O':
#             q.append(((new_x,new_y) ,dist+1))

              
#           if (new_x,new_y) in visited:
#             continue
#           else:
#             visited.add((new_x,new_y))          

        
#     return -1
# print(getFood( [["X","*"],["#","X"]]))



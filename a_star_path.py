from random import randint 

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position  
        self.dFromS = 0 #distance from start
        self.estimateDistance = 0 #estimated distance
        self.cost = 0 #cost of trying that route  

    def __eq__(self, other): 
        return self.position == other.position #overrides comparision amongst nodeA == nodeB 


def astar(maze, start, end):
  #___________setup phase______________________
  start_node = Node(None, start)
  start_node.dFromS = start_node.estimateDistance = start_node.cost = 0
  end_node = Node(None, end)
  end_node.dFromS = end_node.estimateDistance = end_node.cost = 0

   
  open_list = []
  closed_list = []
  open_list.append(start_node)
  
  while len(open_list) > 0:
    current_node = open_list[0]
    current_index = 0
    #______________evaluation phase___________
   
    for index, item in enumerate(open_list):
        if item.cost < current_node.cost:
            current_node = item
            current_index = index
    open_list.pop(current_index)
    closed_list.append(current_node)

    if current_node == end_node:
        path = []
        current = current_node
        while current is not None:
          path.append(current.position)
          current = current.parent
        return path[::-1] 
    #_______________discovery phase_______________
    
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
      node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
      if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
          continue
      if maze[node_position[0]][node_position[1]] != ".":
          continue
      # Create new node for discovering 
      new_node = Node(current_node, node_position)
      # Add to children the new node (discovering)
      children.append(new_node)
    for child in children:
      for closed_child in closed_list:
        if child == closed_child:
            continue
          
      # ___________frontier phase____________________
     
      # Create all needed values
      child.dFromS = current_node.dFromS + 1
      child.estimateDistance = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
      child.cost = child.dFromS + child.estimateDistance
      # Child is already in the open list
      for open_node in open_list:
          if child == open_node and child.dFromS > open_node.dFromS:
              continue
      # Add the child to the open list
      open_list.append(child)
      
# ___________________________BUILD AND DRAW MAP_____________________________          
def build(r,c):
    return [["." for j in range(c)] for i in range(r)]
  
def createLevel(rowSize, colSize): #random map generator 
  level = build(rowSize,colSize)
  walls = [randint(0, len(level)-1), randint(0, len(level)-1), randint(0, len(level)-1),randint(0, len(level)-1) ]
  for each in walls:
    level[each] = ["#" if randint(0,1) == 1 else "." for i in range(len(level[each]))]
    level[each-randint(0, len(level)-1)] = ["#" if randint(0,1) == 1 else "." for i in range(len(level[each]))]
  return level

def draw(level):
  for i in range(len(level)):
    print " ".join(level[i])
    
    
def drawTrail(maze,path):
  for i in range(len(path)):
    x,y = path[i]
    maze[x][y] = "@"



maze = createLevel(20,20)
start = (0, 0) #start of Map
end = (len(maze)-1, len(maze)-1) #end of Map




path = astar(maze, start, end)
drawTrail(maze, path)
draw(maze)






    

#DFS


def findAllPossibles(graph, start):
  #create a empty set and list with start point
  visited, stack = set(), [start] 
  while stack:
    vertex = stack.pop() #set to top of stack
    if vertex not in visited:
      visited.add(vertex)
      #subtract the visited from the next node-set and 
      #push to stack all remaining nodes.
      stack.extend(graph[vertex]- visited) 
  return visited
  
  
def findPathBetween(graph, start, end):
  stack, paths = [(start, [start])], []         # use tuple to create a psuedo node (could of used class Node object instead).
  while stack:
    (vertex, path) = stack.pop() #set to top of stack
    
    # traverse only nodes not in path already
    for node in graph[vertex]- set(path):
      if node == end:
        paths.append((node, path + [node]))# found end. store for return
      else:
        stack.append((node, path+[node])) # add to stack existing path and recuse to next loop
  return paths
        

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Driver Code 
if __name__ == "__main__": 
	
	# Graph using dictionaries 
	graph = {'A': ['B', 'C', 'D', 'E'],
         'B': ['F','G'],
         'C': ['H'],
         'D': ['I','J'],
         'E': [],
         'F': [],
         'G': ['K','L'],
         'H': [],
         'I': ['M'],
         'J': ['N'],
         'K': [],
         'L': ['O'],
         'M': [],
         'N': [],
         'O': []
         
         
         }

visited = [] # List to keep track of visited nodes.
queue = []   #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    
    for neighbour in graph[s]:
      
      if neighbour not in visited:                
        queue.append(neighbour)
        visited.append(neighbour)
    
print ("Following is Breadth First Search Traversal:") 
bfs(visited, graph, 'A')      

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "Same Node"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                # return path if neighbour is goal
                if neighbour == goal:
                    print ("\nFollowing is Breadth First Search Shortest Path:", *new_path)                 
                    return 
          
 
            # mark node as explored
            explored.append(node)
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
     

	# Function Call 
bfs_shortest_path(graph, 'A', 'O') 

 


# In[ ]:





 
queue = [] 
visited =[]  
def bfs(visited, graph, node):  
  visited.append(node)
  queue.append(node)
  while queue:
      x = queue.pop(0) 
      print (x) 
      for neighbour in graph[x]:
          queue.append(neighbour)
          visited.append(neighbour) 

# Driver code
if __name__ == "__main__":
    graph = {
          '5' : ['3','7'],
          '3' : ['2', '4'],
          '7' : ['8'],
          '2' : [],
          '4' : ['8'],
          '8' : []
        } 
     
    # Driver Code
    print("Following is the Depth-  First Search")
    bfs(visited, graph, '5')  
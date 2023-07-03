class Grapher: 
    
    def __init__(self, graph):
      self.graph=graph
  
    def dfs(self, visited, graph, node):  #function for dfs 
        if node not in visited:
            print (node)
            visited.add(node)
            for neighbour in graph[node]:
                self.dfs(visited, graph, neighbour)

if __name__ == "__main__":
    graph = {
          '5' : ['3','7'],
          '3' : ['2', '4'],
          '7' : ['8'],
          '2' : [],
          '4' : ['8'],
          '8' : []
        }
    visited =  set() # Set to keep track of visited nodes of graph.
    
    nx = Grapher(graph)
    
    print("Following is the Depth-First Search")
    nx.dfs(visited, graph, '5')  
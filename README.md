# Task 1 summary: Graph analysis

Vertices: 9  
Edges: 10

Degree of vertices:  
Router1 -> 4  
Router2 -> 4  
Router3 -> 4  
Router4 -> 3  
Server1 -> 1  
Server2 -> 1  
Server3 -> 1  
Server4 -> 1  
Server5 -> 1  

# Task 2 summary: DFS and BFS paths

Start: Server1  
Goal: Server5

DFS path: ['Server1', 'Router1', 'Router2', 'Router4', 'Server5']  
BFS path: ['Server1', 'Router1', 'Router2', 'Router4', 'Server5']

DFS and BFS were implemented to find a path between 'Server1' and 'Server5'  
For this graph, both algorithms returned the same path:  
Server1 -> Router1 -> Router2 -> Router4 -> Server5

This result is explained by the structure of the graph:
- there are only a few possible routes between the start and the goal nodes
- the order of neighbor traversal is fixed
- DFS does not have an alternative deeper route that differs from the BFS result

Although DFS and BFS use different traversal strategies, in this specific graph they produce the same path  
BFS guarantees the shortest path in terms of number of edges, while DFS returns a path that depends on the traversal order

# Task 3 summary: Dijkstra shortest paths

From: Router1  
  to Router2 | cost = 3 | path = ['Router1', 'Router2']  
  to Router3 | cost = 5 | path = ['Router1', 'Router2', 'Router3']  
  to Router4 | cost = 4 | path = ['Router1', 'Router2', 'Router4']  
  to Server1 | cost = 1 | path = ['Router1', 'Server1']  
  to Server2 | cost = 2 | path = ['Router1', 'Server2']  
  to Server3 | cost = 5 | path = ['Router1', 'Router2', 'Server3']  
  to Server4 | cost = 8 | path = ['Router1', 'Router2', 'Router3', 'Server4']  
  to Server5 | cost = 5 | path = ['Router1', 'Router2', 'Router4', 'Server5']

From: Router2  
  to Router1 | cost = 3 | path = ['Router2', 'Router1']  
  to Router3 | cost = 2 | path = ['Router2', 'Router3']  
  to Router4 | cost = 1 | path = ['Router2', 'Router4']  
  to Server1 | cost = 4 | path = ['Router2', 'Router1', 'Server1']  
  to Server2 | cost = 5 | path = ['Router2', 'Router1', 'Server2']  
  to Server3 | cost = 2 | path = ['Router2', 'Server3']  
  to Server4 | cost = 5 | path = ['Router2', 'Router3', 'Server4']  
  to Server5 | cost = 2 | path = ['Router2', 'Router4', 'Server5']  

From: Router3  
  to Router1 | cost = 5 | path = ['Router3', 'Router2', 'Router1']  
  to Router2 | cost = 2 | path = ['Router3', 'Router2']  
  to Router4 | cost = 3 | path = ['Router3', 'Router2', 'Router4']  
  to Server1 | cost = 6 | path = ['Router3', 'Router2', 'Router1', 'Server1']  
  to Server2 | cost = 7 | path = ['Router3', 'Router2', 'Router1', 'Server2']  
  to Server3 | cost = 4 | path = ['Router3', 'Router2', 'Server3']  
  to Server4 | cost = 3 | path = ['Router3', 'Server4']  
  to Server5 | cost = 4 | path = ['Router3', 'Router2', 'Router4', 'Server5']  

From: Router4  
  to Router1 | cost = 4 | path = ['Router4', 'Router2', 'Router1']  
  to Router2 | cost = 1 | path = ['Router4', 'Router2']  
  to Router3 | cost = 3 | path = ['Router4', 'Router2', 'Router3']  
  to Server1 | cost = 5 | path = ['Router4', 'Router2', 'Router1', 'Server1']  
  to Server2 | cost = 6 | path = ['Router4', 'Router2', 'Router1', 'Server2']  
  to Server3 | cost = 3 | path = ['Router4', 'Router2', 'Server3']  
  to Server4 | cost = 6 | path = ['Router4', 'Router2', 'Router3', 'Server4']  
  to Server5 | cost = 1 | path = ['Router4', 'Server5']  

From: Server1  
  to Router1 | cost = 1 | path = ['Server1', 'Router1']  
  to Router2 | cost = 4 | path = ['Server1', 'Router1', 'Router2']  
  to Router3 | cost = 6 | path = ['Server1', 'Router1', 'Router2', 'Router3']  
  to Router4 | cost = 5 | path = ['Server1', 'Router1', 'Router2', 'Router4']  
  to Server2 | cost = 3 | path = ['Server1', 'Router1', 'Server2']  
  to Server3 | cost = 6 | path = ['Server1', 'Router1', 'Router2', 'Server3']  
  to Server4 | cost = 9 | path = ['Server1', 'Router1', 'Router2', 'Router3', 'Server4']  
  to Server5 | cost = 6 | path = ['Server1', 'Router1', 'Router2', 'Router4', 'Server5']  

From: Server2  
  to Router1 | cost = 2 | path = ['Server2', 'Router1']  
  to Router2 | cost = 5 | path = ['Server2', 'Router1', 'Router2']  
  to Router3 | cost = 7 | path = ['Server2', 'Router1', 'Router2', 'Router3']  
  to Router4 | cost = 6 | path = ['Server2', 'Router1', 'Router2', 'Router4']  
  to Server1 | cost = 3 | path = ['Server2', 'Router1', 'Server1']  
  to Server3 | cost = 7 | path = ['Server2', 'Router1', 'Router2', 'Server3']  
  to Server4 | cost = 10 | path = ['Server2', 'Router1', 'Router2', 'Router3', 'Server4']  
  to Server5 | cost = 7 | path = ['Server2', 'Router1', 'Router2', 'Router4', 'Server5']  

From: Server3  
  to Router1 | cost = 5 | path = ['Server3', 'Router2', 'Router1']  
  to Router2 | cost = 2 | path = ['Server3', 'Router2']  
  to Router3 | cost = 4 | path = ['Server3', 'Router2', 'Router3']  
  to Router4 | cost = 3 | path = ['Server3', 'Router2', 'Router4']  
  to Server1 | cost = 6 | path = ['Server3', 'Router2', 'Router1', 'Server1']  
  to Server2 | cost = 7 | path = ['Server3', 'Router2', 'Router1', 'Server2']  
  to Server4 | cost = 7 | path = ['Server3', 'Router2', 'Router3', 'Server4']  
  to Server5 | cost = 4 | path = ['Server3', 'Router2', 'Router4', 'Server5']  

From: Server4  
  to Router1 | cost = 8 | path = ['Server4', 'Router3', 'Router2', 'Router1']  
  to Router2 | cost = 5 | path = ['Server4', 'Router3', 'Router2']  
  to Router3 | cost = 3 | path = ['Server4', 'Router3']  
  to Router4 | cost = 6 | path = ['Server4', 'Router3', 'Router2', 'Router4']  
  to Server1 | cost = 9 | path = ['Server4', 'Router3', 'Router2', 'Router1', 'Server1']  
  to Server2 | cost = 10 | path = ['Server4', 'Router3', 'Router2', 'Router1', 'Server2']  
  to Server3 | cost = 7 | path = ['Server4', 'Router3', 'Router2', 'Server3']  
  to Server5 | cost = 7 | path = ['Server4', 'Router3', 'Router2', 'Router4', 'Server5']  

From: Server5  
  to Router1 | cost = 5 | path = ['Server5', 'Router4', 'Router2', 'Router1']  
  to Router2 | cost = 2 | path = ['Server5', 'Router4', 'Router2']  
  to Router3 | cost = 4 | path = ['Server5', 'Router4', 'Router2', 'Router3']  
  to Router4 | cost = 1 | path = ['Server5', 'Router4']  
  to Server1 | cost = 6 | path = ['Server5', 'Router4', 'Router2', 'Router1', 'Server1']  
  to Server2 | cost = 7 | path = ['Server5', 'Router4', 'Router2', 'Router1', 'Server2']  
  to Server3 | cost = 4 | path = ['Server5', 'Router4', 'Router2', 'Server3']  
  to Server4 | cost = 7 | path = ['Server5', 'Router4', 'Router2', 'Router3', 'Server4']  
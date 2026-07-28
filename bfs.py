graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

print(graph["A"])

 
print("=== BFS ===")
def bfs(graph , start):
    visited = []
    queue = [start]

    while len(queue) > 0:
        node = queue.pop(0)

        if node not in visited:
         print(node , end=" ")    
         visited.append(node)

        for negibhor in graph[node] :
           queue.append(negibhor)
       

# bfs(graph , "A")

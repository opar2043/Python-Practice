graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

visited = set()
print("===DFS===")
def dfs(graph , node):
    if node not in visited:
        print(node , end=" ")
        visited.add(node)

        for negibhor in graph[node]:
            dfs(graph , negibhor)

dfs(graph, "A")             
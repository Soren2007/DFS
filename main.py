""" 
Created By SORENSHAMLOU

Create At : 2024/10/24

Update At : 2024/10/24

Name : DFS Algoritm

Version : 1.1.1
"""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # چاپ گره فعلی
    for neighbour in graph[start] - visited:
        dfs(graph, neighbour, visited)
    return visited

# گراف مثال

graph = {0: {1, 2}, 1: {2}, 2: {3}, 3: {1, 2}}

dfs(graph, 0)

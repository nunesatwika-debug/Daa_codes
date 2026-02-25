INF = 99999

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

src = int(input("Enter source vertex: "))

dist = [INF]*n
visited = [False]*n
dist[src] = 0

for _ in range(n-1):
    u = -1
    min_dist = INF
    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    visited[u] = True

    for v in range(n):
        if graph[u][v] and not visited[v]:
            dist[v] = min(dist[v], dist[u] + graph[u][v])

print("Shortest distances from source:")
for i in range(n):
    print(f"To {i} = {dist[i]}")
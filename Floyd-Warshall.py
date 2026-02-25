#all pairs shortest path
INF = 99999

n = int(input("Enter number of vertices: "))
dist = []

print("Enter adjacency matrix (use 99999 for INF):")
for _ in range(n):
    dist.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

print("All-pairs shortest paths:")
for row in dist:
    print(row)
print("\nMinimum distance between every pair of vertices:")
for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(f"From {i+1} to {j+1} = No path")
        else:
            print(f"From {i+1} to {j+1} = {dist[i][j]}")
            
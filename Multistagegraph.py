import sys

INF = sys.maxsize

# Read number of vertices
n = int(input("Enter number of vertices: "))

# Initialize cost matrix
cost = [[INF] * n for _ in range(n)]

# Read number of edges
e = int(input("Enter number of edges: "))

print("Enter edges in format: from to weight (1-based index)")
for _ in range(e):
    u, v, w = map(int, input().split())
    cost[u - 1][v - 1] = w   # convert to 0-based

# DP arrays
dp = [INF] * n
path = [-1] * n

# Destination vertex
dp[n - 1] = 0

# Dynamic Programming (Backward)
for i in range(n - 2, -1, -1):
    for j in range(n):
        if cost[i][j] != INF and dp[j] != INF:
            if cost[i][j] + dp[j] < dp[i]:
                dp[i] = cost[i][j] + dp[j]
                path[i] = j

# Output minimum cost
print("\nMinimum cost from source to destination:", dp[0])

# Print path (convert back to 1-based)
print("Path:", end=" ")
v = 0
while v != -1:
    print(v + 1, end=" ")
    v = path[v]
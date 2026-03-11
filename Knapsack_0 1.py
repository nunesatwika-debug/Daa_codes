def knapsack_01(weights, values, capacity, n):
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Backtracking to find selected items
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:   # Item was included
            selected_items.append(i-1)
            w -= weights[i-1]

    return dp[n][capacity], selected_items


n = int(input("Enter number of items: "))

weights = []
values = []

print("Enter weights of items:")
for i in range(n):
    weights.append(int(input()))

print("Enter values of items:")
for i in range(n):
    values.append(int(input()))

capacity = int(input("Enter knapsack capacity: "))

max_profit, selected = knapsack_01(weights, values, capacity, n)

print("Maximum Profit =", max_profit)

print("Items included in knapsack:")
for i in selected:
    print("Item", i+1, "Weight =", weights[i], "Value =", values[i])
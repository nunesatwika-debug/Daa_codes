# Read number of cities
number_of_cities = int(input("Enter number of cities: "))

# Read distance matrix
print("Enter distance matrix:")
distance = []
for i in range(number_of_cities):
    distance.append(list(map(int, input().split())))

# Bitmask where all cities are visited (e.g., for n=4 → 1111)
all_cities_visited = (1 << number_of_cities) - 1

# dp[mask][current_city] = minimum cost to reach current_city
# after visiting cities represented by mask
dp = [[-1] * number_of_cities for _ in range(1 << number_of_cities)]

# To store previous city for path reconstruction
previous_city = [[-1] * number_of_cities for _ in range(1 << number_of_cities)]

# Start from city 0, only city 0 is visited → mask = 1
dp[1][0] = 0

# Fill DP table
for visited_mask in range(1 << number_of_cities):
    for current_city in range(number_of_cities):
        # Proceed only if current_city is visited and state is reachable
        if (visited_mask & (1 << current_city)) and dp[visited_mask][current_city] != -1:
            for next_city in range(number_of_cities):
                # Visit next_city if it is not yet visited
                if (visited_mask & (1 << next_city)) == 0:
                    new_mask = visited_mask | (1 << next_city)
                    new_cost = dp[visited_mask][current_city] + distance[current_city][next_city]

                    # Update dp if this path is cheaper
                    if dp[new_mask][next_city] == -1 or new_cost < dp[new_mask][next_city]:
                        dp[new_mask][next_city] = new_cost
                        previous_city[new_mask][next_city] = current_city

# Find minimum cost to return to starting city (0)
minimum_cost = -1
last_city = -1

for city in range(1, number_of_cities):
    total_cost = dp[all_cities_visited][city] + distance[city][0]
    if minimum_cost == -1 or total_cost < minimum_cost:
        minimum_cost = total_cost
        last_city = city
# Reconstruct path (correct and clean)
path = []
current_mask = all_cities_visited
current_city = last_city

# Backtrack from last city to start city
while current_city != 0:
    path.append(current_city)
    prev = previous_city[current_mask][current_city]
    current_mask = current_mask ^ (1 << current_city)
    current_city = prev

path.append(0)        # add starting city
path.reverse()        # correct order
path.append(0)        # return to starting city

# Convert to 1-based indexing
path = [city + 1 for city in path]

# Output
print("\nMinimum Cost:", minimum_cost)
print("Path:", " -> ".join(map(str, path)))

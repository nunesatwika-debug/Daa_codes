def sum_of_subsets(arr, target):
    n = len(arr)
    subset = [0] * n

    def backtrack(i, current_sum):
        # If current sum equals target, print the subset
        if current_sum == target:
            print("Subset:", [arr[j] for j in range(n) if subset[j] == 1])
            return
        
        # If we reach end or sum exceeds target, stop
        if i == n or current_sum > target:
            return
        
        # Include the current element
        subset[i] = 1
        backtrack(i + 1, current_sum + arr[i])
        
        # Exclude the current element
        subset[i] = 0
        backtrack(i + 1, current_sum)

    backtrack(0, 0)


n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter target sum: "))

print("\nSubsets with sum", target, "are:")
sum_of_subsets(arr, target)
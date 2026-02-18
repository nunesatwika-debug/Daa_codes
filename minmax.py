def getMinMax(arr, low, high):
    # If only one element
    if low == high:
        return arr[low], arr[low]
    # If two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    # More than two elements
    mid = (low + high) // 2
    min1, max1 = getMinMax(arr, low, mid)
    min2, max2 = getMinMax(arr, mid + 1, high)
    minimum = min(min1, min2) 
    maximum = max(max1, max2)
    return minimum, maximum
n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))
minimum, maximum = getMinMax(arr, 0, n - 1)
print("Minimum element:", minimum)
print("Maximum element:", maximum)

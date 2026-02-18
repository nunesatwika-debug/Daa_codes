def Knapsack(items,capacity):
    items.sort(key= lambda x: x[1]/x[0],reverse=True)
    total=0.0
    for weight,value in items:
        if capacity==0:
            break
        if weight<=capacity:
            capacity-=weight
            total+=value
        else:
            fraction=capacity/weight
            total+=value*fraction
            capacity=0
    return total
n=int(input("Enter no of items:"))
items=[]
for i in range(n):
    weight=float(input(f"Enter weight of item {i+1}:"))
    value=float(input(f"Enter value of item {i+1}:"))
    items.append((weight,value))
capacity=float(input("Enter Knapsack capacity:"))
max_value = Knapsack(items,capacity)
print(f"\nMaximum value in Knapsack: {max_value:.2f}")


# Returns the maximum value that can be put in a knapsack of the capacity W
def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0, []

    # If weight of the nth item is more than Knapsack capacity W then this item cannot be included in the optimal solution
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)
    else:
        included_val, included_items = knapSack(W-wt[n-1], wt, val, n-1)
        included_val += val[n-1]
        included_items.append(n)
        excluded_val, excluded_items = knapSack(W, wt, val, n-1)

        if included_val > excluded_val:
            return included_val, included_items
        else:
            return excluded_val, excluded_items

# error to the user for a positive integer input
def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

# Display a header with a given title
def display_header(title):
    print("=" * 40)
    print(title)
    print("=" * 40)

# To test the above function
display_header("0-1 Knapsack Problem Solver")

n = get_positive_integer_input("Enter the number of objects: ")

val = []
wt = []

print("\nEnter the weight and value of each object:")

for i in range(n):
    print("\nObject {}:".format(i + 1))
    weight = get_positive_integer_input("  Weight: ")
    value = get_positive_integer_input("  Value: ")
    wt.append(weight)
    val.append(value)

W = get_positive_integer_input("\nEnter the capacity of the knapsack: ")
max_weight = get_positive_integer_input("Enter the maximum weight to consider: ")

print("\nCalculating the maximum value and objects included...\n")

if max_weight < W:
    display_header("Warning")
    print("The maximum weight to consider ({}) is less than the knapsack capacity ({}).".format(max_weight, W))
    print("The algorithm will find the maximum value considering the weight constraint.")

max_value, included_items = knapSack(W, wt, val, n)

display_header("Results")
print("Number of objects: {}".format(n))
print("Knapsack capacity: {}".format(W))
print("Maximum value: {}".format(max_value))

if len(included_items) > 0:
    print("Objects included (in order):")
    for item in included_items:
        print("Object {}: Weight = {}, Value = {}".format(item, wt[item - 1], val[item - 1]))
else:
    print("No objects included.")

# Print a table of objects and their weights/values
display_header("Objects")
print("| Object | Weight | Value |")
print("|--------|--------|-------|")
for i in range(n):
    print("|   {:2d}   |   {:3d}  |  {:4d} |".format(i + 1, wt[i], val[i]))
print("=" * 29)

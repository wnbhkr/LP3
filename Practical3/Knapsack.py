def fractional_knapsack(items, capacity):
    # Sort items by the ratio of value to weight in descending order (greedy choice)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0  # Total value of items selected
    knapsack = []  # List to store the selected items

    for weight, value in items:
        if capacity == 0:
            break
        elif weight <= capacity:
            # Take the whole item if it can fit
            total_value += value
            knapsack.append((weight, value))
            capacity -= weight
        else:
            # Take a fraction of the item if it can't fit entirely
            fraction = capacity / weight
            total_value += fraction * value
            knapsack.append((capacity, value))
            break

    return total_value, knapsack

# Example usage:
items = [(10, 60), (20, 100), (30, 120)]  # Each item: (weight, value)
capacity = 50
max_value, selected_items = fractional_knapsack(items, capacity)

print(f"Maximum value: {max_value}")
print("Selected items:")
for weight, value in selected_items:
    print(f"   Weight: {weight}, Value: {value}")

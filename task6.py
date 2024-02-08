def greedy_algorithm(items, budget):
    
    selected_items = []
    remaining_budget = budget

    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    for item, data in sorted_items:
        if data['cost'] <= remaining_budget:
            selected_items.append((item, data['calories']))
            remaining_budget -= data['cost']

    return selected_items


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            item_cost = items[list(items.keys())[i - 1]]['cost']
            item_calories = items[list(items.keys())[i - 1]]['calories']
            if item_cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_cost] + item_calories)
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append((list(items.keys())[i - 1], items[list(items.keys())[i - 1]]['calories']))
            j -= items[list(items.keys())[i - 1]]['cost']
        i -= 1

    return selected_items

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Жадібний алгоритм:")
print(greedy_algorithm(items, budget))
print("\nАлгоритм динамічного програмування:")
print(dynamic_programming(items, budget))
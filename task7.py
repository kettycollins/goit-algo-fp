import random
from collections import defaultdict
import matplotlib.pyplot as plt

nums = 1_000_000

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(nums):
    counts = defaultdict(int)

    for _ in range(nums):
        dice_one = roll_dice()
        dice_two = roll_dice()
        counts[dice_one + dice_two] += 1

    probabilities = {key: count / nums for key, count in counts.items()}
    return probabilities

def print_probabilities(probabilities):
    print("Сума  |  Імовірність")
    print("------|----------------")
    total_outcomes = 36  # загальна кількість можливих комбінацій для двох кубиків
    for sum_dice, prob in probabilities.items():
        fraction = f"({prob * total_outcomes:.0f}/{total_outcomes})"
        print(f"{sum_dice:4d}  |  {prob:.2%} {fraction}")


def plot_probabilities(probabilities):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title('Імовірність суми при киданні двох кубиків')
    plt.show()

if __name__ == "__main__":
    probabilities = monte_carlo_simulation(nums)
    print_probabilities(probabilities)
    plot_probabilities(probabilities)
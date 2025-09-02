import numpy as np

purchase = np.array([500, 600, 700, 800, 1000, 10000, 50000])
mean_value = purchase.mean()


def find_median(numbers):
    # Step 1: Sort the list
    numbers = sorted(numbers)
    n = len(numbers)

    # Step 2: Check if n is odd
    if n % 2 != 0:
        # Odd length → middle element
        median = numbers[n // 2]
    else:
        # Even length → average of two middle elements
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        median = (mid1 + mid2) / 2
    
    return median


print(find_median(purchase))
    

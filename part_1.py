

import random
import time

# ===========================================================
# PART 1 — SELECTION ALGORITHMS
# ===========================================================

# -----------------------------------------------------------
# Deterministic Selection — Median of Medians (Worst-case O(n))
# -----------------------------------------------------------

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Split into groups of 5
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Find medians of groups
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Recursively select pivot
    pivot = median_of_medians(medians, len(medians)//2)

    # Partition
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]

    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))


# -----------------------------------------------------------
# Randomized Quickselect — Expected O(n)
# -----------------------------------------------------------

def randomized_partition(arr, pivot):
    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]
    return low, equal, high


def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    low, equal, high = randomized_partition(arr, pivot)

    if k < len(low):
        return randomized_select(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return randomized_select(high, k - len(low) - len(equal))


# -----------------------------------------------------------
# Time Measurement Helper
# -----------------------------------------------------------

def time_function(func, arr, k):
    start = time.time()
    result = func(arr.copy(), k)
    end = time.time()
    return result, end - start


# -----------------------------------------------------------
# Empirical Running Time Comparison
# -----------------------------------------------------------

def run_empirical_analysis():
    print("\n========== EMPIRICAL ANALYSIS (PART 1) ==========\n")
    sizes = [1000, 3000, 5000]

    for n in sizes:
        print(f"\n--- Input Size: {n} ---")
        k = n // 2  # median index

        # Random input
        arr = random.sample(range(n * 10), n)
        _, t1 = time_function(median_of_medians, arr, k)
        _, t2 = time_function(randomized_select, arr, k)

        print(f"Random input:")
        print(f"  Deterministic MOM:       {t1:.6f} sec")
        print(f"  Randomized Quickselect:  {t2:.6f} sec")

        # Sorted input
        arr = list(range(n))
        _, t3 = time_function(median_of_medians, arr, k)
        _, t4 = time_function(randomized_select, arr, k)

        print(f"Sorted input:")
        print(f"  Deterministic MOM:       {t3:.6f} sec")
        print(f"  Randomized Quickselect:  {t4:.6f} sec")

        # Reverse sorted
        arr = list(range(n, 0, -1))
        _, t5 = time_function(median_of_medians, arr, k)
        _, t6 = time_function(randomized_select, arr, k)

        print(f"Reverse sorted input:")
        print(f"  Deterministic MOM:       {t5:.6f} sec")
        print(f"  Randomized Quickselect:  {t6:.6f} sec")


# -----------------------------------------------------------
# FUNCTION CALLS (DEMO)
# -----------------------------------------------------------

if __name__ == "__main__":

    arr = [12, 3, 5, 7, 19, 26, 4]
    k = 3

    print("===== PART 1: SELECTION ALGORITHMS =====")
    print("Array:", arr)

    print("\nDeterministic Selection (Median of Medians):")
    print("Result:", median_of_medians(arr, k))

    print("\nRandomized Quickselect:")
    print("Result:", randomized_select(arr, k))

    print("\nRunning empirical tests...")
    run_empirical_analysis()




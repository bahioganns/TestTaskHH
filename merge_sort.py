"""Task 3: best sorting algorythm."""

import random

MAX_SIZE = 15
MAX_NUM = 100000

def merge_sort(lst):
    """Sort list using recursive merge sorting algorythm."""

    if len(lst) > 1:

        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return lst

# sorting showcase
size = random.randint(0, MAX_SIZE)
lst = [random.randint(0, MAX_NUM) for _ in range(size)]
sorted_lst = sorted(lst)

print(lst, sorted_lst, sep="\n")

merge_sort(lst)
assert sorted_lst == lst, "Both lists are sorted"

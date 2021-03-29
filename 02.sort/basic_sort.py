from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    # print(bubble_sort(nums))
    # print(selection_sort(nums))
    print(insertion_sort([1,7,3,2,8,5]))
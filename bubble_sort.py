def bubble_sort(numbers):
    """Sort numbers in place in ascending order using bubble sort."""
    for end in range(len(numbers) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    numbers = [5, 2, 8, 6, 1]
    bubble_sort(numbers)
    print(*numbers)

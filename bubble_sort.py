def quick_sort(numbers):
    """Sort numbers in place in ascending order using three-way QuickSort."""
    def sort_range(start, end):
        while end - start > 1:
            pivot = numbers[(start + end) // 2]
            lower = current = start
            upper = end

            while current < upper:
                if numbers[current] < pivot:
                    numbers[lower], numbers[current] = numbers[current], numbers[lower]
                    lower += 1
                    current += 1
                elif numbers[current] > pivot:
                    upper -= 1
                    numbers[current], numbers[upper] = numbers[upper], numbers[current]
                else:
                    current += 1

            # Recurse on the smaller partition to keep stack usage logarithmic.
            if lower - start < end - upper:
                sort_range(start, lower)
                start = upper
            else:
                sort_range(upper, end)
                end = lower

    sort_range(0, len(numbers))


def bubble_sort(numbers):
    """Compatibility entry point for the in-place QuickSort implementation."""
    quick_sort(numbers)


if __name__ == "__main__":
    numbers = [5, 2, 8, 6, 1]
    quick_sort(numbers)
    print(*numbers)

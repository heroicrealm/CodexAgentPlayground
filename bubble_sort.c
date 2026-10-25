#include <stdio.h>

static void swap(int *left, int *right)
{
    int temporary = *left;
    *left = *right;
    *right = temporary;
}

static void quicksort(int numbers[], size_t count)
{
    while (count > 1) {
        int pivot = numbers[count / 2];
        size_t lower = 0;
        size_t current = 0;
        size_t upper = count;

        /* Partition into values below, equal to, and above the pivot. */
        while (current < upper) {
            if (numbers[current] < pivot) {
                swap(&numbers[lower++], &numbers[current++]);
            } else if (numbers[current] > pivot) {
                swap(&numbers[current], &numbers[--upper]);
            } else {
                ++current;
            }
        }

        /* Recurse on the smaller partition to bound stack usage. */
        if (lower < count - upper) {
            quicksort(numbers, lower);
            numbers += upper;
            count -= upper;
        } else {
            quicksort(numbers + upper, count - upper);
            count = lower;
        }
    }
}

int main(void)
{
    int numbers[] = {5, 2, 3, 7, 2, 1};
    const size_t count = sizeof numbers / sizeof numbers[0];

    quicksort(numbers, count);

    for (size_t i = 0; i < count; ++i) {
        printf("%s%d", i == 0 ? "" : " ", numbers[i]);
    }
    putchar('\n');

    return 0;
}

#include <stdio.h>

int main(void)
{
    int numbers[] = {5, 2, 3, 7, 2, 1};
    const size_t count = sizeof numbers / sizeof numbers[0];

    for (size_t end = count; end > 1; --end) {
        for (size_t i = 1; i < end; ++i) {
            if (numbers[i - 1] > numbers[i]) {
                int temporary = numbers[i - 1];
                numbers[i - 1] = numbers[i];
                numbers[i] = temporary;
            }
        }
    }

    for (size_t i = 0; i < count; ++i) {
        printf("%s%d", i == 0 ? "" : " ", numbers[i]);
    }
    putchar('\n');

    return 0;
}

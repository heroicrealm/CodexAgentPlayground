# CodexAgentPlayground
Playground for CodexAgent project

Run the Python QuickSort program (source file: `bubble_sort.py`):

```sh
python3 bubble_sort.py
```

The program sorts the array `5 2 8 6 1` in place in ascending order using QuickSort.
Expected output:

```text
1 2 5 6 8
```

Run the Python sorting tests:

```sh
python3 -m unittest discover -v
```

Build and run the quicksort program (source file: `bubble_sort.c`):

```sh
cc -std=c11 -Wall -Wextra -Werror bubble_sort.c -o bubble_sort
./bubble_sort
```

The program sorts the array `5 2 3 7 2 1` in ascending order using quicksort.
Expected output:

```text
1 2 2 3 5 7
```

Build and run the C hello world program:

```sh
cc -std=c11 -Wall -Wextra -Werror hello.c -o hello
./hello
```

Expected output (10 lines):

```text
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
```

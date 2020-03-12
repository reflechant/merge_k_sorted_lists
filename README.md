# merge_k_sorted_lists
https://contest.yandex.ru/contest/8458/problems/F/

Even optimized and idiomatic solution exceeds the memory limit of the exercise. I believe the problem is in `input().split()` which holds the entire string (and then the entire list) in memory.
Eventually I passed this exercize in C++ with basically the same algorithm. The only difference is the way C++ treats input - both old-style `scanf` and iostream can parse a string element by element using space as separator. It's possible to do in Python by reading from `sys.stdin` character by character, accumulating them and converting to an int when space is met but I'm too lazy to do that.

from typing import Iterator


def merge(k: int, lines: Iterator[Iterator[int]]) -> bytearray:
    array = bytearray(0)
    if k == 0:
        return array
    # line = (int(x) for x in input().split())
    line = next(lines)
    for i in range(k):
        sz = next(line)
        array = array + bytearray(line)

    return array


if __name__ == '__main__':
    k = int(input())
    lines = ((int(x) for x in input().split()) for i in range(k))
    # lines = list(lines)
    # print(lines)
    result = merge(k, lines)
    if result:
        print(result)

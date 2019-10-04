import heapq


def merge(data):
    data = (ba[1:] for ba in data)
    heap = heapq.merge(*data)
    return heap


def read_data(k):
    for _ in range(k):
        yield bytearray(int(x) for x in input().split())


def main():
    k = int(input())
    result = merge(read_data(k))
    if result:
        for x in result:
            print(x, end=' ')
    print()


if __name__ == '__main__':
    main()

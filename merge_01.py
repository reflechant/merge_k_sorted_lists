def merge(k, lines):
    data = [bytearray(0)] * k
    sz = [0] * k

    for i, line in enumerate(lines):
        sz[i] = line[0]
        data[i] = bytearray(line[1:])

    idx = [0] * k
    stop = False
    while not stop:
        stop = True
        local_min = 101
        local_idx = 0
        for i in range(k):
            if idx[i] < sz[i]:
                stop = False
                local_min = min(local_min, data[i][idx[i]])
                local_idx = i
        idx[local_idx] += 1
        yield local_min


def main():
    k = int(input())
    lines = ((int(x) for x in input().split()) for i in range(k))
    # lines = [[int(x) for x in input().split()] for i in range(k)]
    result = merge(k, lines)
    for x in result:
        print(x, end=' ')


if __name__ == '__main__':
    main()

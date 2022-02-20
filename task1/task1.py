import sys

def task1(n, m):
    i = 1
    way = []
    while True:
        way.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    way = ''.join(list(map(str, way)))
    return int(way)

n = int(sys.argv[1])
m = int(sys.argv[2])

print(task1(n, m))

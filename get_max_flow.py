#!/usr/bin/env python3
n = 0
s = 0
t = 0
c = {}
f = {}
met = {}
weight_f = 0


def get_max_flow(filename):
    input = open(filename)
    global n, s, t, c
    n = int(input.readline())
    k = 1
    while k <= n:
        line = input.readline()
        arr = line.split()
        l = 1
        while l <= len(arr):
            c[(k, l)] = int(arr[l-1])
            f[(k, l)] = 0
            l += 1
        k += 1
    s = int(input.readline())
    t = int(input.readline())
    input.close()
    global met
    met[s] = (float('inf'), 0)
    i = s
    while True:
        st = set()
        for j in range(1, n + 1):
            if j not in met and c[i, j] > 0:
                st.add(j)
        max = (0, 0)
        if len(st) != 0:
            for j in st:
                if c[(i, j)] > max[0]:
                    max = (c[(i, j)], j)
            met[max[1]] = (max[0], i)
            if max[1] == t:
                min = max[0]
                k = max[1]
                while k != s:
                    k = met[k][1]
                    if met[k][0] < min:
                        min = met[k][0]
                global weight_f
                weight_f += min
                m = max[1]
                while m != s:
                    c[met[m][1], m] -= min
                    c[m, met[m][1]] += min
                    f[met[m][1], m] += min
                    m = met[m][1]
                met = {}
                met[s] = (float('inf'), 0)
                i = s
            else:
                i = max[1]
        else:
            if i == s:
                break
            i = met[i][1]
    output = open('out.txt', 'w')
    line = ''
    for el in f.items():
        if k <= n:
            line += (str(el[1]) + ' ')
            k += 1
        if k == n + 1:
            line += '\n'
            k = 1
    line += str(weight_f)
    output.write(line)
    output.close()


if __name__ == '__main__':
    get_max_flow('in.txt')

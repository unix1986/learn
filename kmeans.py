import sys
import random
import math

def dist(x, y):
    n = len(x)
    sum = 0
    for i in range(len(x)):
        sum += math.pow(x[i] - y[i], 2)
    return sum

def add_val(x, y):
    for i in range(len(x)):
        x[i] += y[i]
    return x

def avg_val(x, y):
    for i in range(len(x)):
        x[i] /= y
    return x

def kmeans(x, k, q, t = sys.maxint):
    n = len(x)
    if n == 0 or n < k:
        return None
    m = len(x[0])
    if m == 0:
        return None
    xk = random.sample(x, k)
    r = []
    last_avg = sys.maxint
    now_avg = 0
    loop = 0
    while True:
        loop += 1
        for i in range(len(xk)):
            r.append([])
        for i in range(len(x)):
            min = sys.float_info.max
            min_pos = 0
            for j in range(len(xk)):
                d = dist(x[i], xk[j])
                if d < min:
                    min = d
                    min_pos = j
            now_avg += d
            r[min_pos].append(x[i])
        if last_avg - now_avg <= q or loop >= t:
            break
        last_avg = now_avg
        for i in range(len(r)):
            val = []
            for i in range(len(x[0])):
                val.append(0)
            for j in range(len(r[i])): 
                val = add_val(val, r[i][j])
            val = avg_val(val, len(r[i]))
            xk[i] = tuple(val)
        r = []
    return r

if __name__ == '__main__':
    x = ((1,), (2,), (3,), (4,), (90,), (100,))
    print kmeans(x, 2, 0)

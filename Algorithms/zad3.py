a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

ret = 0
for pos, val in enumerate(a):
    ret += val * b[pos]

print(ret)

# declaring the variables before hand


def oldfunction():
    c = []  # creates the empty list C
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8, 9]
    for i in range(len(a)):
        c.append(a[i]*b[i])  # element-wise multiplication [len(a) <= len(6)]
    return c
print(oldfunction())
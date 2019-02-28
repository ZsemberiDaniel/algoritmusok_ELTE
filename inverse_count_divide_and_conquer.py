import numpy as np


DEBUG_MODE = True

# random array
li = [i for i in range(1, 4)]
np.random.shuffle(li)


def inverse_count(l):
    def merge_with_count(l, low, pivot, high):
        lower_count = pivot - low + 1
        higher_count = high - pivot

        B = [0] * lower_count
        for i in range(lower_count):
            B[i] = l[low + i - 1]

        C = [0] * higher_count
        for i in range(higher_count):
            C[i] = l[pivot + i]

        B.append(np.iinfo(int).max)
        C.append(np.iinfo(int).max)

        i = 0
        j = 0
        inv_count = 0

        for m in range(low, high + 1):
            if B[i] < C[j]:
                l[m] = B[i]
                i += 1
            else:
                l[m] = C[j]
                inv_count += lower_count - i + 1
                j += 1

        return inv_count

    def recurse(l, low, high):
        inv_count = 0

        if low < high:
            mid = int(np.floor((low + high) / 2))

            inv_count += recurse(l, low, mid)
            inv_count += recurse(l, mid + 1, high)
            inv_count += merge_with_count(l, low, mid, high)

        return inv_count

    return recurse(l, 0, len(l) - 1)


print(li)
print(inverse_count(li))

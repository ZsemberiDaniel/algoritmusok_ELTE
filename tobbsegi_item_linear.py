import numpy as np


# random array
li = np.concatenate((np.zeros(10).astype(int), np.random.uniform(1, 100, 5).astype(int)))
np.random.shuffle(li)
li[0] = 20


def tobbsegi_elem(l):
    # where the pairs (that have distinct elements) end (inclusive)
    i = -1
    # from i + 1 to j - 1 there are identical elements
    j = 0
    s = 0

    # here we make the pairs
    # and we are also choosing a candidate to be the tobbsegi elem
    while j < len(l) and i + 1 < len(l):
        # the elem we are processing is not equal to the identical elements
        # -> we should pair it to an element
        if l[j] != l[i + 1]:
            i += 2  # add new pair
            l[j], l[i] = l[i], l[j]  # swap currently processed with the end of the last pair

        j += 1

    # the candidate is (i + 1)st element

    for k in range(len(l)):
        if l[k] == l[i + 1]:
            s += 1

    return l[i + 1] if s > len(l) / 2 else None


print(tobbsegi_elem(li))

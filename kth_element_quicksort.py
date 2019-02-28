import numpy as np


DEBUG_MODE = True

# random array
li = [i for i in range(1, 21)]
np.random.shuffle(li)


def kth_element(l, k):
    def partition(low, high) -> int:
        """
        Partitions the list with the pivot being the last element.

        :param low: Where in the array the first elem is we want to partition.
        :param high: Where in the array the last element (the pivot is).
        :return: Where the pivot ended up being.
        """
        last_smaller_elem_index = low - 1

        # we need to divide them into two partitions, the smaller ones first and then the higher ones and lastly the pivot
        for i in range(low, high):
            # send the smaller element to the other smaller ones
            if l[i] < l[high]:
                l[i], l[last_smaller_elem_index + 1] = l[last_smaller_elem_index + 1], l[i]

                last_smaller_elem_index += 1

        # we need to insert the pivot
        l[high], l[last_smaller_elem_index + 1] = l[last_smaller_elem_index + 1], l[high]

        # where the pivot ended up being
        return last_smaller_elem_index + 1

    def recurse(low, high):
        if DEBUG_MODE:
            print("Chosen {} as pivot".format(l[high]))

        r = partition(low, high)

        if r + 1 == k:
            return l[r]
        elif r + 1 > k:  # kth is before the pivot
            return recurse(low, r - 1)
        else:  # kth is after the pivot
            return recurse(r + 1, high)

    return recurse(0, len(l) - 1)


print(kth_element(li, 3))

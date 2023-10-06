import numpy as np
import random

def initilisation_array(n):
    final_array = []
    len_array = []
    count_array = 0
    while count_array != n:
        new_array = np.random.randint(0, 100, size=random.randint(1, n*10))
        if len(new_array) not in len_array:
            len_array.append(len(new_array))
            if count_array % 2 == 0:
                new_array = sorted(new_array)
                final_array.append(new_array)
            else:
                new_array = sorted(new_array, reverse=True)
                final_array.append(new_array)
            count_array += 1
    return final_array    
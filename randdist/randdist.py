import random
import numpy as np

def random_naive_dist(min_value, max_value, step = 1, formula = lambda x:x, seeds = 1000, round_to_step = True):
    # set an extra bin for max_value if it will return rounded random numbers
    max_value = max_value + step if round_to_step else max_value
    window_size = float(max_value) - float(min_value)
    max_counts = {}
    bin_counts = {}
    rand_list = []
    # loop in bracket
    ### needs a fix: if formula has negative value (shift up all bins by minimum value)
    for i in np.arange(min_value, max_value, step):
        max_counts[i] = formula(i)
        bin_counts[i] = 0
    scaler = round(seeds/sum(max_counts.values()))
    max_counts.update((x, round(y * scaler)) for x, y in max_counts.items())
    # adding values to the list
    if round_to_step:
        for i in np.arange(min_value, max_value, step):
            rand_list.extend(i for j in range(max_counts[i]))
    # else:
        # loop in seeds
        # for i in range(sum(max_counts.values())):
        #     rand = random.random()
    
    list_copy = list(rand_list)
    random.shuffle(list_copy)
    return list_copy
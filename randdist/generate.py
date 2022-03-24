import random
import numpy as np

def _adjust_values(min_value, max_value, step, formula, seeds):
    bin_y = {}
    # loop in bracket
    for i in np.arange(min_value, max_value, step):
        bin_y[i] = formula(i)
    # adjust values
    min_y = min(bin_y.values())
    upshift = abs(min_y) if min_y < 0 else 0
    sum_y = sum(bin_y.values()) + (upshift * len(bin_y))
    scaler = round(seeds/sum_y) if seeds > sum_y else 1
    bin_y.update((x, round((y + upshift) * scaler)) for x, y in bin_y.items())
    return bin_y

def _return_list(rand_list):
    sample = random.choice(rand_list)
    rand_list_shuffled = list(rand_list)
    random.shuffle(rand_list_shuffled)
    return rand_list_shuffled, sample

def randint(min_value, max_value, step = 1, formula = lambda x:x, seeds = 1000):
    # set an extra bin for max_value
    max_value = max_value + step
    # calculate max numbers for each bin
    bin_y = _adjust_values(min_value, max_value, step, formula, seeds)
    # adding values to the list
    rand_list = []
    for i in np.arange(min_value, max_value, step):
        rand_list.extend(i for j in range(bin_y[i]))
    return _return_list(rand_list)

def randfloat(min_value, max_value, step = 1, formula = lambda x:x, seeds = 1000):
    # calculate max numbers for each bin
    bin_y = _adjust_values(min_value, max_value, step, formula, seeds)
    # adding values to the list
    rand_list = []
    for i in np.arange(min_value, max_value, step):
        for j in range(bin_y[i]):
            rand_num = i + random.random() * step
            rand_list.append(rand_num)
    return _return_list(rand_list)
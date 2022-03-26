'''
RandDist:
----------
This minimal package generates a list of int or float numbers within a specific range and steps with custom probability distribution. \n
It has two methods:\n
1. randint\n
2. randfloat\n
each take same parameters and output same data
'''
import random
from typing import Union, Callable

def _frange(start, stop, step):
    count = 0
    while True:
        temp = start + count * step
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

def _adjust_values(min_value, max_value, step, formula, seeds):
    ''' a private method that return each bin's maximum # of numbers '''
    bin_y = {}
    # loop in bracket
    for i in _frange(min_value, max_value, step):
        bin_y[i] = formula(i)
    # adjust values
    min_y = min(bin_y.values())
    upshift = abs(min_y) if min_y < 0 else 0
    sum_y = sum(bin_y.values()) + (upshift * len(bin_y))
    if sum_y == 0:
        return {0:0}
    scaler = round(seeds/sum_y) if seeds > sum_y else 1
    bin_y.update((x, round((y + upshift) * scaler)) for x, y in bin_y.items())
    return bin_y

def _return_list(rand_list, sample_size, seeds):
    ''' a private method used in both main methods to return generated list and sample '''
    if len(rand_list) == 0:
        return 0
    if sample_size == 1:
        sample = random.choice(rand_list)
        return sample
    else:
        list_length = len(rand_list)
        if sample_size != 0:
            sample_size = min(sample_size, list_length)
        else:
            sample_size = seeds
            if list_length < sample_size:
                diff = sample_size - list_length
                for i in range(diff):
                    sample = random.choice(rand_list)
                    rand_list.append(sample)
        rand_list_shuffled = list(rand_list)
        random.shuffle(rand_list_shuffled)
        rand_list_shuffled = rand_list_shuffled[0:sample_size]
        return rand_list_shuffled

def randint(
        min_value: Union[int, float],
        max_value: Union[int, float],
        step: Union[int, float] = 1,
        formula: Callable[[int], int] = lambda x:x,
        seeds: int = 1000,
        sample_size: int = 0
    ) -> Union[list, int, float]:
    '''
    This method generates integer numbers
    ----------
    Arguments:
        min_value: start
        max_value: stop
        step: bin step size (default: 1)
        formula: a lambda function for distribution curve (default: lambda x:x)
        seeds: # of generated numbers (default: 1000)
        sample_size: # of numbers to return. 0 return a list of generated numbers, 1 return only one int or float number, 2 or more returns a list with the specified amount of numbers. sample_size can't be more than seeds. (default: 0)
    Returns:
        a list of generated numbers or
        a sample number
    '''
    # set an extra bin for max_value
    max_value = max_value + step
    # calculate max numbers for each bin
    bin_y = _adjust_values(min_value, max_value, step, formula, seeds)
    # adding values to the list
    rand_list = []
    for i in _frange(min_value, max_value, step):
        rand_list.extend(i for j in range(bin_y[i]))
    return _return_list(rand_list, sample_size, seeds)

def randfloat(
        min_value: Union[int, float],
        max_value: Union[int, float],
        step: Union[int, float] = 1,
        formula: Callable[[int], int] = lambda x:x,
        seeds: int = 1000,
        sample_size: int = 0
    ) -> Union[list, int, float]:
    '''
    This method generates float numbers
    ----------
    Arguments:
        min_value: start
        max_value: stop
        step: bin step size (default: 1)
        formula: a lambda function for distribution curve (default: lambda x:x)
        seeds: # of generated numbers (default: 1000)
        sample_size: # of numbers to return. 0 return a list of generated numbers, 1 return only one int or float number, 2 or more returns a list with the specified amount of numbers. sample_size can't be more than seeds. (default: 0)
    Returns:
        a list of generated numbers or
        a sample number
    '''
    # set an extra bin for max_value
    max_value = max_value + step
    # calculate max numbers for each bin
    bin_y = _adjust_values(min_value, max_value, step, formula, seeds)
    # adding values to the list
    rand_list = []
    for i in _frange(min_value, max_value, step):
        for j in range(bin_y[i]):
            rand_num = i + random.random() * step
            rand_list.append(rand_num)
    return _return_list(rand_list, sample_size, seeds)
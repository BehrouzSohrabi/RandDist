# RandDist

## python random generator with custom probability distribution

This minimal package generates a list of int or float numbers within a specific range and steps with custom probability distribution.

![myfile](https://raw.githubusercontent.com/BehrouzSohrabi/Random-with-custom-distribution/main/demo/animated_plot.gif)

## How to use

### install

`` pip install randdist``

### include

```python
import randdist
```

### generate

```python
numbers_list = randdist.randint(0, 10, formula = lambda x:x**2)
```

## Methods

* `randint`: Generates integer numbers
* `randfloat`: Generates float numbers

## Parameters

* `min_value`: start
* `max_value`: stop
* `step`: bin step size `default = 1`
* `formula`: lambda function for distribution curve `default = lambda x:x`
* `seeds`: # of generated numbers `default = 1000`
* `sample_size`: # of numbers to return `default = 0`
  - `0`: return a list of generated numbers.
  - `1`: return only one int or float number
  - `2 or more`: returns a list with the specified amount of numbers. sample_size can't be more than seeds.

## Outputs

Depending on `sample_size`:

* `list`: a list of shuffled generated numbers
  or
* `sample`: an integer of a float number from the list

## Demo

* `min_value = -3`
* `max_value = 3`
* `step = 0.5`
* `formula = lambda x:12-(x**2)`
* `seeds = 1000`

```python
# generate int numbers
random_list_int = randdist.randint(min_value, max_value, step, formula, seeds)

# generate float numbers
random_list_float = randdist.randfloat(min_value, max_value, step, formula, seeds)
```

![myfile](https://raw.githubusercontent.com/BehrouzSohrabi/Random-with-custom-distribution/main/demo/formula_plot.png)
![myfile](https://raw.githubusercontent.com/BehrouzSohrabi/Random-with-custom-distribution/main/demo/distribution_plot_int.png)
![myfile](https://raw.githubusercontent.com/BehrouzSohrabi/Random-with-custom-distribution/main/demo/distribution_plot_float.png)

### Test Distribution

with 10K generated numbers

```python
# pick samples from 10K generated list of numbers
generated_list = []
for i in range(10000):
    sample_int = randdist.randint(-3, 3, 0.5, lambda x:12-(x**2), sample_size = 1)
    generated_list.append(sample_int)
```

![myfile](https://raw.githubusercontent.com/BehrouzSohrabi/Random-with-custom-distribution/main/demo/distribution_plot_test.png)

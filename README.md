# RandDist
## python random generator with custom probability distribution

This minimal package generates a list of int or float numbers within a specific range and steps with custom probability distribution.<br><br>

![myfile](https://raw.githubusercontent.com/BehrouzSohrabi/Random-with-custom-distribution/main/demo/distribution_plot_float.png)

## How to use
### install
``` pip install randdist```
### include
```python
import randdist
```
### generate
```python
numbers_list, sample_number = randdist.randint(0, 10, formula = lambda x:x**2)
```

## Methods
* `randint`: Generates integer numbers
* `randfloat`: Generates float numbers
## Parameters
* `min_value`: min value
* `max_value`: max value
* `step`: bin steps `default = 1`
* `formula`: lambda function for distribution curve `default = lambda x:x`
* `seeds`: # of generated numbers `default = 1000`

## Outputs

* `list`: a list of shuffled generated numbers
* `sample`: picks one from the list

## Demo

* `min_value = -3`
* `max_value = 3`
* `step = 0.5`
* `formula = lambda x:12-(x**2)`
* `seeds = 1000`

``` python
# generate int numbers
random_list_int, sample_int = randdist.randint(min_value, max_value, step, formula, seeds)

# generate float numbers
random_list_float, sample_float = randdist.randfloat(min_value, max_value+step, step, formula, seeds)
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
    random_list_int, sample_int = randdist.naive_int(min_value, max_value, step, formula, seeds)
    generated_list.append(sample_int)
```

![myfile](https://raw.githubusercontent.com/BehrouzSohrabi/Random-with-custom-distribution/main/demo/distribution_plot_test.png)
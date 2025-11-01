# Functions
Function is a block of code that performs a specific task. Function helps in organizing code, reusing code and improving readability.

``` python
  def function_name(parameters):
        "DocString" #It is used in every function to let others know what this function actually does
  #Function Body
```
```python
  """This function finds even or odd"""
  def even_check(num):
      if(num%2 == 0):
          print(f"{num} is even")
      else:
          print(f"{num} is odd")

  even_check(11) ## Calling Function
```

### Functions with multiple parameters
``` python
def add(a,b):
    return a+b

result = add(3,4)
print(result)
```

### Default Parameters
``` python
  def greet(name = "Guest"):
      print(f"Hello {name}")

  greet()
```

### Keywords Arguments
``` python
  def print_details(**kwargs): #all the paramters will be in key value pairs
      for key, value in kwargs.items():
          print(f"{key}:{value}")
```
-----
## Lambda Functions
Lambda Functions are small anonymous functions defined using the lambda keyword. They can have any number of arguments but only one expression. They are commonly used for short operations or as arguments to higher-order functions.

### Syntax
``` python
  lambda arguments: expression
```

### Lambda functions are used where we have a single expression for a function which saves time and lines of codes.
-----
## Map() function
The map() function applies a given function to all items in an input list (or any other iterable) and returns a map object (an iterator). This is particularly useful for transforming data in a list comprehensively.

```python
  def square(x):
      return x**x

  numbers = [1,2,3,4,5,6,7,8]
  list(map(square, numbers))
  # map would take each number and use the function to perform the square operation
```

#### Lambda function with map
```python
  numbers = [1,2,3,4,5,6,7,8]
  list(map(lambda x:x*x, numbers))
```
#### map() to convert a list of strings to integers
##### use map to convert strings to integers and strings to upper case

``` python
  str_numbers = ["1","2","3","4"]
  int_numbers = list(map(int, str_numbers))
  print(int_numbers)
```
``` python
  words = ['apple','cherry','tomato']
  upper_words = list(map(str.upper, words))
  print(upper_words)
```
-----
## Filter Function
The filter function constructs an iterator from elements of an iterable for which a function returns true. It is used to filter out items from a list (or any other iterable) based on a condition.

```python
  def even(num):
      if num%2 == 0:
          return True

  lst = [1,2,3,4,5,6,7,8]
  list(filter(even,lst)) #first parameter is function, second paramter is list
```
```python
  ## Filter with a Lambda function
  numbers = [1,2,3,4,5,6,7,8]
  greater_than_five = list(filter(lambda x:x>5, numbers))
  print(greater_than_five)
```

#### The filter function is a powerful tool for creating iterators that filter items out of an iterable based on a function. It is commonly used for data cleaning, filtering objects, and removing unwanted elements from lists. By mastering filter(), you can write more concie and efficiet code for processing and manipulating collections in Python

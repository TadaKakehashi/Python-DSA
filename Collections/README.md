# Collections
A **Collection** is a data structure that is used to store multiple items in a single variable.

> Collections helps us to group related data together - instead of keeping separable varibales for each item
- List : Ordered, changable collection
- Set : Unordered, unique items
- Dictionary : Key Value Pairs
- Tuple : Ordered, unchangeable collection

### List: They are Ordered mutable collection of items
``` python
    list = ["Tada","Aryan","Ray"]
    print(names)
    print(type(names))
```

``` python
  ### Accessing List Elements:
  fruits = ["apple","banana","cherry","kiwi]
  print(fruits[0])
  print(fruits[-1])
  print(fruits[1:])
  print(fruits[1:3])
  print(fruits[-1:])
```

``` python
  ### Modifying the List Elements
  fruits[2] = 'watermelon'
  print(fruits)
```

#### List Methods:
1. Append: Add elements to the end
   ``` python
     fruits.append('orange')
   ```
2. Insert: Inserting element at particular index
   ``` python
     fruits.insert(1,'watermelon')
   ```
3. Remove: Removing the first occurence of an item
   ``` python
     fruits.remove('banana')
   ```
4. Pop: Remove and return the last
   ``` python
      popped_fruits= fruits.pop()
   ```
5. Index: Return the index number of the item
   ``` python
     index = fruits.index('orange')
   ```
6. Count: Count the occurence of a particular item
   ``` python
     fruits.count('banana')
   ```
7. Reverse: Reverse the list
   ``` python
     fruits.reverse()
   ```
8. Clear: Remove all items from the list
   ``` python
     fruits.clear()
   ```

##### Slicing List
``` python
  numbers = [1,2,3,4,5,6,7,8,9,10]
  print(numbers[2:5])
  print(numbers[:5])
  print(numbers[5:])
  print(numbers[::2]) ## we will jump two steps throughout the list 
  print(numbers[::-1]) ## -1 means from the last element of the list :: then step number
```

#### Iterating Over List
``` python
  for number in numbers:
      print(number)
```
``` python
  for index, number in enumerate(numbers): #enumerate is needed when we need index number
      print(f`Index: {index} :: Number : {number}`)
```

### List Comprehension:
 It is a powerful and concise way to create lists in Python. They are syntactically compact and can replace more verbose looping constructs. Understanding the syntax of list comprehensions will help you write cleaner and more efficient Python code.

*Basic Syntax* 
: [expression for item in iterable]
  ```python
    square =[num**2 for num in range(10)]
  ```

*With conditional logic*
: [expression for item in iterable if condition]
  ```python
  #List comprehension with condition
    list = []
    for i in range(10):
      if i%2 == 0:
        list.append(i)

    print(list)
  ```
*Nested List Comprehension*
: [expression for item1 in iterable1 for item2 in iterable2]
  ```python
    list1 = [1,2,3,4]
    list2 = ['a','b','c','d']

    pairs =[[i,j] for i in list1 for j in list2] 
    print(pairs)
  ```

  ```python
    ## List comprehension with function calls
    words = ["hello",'world','python','list','comprehension']
    lengths = [len(word) for word in words]
    print(lengths)
  ```

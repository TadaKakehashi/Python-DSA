## Arrays
*An Array is a collection of elements stored in Contiguous memory location. All elements of array are of same data type (int, float etc.)
Array allow for eficient access and manipulationn of data.*

-> Arrays are of fixed size
-> Arrays are homogeneous in nature (A single data type of elements are used)

*In Python we use list instead of array as they provide more flexibility. However, python provide ability to use array via libraries such as numpy and array*

```python
  import array #to define arrays we use import to use array otherwise we use lists
  arr = array.array('i',[1,2,3,4,5]) #i = data types 
  print(arr)
```

------
| Type code | C Type             | Python Type       | Minimum size in bytes |
| --------- | ------------------ | ----------------- | --------------------- |
| `'b'`     | signed char        | int               | 1                     |
| `'B'`     | unsigned char      | int               | 1                     |
| `'u'`     | wchar_t            | Unicode character | 2                     |
| `'h'`     | signed short       | int               | 2                     |
| `'H'`     | unsigned short     | int               | 2                     |
| `'i'`     | signed int         | int               | 2                     |
| `'I'`     | unsigned int       | int               | 2                     |
| `'l'`     | signed long        | int               | 4                     |
| `'L'`     | unsigned long      | int               | 4                     |
| `'q'`     | signed long long   | int               | 8                     |
| `'Q'`     | unsigned long long | int               | 8                     |
| `'f'`     | float              | float             | 4                     |
| `'d'`     | double             | float             | 8                     |

------


Arrays: 
1. Are Homogenous (same type)
2. Fixed Size
3. More memory Efficient for larger data
4. Use array or numpy (in python)

Lists:
1. Heterogenous in nature (Different type)
2. They are of Dynamic Size (Can grow and Shrink)
3. Slower for larger dataset
4. They are built in datatypes in Python

-------

# Linear Search
*Linear Search is the simplest searching algorithm.
In Linear Search we visit every single element and see if it matches with the target or not, and move till the end of the array.*

```python
    def linearsearch(arr,target):
    size = len(arr)
    for index in range(size):
        if arr[index] == target:
            return index

    return -1

arr = [10,20,30,40,50]
target = 40
result = linearsearch(arr,target)
print(result)
```
Algorithm Steps

- Start from the first element of the list.

- Compare the current element with the target element.

- If they match → return the index (or indicate “found”).

- If not → move to the next element.

- If the end of the list is reached → return “not found”.


### Case	Time Complexity	Explanation

- Best Case:	O(1)	Target found at first position

- Worst Case:	O(n)	Target not present or at last position

- Average Case:	O(n/2) ≈ O(n)	Target somewhere in the middle

- Space Complexity:	O(1)	No extra space used

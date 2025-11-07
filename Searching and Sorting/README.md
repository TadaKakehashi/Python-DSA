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


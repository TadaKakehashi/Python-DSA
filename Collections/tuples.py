## Tuples are versatile and useful in many real-world scenarios where an immutable and ordered collection of items is required.


## Creating a tuple

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))


lst = list()
print(type(lst))
tpl = tuple()
print(type(tpl))
#
number = (1,2,3,4,5,6)
#
mixed_tuples = (1,"Hi",3.12,True)


## Accessing Tuple Elements
print(number[0])
print(number[::-1])

## Concatination of Tuples
concat_tuples = number + mixed_tuples
print(concat_tuples)
#
print(mixed_tuples*3)

## Immutable nature of Tuples
# Tuples are immutable meaning their elements cannot be changed once assigned

lst = [1,2,3,4]
print(lst)
lst[1] = "Tada"
print(lst)

number[1] = "Tada"
print(number)

number = tuple([1,2,2,2,2,2,2,3,4,5,6])
## Tuple Methods
print(number.count(2)) ## returns the count of the number
print(number.index(3)) ## in which index is 3 present

## packing nd unpacking tuples
packed_tuple = 1, "hello", 3.13 #it will pack it automatically as a tuple
print(packed_tuple)

## unpacking of tuples
a,b,c = packed_tuple
print(a)
print(b)
print(c)
#
# ## Unpacking with *
numbers = (1,2,3,4,5,6)
first,*middle,last = numbers
print(first)
print(middle) #* will take the remaining elements into a packed tup
print(last)


## Nested Tuple
lst = [[1,2,3,4],[6,7,8,9],[1,"Hello",3.13,"c"]]
print(lst[0][0:3])

nested_tup = ((1,2,3,4),("A","B","C"),(True , False))
print(nested_tup[0][0:2])

#Iterating over a nested tuple
for tup in nested_tup:
    for item in tup:
        print(item, end=" ")
        print()

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)The time complexity is O(1) + O(n^3) / O(n^2) == O(n)

```python
a = 0                       #O(1)
while (a < n * n * n):      #O(n)
    a = a + n * n           # O(1)

```
The control variable ```a``` increases everytime with ```n^2```.  But the while loop checks if the ```a < n^3```.  Basically it checks ```n^2 < n^3``` which gives a complexity of ```O(n)```.  


b) The time complexity is O(1) + O(n) * O(1) * O(log n) * O(1 + 1) == 0(n log n)

```python
sum = 0                     #O(1)
    for i in range(n):      #O(n)
    j = 1                   #O(1)
    while j < n:            #O(log n)
    j *= 2                  #O(1)
    sum += 1                #O(1)

```

c) The time complexity is == O(n)

```python
def bunnyEars(bunnies):     
    if bunnies == 0:                    #O(1)
    return 0                            #O(1)

    return 2 + bunnyEars(bunnies-1)     #O(n)

```
This is recursive.  Base case first and then recurses towards base case.  Calls the function n times until reaches n=0.  

## Exercise II

```
# Base case:
# Start on the ground  floor
# Get the middle floor between the start point and the top floor (n)
# run until floor f:
    # drop the egg
    # if the egg breaks:
        # move to the middle point between current location and the ground
    # otherwise:
        # move to the middle point between current location and the top floor
# return floor f
# floor f is the highest floor where the egg doesn't break

```
This is Binary search approach.  Has a runtime complexity of O(log n).  



## About My Data Structure
I defined NoDuplicatedLinkedList which is similar to linkedlist, but it doesn't have not duplicate value.

## Time and Space
It is O(n) abount order when I add a block.
So, when linkedlist has many elements,
it will take a lot of time.

To union, it is O(n).
To intersection, it is O(n) too.

As to space, In the case of the union and the intersection,
I used shallow copy,
especially,  I used list and dict to remember list1 in the intersection.
It may waste space...

## About My Data Structure
I used data structure of tree to build haffman tree surely.

I defined root's char and its frequencies as dummy.
When given character is only one, it is placed left child of root.

Then, my code pick out two nodes that has the smallest frequencies and next one to build the tree.
After that, it creates new node which has total frequencies, and be stored to the list.

To encode, I used recursion to traverse haffman tree.
TO decode, I used dict so that it can be found more effective.

## Time and Space
In the case of build tree, it may be  O(logn).
It is complexity.
I did't know an order when sort appear in the loop.
I used sort function in a loop.
```
while len(nodes) >= 2:
    (omitted)
    nodes = sorted(nodes, key = attrgetter('frequencies'))
```

In the case of encode and decode, it may be O(n).

As to space, I used dict to decode.
So, it will use some spaces than searching char every time.
But, I think it is tradeoff. I selected the way to find characters easily.

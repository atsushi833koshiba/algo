## About My Data Structure
I used data structure of tree to build haffman tree surely.

I defined root's char and its frequencies as dummy.
When given character is only one, it is placed left child of root.

Then, my code pick out two nodes that has the smallest frequencies and next one to build the tree.
After that, it creates new node which has total frequencies, and be stored to the list.

To encode, I used recursion to traverse haffman tree.
To decode, I used dict so that it can be found more effective.

## Time and Space
In the case of encode, it is O(logn) because I used sorted function to order by frequencies.
In the case of decode, it is O(n).

As to space, there is not wasted or duplicated data.
So, it is OK!

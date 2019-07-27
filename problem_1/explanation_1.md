## About My Data Structure
I used queue to resolve how to implement Least Recently Used.
By using it, the data which is used recently is enqueued in the dict,(first time or again)
on the other hand, the data which is not used recently is dequeued.

Then, as I said above, I used the dict as map to extract the data in the list for O(1).

## Time and Space
I think it mostly meets O(1).
But, I write below code to extract the data when the cache size exceed its capacity.
It may not be O(1). I could not know another way.

```
first = list(self.entry)[0]
```

As to space, there is not wasted or duplicated data.
So, it is OK!

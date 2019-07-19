import unittest

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.entry = {}
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = self.entry.pop(key, None)
        if value:
            self.entry[key] = value
            return value
        return -1

    def isExceedingCapacity(self):
        return len(self.entry) >= self.capacity

    def set(self, key, value):
        # Capacity Over
        if self.isExceedingCapacity():
            # Remove fist element in dict.
            # TODO: I think it is needed to modify, because from dict to list may be not O(1).
            if self.capacity == 0:
                return
            first = list(self.entry)[0]
            self.entry.pop(first)

            # Add new key and value.
            self.entry[key] = value
            return

        self.entry[key] = value


def test_case1_do_LRU_Cache():

    actual = []
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    actual.append(our_cache.get(1))       # returns 1
    actual.append(our_cache.get(2))       # returns 2
    actual.append(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    actual.append(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    expected = [1,2,-1,-1]
    statement = "Test Case1 : actual {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    #Expected: Test Case1 : actual [1,2,-1,-1]

def test_case2_do_LRU_Cache():

    actual = []
    our_cache = LRU_Cache(3)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(1, 1)
    our_cache.set(2, 2)

    actual.append(our_cache.get(3))       # returns -1
    actual.append(our_cache.get(1))       # returns 1

    expected = [-1,1]
    statement = "Test Case2 : actual {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    #Expected: Test Case2 : actual [-1, 1]

def test_case3_do_LRU_Cache():

    actual = []
    our_cache = LRU_Cache(10)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    our_cache.set(7, 7)
    our_cache.set(8, 8)

    actual.append(our_cache.get(5))       # returns 5

    our_cache.set(9, 9);
    our_cache.set(10, 10);
    our_cache.set(11, 11);
    our_cache.set(12, 12);
    our_cache.set(13, 13);
    our_cache.set(14, 14);
    our_cache.set(15, 15);

    actual.append(our_cache.get(5))       # returns 5
    actual.append(our_cache.get(6))       # returns 6
    actual.append(our_cache.get(4))       # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    actual.append(our_cache.get(15))      # returns 15
    actual.append(our_cache.get(100))     # returns -1

    expected = [5,5,-1,-1,15,-1]
    statement = "Test Case3 : actual {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    #Expected: Test Case3 : actual [5, 5, -1, -1, 15, -1]

def test_case4_do_LRU_Cache():
    actual = []
    our_cache = LRU_Cache(0)
    our_cache.set(1,1)
    our_cache.set(1,2)
    actual.append(our_cache.get(1))
    actual.append(our_cache.get(2))
    expected = [-1,-1]
    statement = "Test Case4 : actual {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    #Expected: Test Case4 : actual [-1, -1]


test_case1_do_LRU_Cache()
test_case2_do_LRU_Cache()
test_case3_do_LRU_Cache()
test_case4_do_LRU_Cache()

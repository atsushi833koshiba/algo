import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class NoDuplicatedLinkedList:
    def __init__(self):
        self.head = None
        self.already_exist_map = {}

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head == None:
            self.head = Node(value)
            return

        node = self.head
        before = node

        while node:
            if str(value) == str(node.value):
                return
            before = node
            node = node.next

        node = before
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    newLinkedList =  NoDuplicatedLinkedList()

    l1 = copy.copy(llist_1)
    l2 = copy.copy(llist_2)

    while l1.head:
        newLinkedList.append(l1.head)
        l1.head = l1.head.next

    while l2.head:
        newLinkedList.append(l2.head)
        l2.head = l2.head.next

    return newLinkedList

def intersection(llist_1, llist_2):

    if not isinstance(llist_1, NoDuplicatedLinkedList) or not isinstance(llist_2, NoDuplicatedLinkedList):
        return None

    if llist_1 == None or llist_2 == None:
        return None

    # Your Solution Here
    newLinkedList =  NoDuplicatedLinkedList()
    already_exist_map = {}
    intersection = []

    l1 = copy.copy(llist_1)
    l2 = copy.copy(llist_2)

    while l1.head:
        already_exist_map[l1.head.value] = l1.head
        l1.head = l1.head.next

    while l2.head:
        # Not exsit in llist_1.
        if already_exist_map.get(l2.head.value):
            intersection.append(l2.head.value)
        l2.head = l2.head.next

    for value in intersection:
        newLinkedList.append(value)

    return newLinkedList



# Test case 1
linked_list_1 = NoDuplicatedLinkedList()
linked_list_2 = NoDuplicatedLinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# Expected: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print (intersection(linked_list_1,linked_list_2))
# Expected: 6 -> 4 -> 21 ->

# Test case 2
linked_list_1 = NoDuplicatedLinkedList()
linked_list_2 = NoDuplicatedLinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# Expected: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2))
# Expected: blanks (There is not something to dispaly.)

# Test case 3
linked_list_1 = NoDuplicatedLinkedList()
linked_list_2 = NoDuplicatedLinkedList()

element_1 = None
element_2 = None

linked_list_1.append(element_1)
linked_list_2.append(element_2)

print (union(linked_list_1,linked_list_2))
# Expected: None
print (intersection(linked_list_1,linked_list_2))
# Expected: None

# Test case 4
linked_list_1 = NoDuplicatedLinkedList()
linked_list_2 = NoDuplicatedLinkedList()

for i in range(10000):
    linked_list_1.append(i)

for i in range(10000):
    # All 2
    linked_list_2.append(2)

print (union(linked_list_1,linked_list_2))
# Expected: 0 -> 1 -> ... -> 9998 -> 9999 ->
print (intersection(linked_list_1,linked_list_2))
# Expected: 2 ->

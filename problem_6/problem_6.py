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

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:

            if value == node.value:
                return
            node = node.next

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

    while llist_1.head:
        newLinkedList.append(llist_1.head)
        llist_1.head = llist_1.head.next

    while llist_2.head:
        newLinkedList.append(llist_2.head)
        llist_2.head = llist_2.head.next

    return newLinkedList

def intersection(llist_1, llist_2):
    # Your Solution Here
    newLinkedList =  NoDuplicatedLinkedList()
    already_exist_map = {}

    while llist_1.head:
        print(llist_1.head.value)
        already_exist_map[llist_1.head.value] = llist_1.head
        llist_1.head = llist_1.head.next
    print(already_exist_map)

    while llist_2.head:
        # Not exsit in llist_1.
        if not llist_2.head.value == already_exist_map.get(llist_2.head.value):
            already_exist_map.pop(llist_2.head.value)
        llist_2.head = llist_2.head.next

    print(already_exist_map)

    for key in already_exist_map:
        newLinkedList.append(already_exist_map[key])

    return newLinkedList



# Test case 1
linked_list_1 = NoDuplicatedLinkedList()
linked_list_2 = NoDuplicatedLinkedList()

# element_1 = [3,2,4,35,6,65,6,4,3,21]
# element_2 = [6,32,4,9,6,1,11,21,1]

element_1 = [3,21,6]
element_2 = [6,21,1]

for i in element_1:
    linked_list_1.append(i)


for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
#print (intersection(linked_list_1,linked_list_2))
#
# # Test case 2
#
linked_list_3 = NoDuplicatedLinkedList()
linked_list_4 = NoDuplicatedLinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# print (union(linked_list_3,linked_list_4))
# print (intersection(linked_list_3,linked_list_4))

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def simple_search(list, target):
    # Simple search.
    if len(list) == 1:
        if list[0] == target:
            return True
    return False


def binary_search(list, target, lower, upper):
    """
    Execute binary search. O(logn)
    Return True if target is in the list, False otherwise.

    Args:
      list(list): List to be traversed.
      target(str): Characters to be wanted to find.
      lower(int): Start position.
      upper(int): End position.
    """
    if len(list) == 0:
        return False

    mid = (lower + upper) // 2

    # End condition.
    if target == list[mid]:
        return True
    elif lower > upper:
        return False

    if target > list[mid]:
        lower = mid + 1
    else:
        upper = mid - 1

    return binary_search(list, target, lower, upper)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user == None or group == None:
        return False

    users = group.get_users()

    # Simple search.
    if simple_search(users, user):
        return True

    _sorted = sorted(users)

    hasUser = binary_search(_sorted, user, 0, len(users)-1)
    if hasUser:
        # In the case of success in searching for user.
        return hasUser

    # Find user with recursion.
    for children_grp in group.get_groups():
        hasUser = is_user_in_group(user, children_grp)

    return hasUser


def test_case1_search_user():

    parent = Group("parent")

    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    result = is_user_in_group("sub_child_user", parent)
    statement = 'test_case1_search_user: {}'.format(result)
    print(statement)
    #Expected: test_case1_search_user: True

def test_case2_search_user():

    parent = Group("parent")

    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub2_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    result = is_user_in_group("sub_child_user", parent)
    statement = 'test_case2_search_user: {}'.format(result)
    print(statement)
    #Expected: test_case2_search_user: False

def test_case3_search_user():

    parent = Group("parent")

    child = Group("child")
    sub_child = Group("subchild")
    sub2_child = Group("sub2child")
    sub3_child = Group("sub3child")
    sub4_child = Group("sub4child")
    sub5_child = Group("sub5child")

    sub_child_user = "sub_child_user"
    sub2_child_user = "sub2_child_user"
    sub2_child2_user = "sub2_child2_user"
    sub5_child_user = "sub5_child_user"

    sub_child.add_user(sub_child_user)
    sub2_child.add_user(sub2_child_user)
    sub2_child.add_user(sub2_child2_user)
    sub5_child.add_user(sub5_child_user)

    sub2_child.add_group(sub3_child)
    sub2_child.add_group(sub4_child)
    sub2_child.add_group(sub5_child)
    sub_child.add_group(sub2_child)

    child.add_group(sub_child)
    parent.add_group(child)

    result = is_user_in_group("sub5_child_user", parent)
    statement = 'test_case3_search_user: {}'.format(result)
    print(statement)
    #Expected: test_case3_search_user: True

def test_case4_search_user():

    parent = Group(None)

    result = is_user_in_group("none", parent)
    statement = 'test_case4_search_user: {}'.format(result)
    print(statement)
    #Expected: test_case4_search_user: False

def test_case5_search_user():

    parent = Group('one')

    result = is_user_in_group("one_user", parent)
    statement = 'test_case5_search_user: {}'.format(result)
    print(statement)
    #Expected: test_case5_search_user: False

def test_case6_search_user():

    parent = Group('parent')
    child1 = Group("child1")
    child2 = Group("child2")
    child3 = Group("child3")
    child4 = Group("child4")
    child5 = Group("child5")
    child6 = Group("child6")
    child7 = Group("child7")
    child8 = Group("child8")
    child9 = Group("child9")
    child10 = Group("child10")

    parent.add_user('1')
    parent.add_user('2')
    parent.add_user('3')
    parent.add_user('4')
    parent.add_user('5')

    child1.add_user('6')
    child1.add_user('7')
    child1.add_user('8')
    child1.add_user('9')
    child1.add_user('10')

    child5.add_user('11')
    child5.add_user('12')
    child5.add_user('13')
    child5.add_user('14')
    child5.add_user('15')

    child6.add_user('16')
    child6.add_user('17')
    child6.add_user('18')
    child6.add_user('19')
    child6.add_user('20')

    for i in range(100):
        child10.add_user('same old same old')
    child10.add_user('different')

    parent.add_group(child1)
    parent.add_group(child2)
    parent.add_group(child3)
    parent.add_group(child4)
    parent.add_group(child5)
    parent.add_group(child6)
    parent.add_group(child7)
    parent.add_group(child8)
    parent.add_group(child9)
    parent.add_group(child10)

    result = is_user_in_group("different", parent)
    statement = 'test_case5_search_user: {}'.format(result)
    #Expected: test_case6_search_user: True
    print(statement)

test_case1_search_user()
test_case2_search_user()
test_case3_search_user()
test_case4_search_user()
test_case5_search_user()
test_case6_search_user()

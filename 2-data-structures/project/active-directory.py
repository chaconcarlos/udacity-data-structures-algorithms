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

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    result = False

    if user:
      group_users = group.get_users()

      if user in group_users:
        result = True
      else:
        sub_group_list = group.get_groups()

        for sub_group in sub_group_list:
          if is_user_in_group(user, sub_group):
            result = True
            break

    return result

#Test data
parent      = Group("parent")
empty_group = Group("empty")

child1 = Group("child1")
child2 = Group("child2")
child3 = Group("child3")
child4 = Group("child4")

sub_child     = Group("subchild")
sub_child1    = Group("subchild1")
sub_sub_child = Group("subsubchild1")

parent.add_user("parent_user")
child1.add_user("carlos")
child2.add_user("maria")
child3.add_user("jose")
child4.add_user("gerardo")

sub_child.add_user("sub_child_user")
sub_child1.add_user("Juana")
sub_sub_child.add_user("sub_sub_child_user")

sub_child1.add_group(sub_sub_child)

child1.add_group(sub_child)
child2.add_group(sub_child1)

parent.add_group(child1)
parent.add_group(child2)
parent.add_group(child3)
parent.add_group(child4)

#Test 1: user "parent_user" that belongs to the "parent" group, that is the root.
#Expected: True
print("Test 1:", is_user_in_group("parent_user", parent))
#Test 2: user "carlos" that belongs to the "child1" group, that on the first level after the root.
#Expected: True
print("Test 2:", is_user_in_group("carlos", parent))
#Test 3: user "gerardo" that belongs to the "child4" group, that on the first level after the root.
#Expected: True
print("Test 3:", is_user_in_group("gerardo", parent))
#Test 4: user "sub_sub_child_user" that belongs to the "subsubchild1" group, that on the third level after the root.
#Expected: True
print("Test 4:", is_user_in_group("sub_sub_child_user", parent))
#Test 5: Look for user "Juan" that is not in the hierarchy.
#Expected: False
print("Test 5:", is_user_in_group("Juan", parent))
#Test 6: Look for user "Juan" in an empty group.
#Expected: False
print("Test 6:", is_user_in_group("Juan", empty_group))
#Test 7: Look an empty string as parameter for the user name.
#Expected: False
print("Test 7:", is_user_in_group("", empty_group))
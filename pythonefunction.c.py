my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
my_set = {1, 2, 3}
my_set.clear()
print(my_set)
my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set_difference = set1.difference(set2)
print(set_difference)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)
print(set1)
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)
set1 = {1, 2, 31, 4}
set2 = {3, 4, 5, 6}
set_intersection = set1.intersection(set2)
print(set_intersection)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)
set1 = {1, 2}
set2 = {1, 2, 3, 4}
result = set1.issubset(set2)
print(result)
set1 = {1, 2, 3, 4}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)
my_set = {1, 2, 3, 4}
popped_element = my_set.pop()
print(popped_element)
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set_symmetric_difference = set1.symmetric_difference(set2)
print(set_symmetric_difference)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print(set1)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)
set
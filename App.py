var_list1 = [1,2,3]
var_list2 = [2,3,4]

var_set1 = set(var_list1)
var_set2 = set(var_list2)


print(var_set1 | var_set2)
print(var_set1 & var_set2)
print(var_set1 ^ var_set2)
print(var_set1 - var_set2)
print(var_set2 - var_set1)

map = {}
map[0] = "0"
map[1] = "1"
map["1"] = "str_1"
print(map)
print(map.keys())
print(map[1])
print(map["1"])
print(map)
import copy

item = {"name": "Roy", "year": 2022}
new_item = item
item['year'] = 2023
print("### same value ###")
print(item)
print(new_item, end="\n\n")

item = {"name": "Roy", "year": 2022}
new_item_copy = copy.copy(item)
item['year'] = 2024
print("### shallow copy ###")
print(item)
print(new_item_copy, end="\n\n")

item = {"grades": [97, 83, 87]}
copied_item = copy.copy(item)
item['grades'][0] = 100
deep_copied_item = copy.deepcopy(item)

item['grades'][0] = 100
print("### deep copy ###")
print(copied_item)
print(deep_copied_item)

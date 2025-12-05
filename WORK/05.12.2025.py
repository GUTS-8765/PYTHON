list_of_dicts = [
    {'a': 11, 'b': 5},
    {'a': 3, 'b': 2},
    {'a': 5, 'b':10}
]
key_value = 'a'
def key_sort(item):
    return item[key_value]
print(sorted(list_of_dicts, key=key_sort))
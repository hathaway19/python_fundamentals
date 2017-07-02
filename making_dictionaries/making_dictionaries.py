# takes two lists and makes a dictionary with the first list being keys and the second, values
def make_dictionary_with_lists(key_list, value_list):
    if len(key_list) < len(value_list):
        temp_list = key_list
        key_list = value_list
        value_list = temp_list
    new_dict = {}
    for i in range(len(key_list)):
        new_dict[key_list[i]] = value_list[i]
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

b = make_dictionary_with_lists(name, favorite_animal)
print b
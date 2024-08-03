def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)


if __name__ == "__main__":
    my_dict = {'a': 5, 'b': 9, 'c': 2}
    print(max_value_key(my_dict))   
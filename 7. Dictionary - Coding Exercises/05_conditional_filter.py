def filter_dict(my_dict, condition):
    return {key: value for key, value in my_dict.items() if condition(key, value)}


if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
    print(filtered_dict)

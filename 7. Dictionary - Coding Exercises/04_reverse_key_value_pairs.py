def reverse_dict(my_dict):
    result = dict()

    for key, value in my_dict.items():
        result[value] = key

    return result


if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(reverse_dict(my_dict))

def firstSecond(my_list):
    max1 = 0
    max2 = 0

    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1, max2


if __name__ ==  "__main__":
    my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
    print(firstSecond(my_list))
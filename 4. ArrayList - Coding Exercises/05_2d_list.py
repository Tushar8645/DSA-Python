def diagonalSum(my_list_2d):
    result = 0

    for i in range(len(my_list_2d)):
        result += my_list_2d[i][i]

    return result


if __name__ == "__main__":
    my_list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonalSum(my_list_2d))

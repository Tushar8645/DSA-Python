# def maxProduct(arr):
#     arr.sort
#     return arr[-1] * arr[-2]


def maxProduct(arr):
    max1 = 0
    max2 = 0

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2


if __name__ == "__main__":
    arr = [1, 7, 3, 4, 9, 5]
    print(maxProduct(arr))

def missingNumber(arr, n):
    total_value = n * (n + 1) // 2
    sum_arr = sum(arr)
    return total_value - sum_arr


if __name__ == "__main__":
    print(missingNumber([1, 2, 3, 4, 6], 6))

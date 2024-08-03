def pairs(arr, target):
    result = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                result.append(f"{arr[i]}+{arr[j]}")

    return result


if __name__ == "__main__":
    arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
    target = 7
    print(pairs(arr, target))

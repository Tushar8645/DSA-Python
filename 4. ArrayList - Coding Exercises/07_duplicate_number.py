def removeDuplicate(nums):
    result = []

    for num in nums:
        if num in result:
            continue
        else:
            result.append(num)

    return result


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 5]
    print(removeDuplicate(nums))

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                if nums[i] + nums[j] == target:
                    print(i, j)


def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 3, 4, 5, 6]
    target = 6
    # nums = [2, 7, 11, 15]
    # target = 9
    # findPairs(nums, target)
    print(twoSum(nums, target))

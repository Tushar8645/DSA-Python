# Array/List - Coding Exercises - LeetCode - Cracking FAANG Interview Questions
---

## 1. Missing Number

Write a function to find the missing number in a given integer array of 1 to 100.

```
Example:
missing_number([1, 2, 3, 4, 6], 6) # 5
```

<br>

## 2. Pairs/Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
<br>
You may assume that each input would have exactly one solution, and you may not use the same element twice.
<br>
You can return the answer in any order.

Example 1:

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Output: Because nums[0] + nums[1] = 9, we return [0, 1]
```

Example 2:

```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

Example 3:

```
Input: nums[3, 3], target = 6
Output: [0, 1]
```

#### Note:

> Write a program to find all pairs of integers whose sum is equal to a given number.

```
[2, 6, 3, 9, 11] 9 --> [6, 3]
```

> Does array contain only positive or negative numbers?

> What if the same pair repeats twice, should we print it array time?

> If the reverse of the pair is acceptable e.g. can we print both (4, 1) & (1, 4) if the given sum is 5.

> Do we need to print only distinct pairs? Does (3, 3) is a valid pair forgiven sum of 6?

> How big is the array?

<br>

## 3. Max Product of Two Integers

Find the maximum product of two integers in an array where all elements are positive.

Example:

```
arr = [1, 7, 3, 4, 9, 5]
max_product(arr) # Output: 63 (9*7)
```

<br>

## 4. Middle Function

Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

Example:

```
myList = [1, 2, 3, 4]
middle(myList) # [2, 3]
```

<br>

## 5. 2D List

Given 2D list calculate the sum of diagonal elements.

Example:

```
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

diagonal_sum(myList2D) # 15
```

<br>

## 6. Best Score

Given a list, write a function to get first, second best scores from the list.
<br>
List may contain duplicates.

Example

```
myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
first_second(myList) # 90 87
```

<br>

## 7. Duplicate Number

Write a function to remove the duplicate numbers on given integer array/list.

Example

```
remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output: [1, 2, 3, 4, 5]
```

<br>

## 8. Pairs

Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

```
pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
Output : ['2+5', '4+3', '3+4', '-2+9']
```

#### Note:

> 4+3 comes from second and third elements from the main list.

> 3+4 comes from third and seventh elements from the main list.

<br>

## 9. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

```
Input: nums = [1,2,3,1]
Output: True
```

`Hint: Use sets`

<br>

## 10. Permutation

<br>

## 11. Rotate Matrix/Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example:

![image.png](2023-05-01_18-45-50-715225fa6b5f82235759d8f9c9d06f26.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```



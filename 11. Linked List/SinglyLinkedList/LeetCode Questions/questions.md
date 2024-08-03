# Singly Linked List - LeetCode Questions

---

## 1. Merge Two Sorted Linked List

You are given the heads of two sorted linked lists list1 and list2.
<br>
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
<br>
Return the head of the merged linked list.

Example 1:

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

Example 2:

```
Input: list1 = [], list2 = []
Output: []
```

Example 3:

```
Input: list1 = [], list2 = [0]
Output: [0]
```

Constraints:

```
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
```

<br>

## 2. Remove Duplicates

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

```
Input: head = [1,1,2]
Output: [1,2]
```

Example 2:

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

<br>

## 3. Remove Linked List Elements

Given the **_head_** of a linked list and an integer **_val_**, remove all the nodes of the linked list that has **_Node.val == val_**, and return the new head.

Example 1:

![Error: Image not found.](removelinked-list.jpg)

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

Example 2:

```
Input: head = [], val = 1
Output: []
```

Example 3:

```
Input: head = [7,7,7,7], val = 7
Output: []
```

Constraints:

- The number of nodes in the list is in the range **_[0, 104]_**.
- **_1 <= Node.val <= 50_**
- **_0 <= val <= 50_**

<br>

## 4. Reverse Linked List

Given the **_head_** of a singly linked list, reverse the list, and return the reversed list.

Example 1:

![Error: Image not found.](rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

Example 2:

![Error: Image not found.](rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
```

Example 3:

```
Input: head = []
Output: []
```

Constraints:

- The number of nodes in the list is the range **_[0, 5000]_**.
- **_-5000 <= Node.val <= 5000_**

<br>

## 5. Palindrome Linked List

Given the **_head_** of a singly linked list, return **_true_** if it is a palindrome or **_false_** otherwise.

Example 1:

![Error: Image not found.](pal1linked-list.jpg)

```
Input: head = [1,2,2,1]
Output: true
```

Example 2:

![Error: Image not found.](pal2linked-list.jpg)

```
Input: head = [1,2]
Output: false
```

Constraints:

- The number of nodes in the list is in the range **_[1, 105]_**.
- **_0 <= Node.val <= 9_**

<br>

## 6. Middle of the Linked List

Given the ***head*** of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

![Error: Image not found.](lc-midlist1.jpg)

```
Input: head = [1,2,3,4,5]
Output: 3
Explanation: The middle node of the list is node 3.
```

Example 2:

![Error: Image not found.](lc-midlist2.jpg)

```
Input: head = [1,2,3,4,5,6]
Output: 4
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

Constraints:

- The number of nodes in the list is in the range **_[1, 100]_**.
- **_1 <= Node.val <= 100_**

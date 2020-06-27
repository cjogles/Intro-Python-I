# STRETCH TASK 2
# DATE = 6/27/2020
# QUESTION https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# EXAMPLES
# 1
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.
# 2
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.

# MY CODE
class Solution:
    def removeDuplicates(self, nums) -> int:
        if (len(nums) == 0):
            return 0
        pointer1 = 0
        for pointer2 in range(1, len(nums)):
            if (nums[pointer1] != nums[pointer2]):
                nums[pointer1 + 1] = nums[pointer2]
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1
        return pointer1 + 1


test1 = Solution()
print(test1.removeDuplicates([1, 2, 3, 3, 3, 4, 4, 5]))  # should return 5

# My Explanation for this solution:
#     - Solution Class removeDuplicate method returns the length(int) of an
#       input(list) after removing all duplicates from the list.
#     - To do this I did the following:
#     - First I took care of the edge case when an input list was length = 0, if so, return 0
#     - I needed a way to iterate through the list IN PLACE and check for duplicates. Then,
#       if a duplicate was present... I needed to account for it somehow. I decided to take a 2 pointer approach.
#       Or in other words, I created two reference points for specific indices in the list/array.
#     - pointer1 starts at index 0, and pointer2 starts at index 1.
#     - if pointer1 == pointer2, I need to increment pointer2 to the next position. That's it.
#     - if pointer1 != pointer2, I need to replace the value right after pointer1 (aka [pointer1 + 1]),
#       with the referenced value of pointer2 AND I need to increment the positions of pointer1 and pointer2 to the next positions.
#     - After checking len(list) times, I should have a list with the unique items at the beginning,
#       and all the duplicates pushed to the back. All that matters is returning the length of non-duplicate items in the input list,
#       so I can now return [pointer1 + 1] because that would be equal to the length of unique items in the list.

# STRETCH TASK 3
# 3. Write a program to determine if a number, given on the command line, is prime.

def solution(num):
    if (num >= 1):
        for x in range(1, num//2):
            if (num % x) == 0:
                return f"{num} is not a prime number"
    return f"{num} is a prime number"
    
# TEST
print(solution(4)) # should return string ==> "{number}is a prime number."

# My explanation for this problem:
# - In order for a number to be considered "PRIME", it needs to be greater then 1, and its only factors can be 1 and itself.
# - To solve this, I would first take care of the edge case of it being less then 1. 

# STRETCH TASK 4
# How can you optimize this program?

# STRETCH TASK 5
# Implement [The Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
# of the oldest algorithms known (ca. 200 BC).
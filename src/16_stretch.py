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
import sys
import math


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
# print(test1.removeDuplicates([1, 2, 3, 3, 3, 4, 4, 5]))  # should return 5

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
    if (num < 1):
        return f"{num} is not a prime number"
    else:
        for x in range(2, num):
            if (num % x) == 0:
                return f"{num} is not a prime number"
    return f"{num} is a prime number"

# TEST
print(solution(13)) # should return string ==> "{number}is a prime number."

# My explanation for this problem:
# - In order for a number to be considered "PRIME", it needs to be greater then 1, and its only factors can be 1 and itself.
# - To solve this, I would first take care of the edge case of it being less then 1, if so, its not prime.
# - next, I realize that every non-negative integer greater then 0 has 1 and itself as its factors. I just need to check if any other
#   number is a factor of the given number. So I take 2 through (num -1), loop through each one of them and run the following:
#   num % x == 0... if that evaluates to true, that means there is a factor of num outside of 1 and itself, which makes it NOT prime.
#   otherwise return prime

# STRETCH TASK 4
# How can you optimize this program?
# ---- going to skip this question for now.

# STRETCH TASK 5
# https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/sieve-of-eratosthenes-prime-adventure-part-4
# Implement [The Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
# of the oldest algorithms known (ca. 200 BC).
# this algorithim finds all prime numbers up to a given limit


# def sieve_of_eratosthenes(limit):
#     candidates = set([*range(2, limit+1)])
#     for x in range(2, (limit+1)):
#         if (x not in candidates):
#             continue
#         composite = x + x
#         while composite < limit + 1:
#             candidates.discard(composite)
#             composite += x
#     return candidates
# # now check number passed via command line
# args = sys.argv[1:]

# if len(args) != 1:
    
#     print("Expected one, and only one, argument.", file=sys.stderr)
#     print("Usage:", file=sys.stderr)
#     print(f"  {sys.argv[0]} <integer>", file=sys.stderr)
#     exit(1)

# number = int(args[0])

# print("^^^^^", number)
# if number <= 0:
#     print("Number must be greater than 0 !", file=sys.stderr)
#     exit(2)

# primes_up_to_number = sieve_of_eratosthenes(number)

# print(str(number in primes_up_to_number))


# print(sieve_of_eratosthenes(45))  # 2, 3, 5, 7, 11
# My explanation for this problem:
# - Basically I just follow the sieve of eratosthenes algorithim to solve this problem. It works in the following way:
# - All numbers from 2 through to the limit given are possible prime numbers. At the beginning, they are all considered "unmarked"
# - Start iterating over each number. If you come across an "unmarked" number, that means its prime.
# - So, you would reach the first number, 2, and you would "mark it" therefore declaring your first prime number.
# - After you mark a prime number, you can now "mark" all multiples of that marked number (2), because we know they are composite (i.e. not prime)
# - After you mark every multiple of 2, you can repeat. The next "unmarked" number is 3. Add this to your list of primes that you collect.
# - Same as before, you can now take multiples of the newly "marked" number (3), and "mark" each of them, declaring them NOT prime.
# - You'll notice that "6" is a multiple of BOTH "2" AND "3". So a neat optimizaation to this algorithim is always start at the square of the newly
#   marked number, when you are "marking off" new composite numbers to declare them NOT prime. That way you don't waste your time looking to "mark"
#   off "6" again.
# - Continue! You'll come across a "marked" number, "4". Since its "marked", you can skip it and you'll come to "5". Repeat the same process
#   you did with "3 and your on your way!"
# - Eventually you'll get to an "unmarked" number whose square is greater then the original limit given at the beginning. Once you've reached
#   this point that means the rest of the unmarked numbers ARE PRIME. Fill in the rest of them as prime and your done!

# when the function is invoked, first ensure that there are only two parameters given
# insure that the two paramters given are both ints, or are both strings
# if all the above is the case, you can now begin, if not, display an error message and instructions
# if both are ints, concatenate as string
# if both are strings, sum as ints

# def silly_function(a, b):
#     if type(a) and type(b) == int:
#         print(str(a) + str(b))
#         pass
#     elif type(a) and type(b) == str:
#         print(int(a) + int(b))
#         pass
#     else:
#         print("none")

# silly_function(2,3)


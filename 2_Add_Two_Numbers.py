import random


class Solution(object):
    def letterCombinations(self, digits):
        t = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl"

        }
        while True:
            numbers = input("Enter number : ")
            lenght = len(numbers)

            for number in numbers:

                print(t[number])


digits = "2"

solution = Solution()
solution.letterCombinations(digits)

"""
Recursion is important to understand Tree and Graph.
Practice again and again.
Every single day, solve a recurtion problem from leet code.

It is important to explain solutions by own words  for interviews, not code base.

https://leetcode.com/problemset/algorithms/?search=Recursion

"""

def factorial(n: int) -> int:
    # base case
    if n == 0:
        return 1
    # recursive case
    return factorial(n-1) * n

print(factorial(5))

# n = 5 -> factorial(4) * 5
# n = 4 -> factorial(3) * 4
# n = 3 -> factorial(2) * 3
# n = 2 -> factorial(1) * 2
# n = 1 -> factorial(0) * 1
# n = 0 -> 1

"""
Excercise Recursion.
"""

# 01.power
def power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return power(base, exponent-1) * base

print(power(2, 3))


# 02.isPalindrome
def isPalindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    return False

print(isPalindrome("madam"))
print(isPalindrome("racecar"))
print(isPalindrome("Hello"))

# 03.printBinary -> watch again around 1:00
def printBinary():
    return

# 04.reverseLines -> watch agein around 1:25
def reverseLines():
    return

"""
Assignment. -> watch again around 1:29

05.evaluate.
Write recursive function evaluate that accepts a string
representing a math expression and computes its value.
- THe expression will be "fully parenthesized" and sill
  consist of + and * n single-digit integers only.
-  You can use a helper function. (Do not change the original function header)
-Recursion

*evaluate("7") -> 7
*evaluate("(2+2)") -> 4
evaluate("(1+(2*4))") -> 9

evaluate("((1+3)+((1+2)*5))") -> 19

"""

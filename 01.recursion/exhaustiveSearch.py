# 01.printBinary
# -> printBinary(n): prints all binary representations for in digits.
# -> parameter n: the number of digits.
def printBinaryExhoustiveHelper(n: int, soFar: str = "", indent: str = ""):
    print(f"{indent} {printBinaryExhoustiveHelper.__name__} n={n}, soFar={soFar}")
    if n == 0:
    # no more choices to make -> stop
        print(soFar)
    else:
    #  choose one & recursive search
        for i in range(2):
            printBinaryExhoustiveHelper(n-1, soFar + str(i), indent + "  ")

def printBinaryExhoustive(n: int):
    printBinaryExhoustiveHelper(n, "")

# print(printBinaryExhoustive(3))



# 02.printDecimal
def printDecimalExhoustiveHelper(n: int, soFar: str = ""):
    if n == 0:
    # no more choices to make -> stop
        print(soFar)
    else:
    #  choose one & recursive search
        for i in range(10):
            printDecimalExhoustiveHelper(n-1, soFar + str(i))

def printDecimalExhoustive(n: int):
    printDecimalExhoustiveHelper(n, "")

# print(printDecimalExhoustive(2))



# 03.permutations O(n!)
def permutationHelper(word: str, soFar: str = "", indent: str = ""):
    print(f"{indent} {permutationHelper.__name__} [word={word}, soFar={soFar}]")
    if len(word) == 0:
        #  no more characters to choose -> stop
        print(soFar)
    else:
        for i in range(len(word)):
            c = word[i]
            permutationHelper(word[0:i] + word[i+1:len(word)], soFar + c, indent + "  ")


# def permutationUnique(word: str, soFar: str = ""):
#     if len(word) == 0: 
#         for w in set(soFar):
#             print(w)
#     else:
#         for i in range(len(word)):
#             c = word[i]
#             permutationUnique(word[0:i] + word[i+1:len(word)], soFar + c)


def permutation(word: str):
    permutationHelper(word)
    # permutationUnique(word)

print(permutation("park"))
# print(permutation("parr"))


"""
Excercise: combinations

@Write a recursive function combinations that accepts a string
s and an integer k as parameters and outputs all possible k-letter strings
that can be formed from unique letters in that string.
The arrangements maybe output in any order.

@Example:
combinations("GOOGLE", 3)
-> EGL, EGO, ELG, ... OLE, OLG.

@To simplify the problem, you may assume that the string a contains
at least k unique chars.
"""
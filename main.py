# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams():
    first_word = input("Enter First word:")
    second_word = input("Enter Second word:")

    if len(first_word) != len(second_word):
        return False
# A for loop to check if the characters in the first word are the same with the secod word
    for char in first_word:
        if char not in second_word:
            return False
        else:
            return True



print(find_anagrams())
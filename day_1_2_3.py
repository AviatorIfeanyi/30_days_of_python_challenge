## Day 1

# Create a function that takes a list and string. 
# The function should remove the letters in the string from the list, and return the list.


# remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

#remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

#remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
#Notes
#If number of times a letter appears in the list is greater than the number of times the letter appears in the string, the extra letters should be left behind (see example #2).
# #If all the letters in the list are used in the string, the function should return an empty list (see example #3).

# Code source https://edabit.com/challenge/gH3QMvF3czMDjENkk

# def remove_letters(letters, word):
# 		for letter in word:
# 			if letter in letters:
# 				letters.remove(letter)
# 		return letters

# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") )


# ===============================
# Alternative solution

# def remove_letters(list_letters, str_word):
#     [list_letters.remove(letter) for letter in str_word if letter in list_letters]
    
#     return list_letters

# letters = ["s", "t", "r", "i", "n", "g", "w"]
# word = 'string'

# print(remove_letters(letters, word))

# ============================================================================================================



# ==========================================
# Day 2
# ==========================================

# https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb

# Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
# Examples

# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

# consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

# consecutive_combo([44, 46], [45]) ➞ True

# Notes

#     The input lists will have unique values.
#     The input lists can be in any order.

# def consecutive_combo(lst1, lst2):
#   lst3 = set(sorted(lst1 + lst2) )
  
#   return list(range(min(lst1), max(lst2)+1)) == list(lst3)

# print(consecutive_combo([3, 1, 4, 6, 5], [2, 7, 8, 9]))


# =======================================
# Day_3
# =======================================
# Write a function that takes an array of numbers and finds the second lowest
# and second greatest number

# def second_lowest_and_highst_num(arr):
#   min_num = min(arr)
#   max_num = max(arr)
  
#   arr_sort = sorted(set(arr) ) 
  
#   return (arr_sort[arr_sort.index(min_num) + 1], arr_sort[arr_sort.index(max_num) - 1] )
    
# print(second_lowest_and_highst_num([3,10,9, 0, 9, 4, 1,3,5])  )


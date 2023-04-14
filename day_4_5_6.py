# ========================================================
# # Day_4
# Source: 
# Edabit: https://edabit.com/challenge/zJSF5EfPe69e9sJAc
# ================================================

# Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.
# Examples

# def censor_string(txt_str, lst, censor_char):
#   str_list = txt_str.split(" ")
#   for word in str_list:
#     if word in lst:
#       word_index = str_list.index(word)
#       str_list[word_index]= censor_char * len(word)
#   return " ".join(str_list)

# print(censor_string("Today is a Wednesday!", ["Today", "a"], "-") )

# # censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")


# ===============================================
# day_5
# Write a function to check whether a passed string is a palindrome or not 
# ===============================================

# def check_palindrome(palindrome):
#   reverse_palindrome = ''
#   palindrome_length = len(palindrome)
  
#   for _ in palindrome:
#     reverse_palindrome += palindrome[palindrome_length - 1]
#     palindrome_length -= 1
    
#   return palindrome == reverse_palindrome

# print(check_palindrome('redder'))

# ================================================
# day_6
# ================================================

# def is_disarium(arg):
#   lst_number = list(str(arg))
#   number_counter = 0
#   for int_number in lst_number:
#     number_counter+=int(int_number) ** (lst_number.index(int_number) + 1) 
#   return number_counter == arg

# print( is_disarium(75) )



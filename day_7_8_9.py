# =================================
# Day_7
# =========================

# def factors_positive_integers(integer):
#   factors = integer
  
#   for integer_number in range(1, integer):
#     factors *= (integer - integer_number)

#   return factors

# print(factors_positive_integers(5) )


# ===================================
# day_8
# +============================
# def divisible_by_b(a, b):
# 	return b * (a // b + 1)


# ==============================
# day_9
# ++++++++++++++++++++++++++++

# def profit(product):
# 	total_sales = product["sell_price"] * product["inventory"]
# 	total_cost = product["cost_price"] * product["inventory"]
# 	return round(total_sales - total_cost)
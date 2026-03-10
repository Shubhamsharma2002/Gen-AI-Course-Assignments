# Task 1 & 2: Importing Modules
import math_utils
from math_utils import square
import string_utils

# Task 4: Importing the Package
import shop_package.discount as disc
from shop_package.billing import calculate_total

# Testing Task 1
print(f"Math Add: {math_utils.add(10, 5)}")
print(f"Math Square: {square(4)}")

# Testing Task 2
text = "hello world"
print(f"Capitalized: {string_utils.capitalize_words(text)}")
print(f"Reversed: {string_utils.reverse_string(text)}")
print(f"Word Count: {string_utils.word_count(text)}")

# Testing Task 3 & 4 (Package)
price_list = [100, 200, 300]
total = calculate_total(price_list)
discounted = disc.apply_discount(total, 10)

print(f"Total Bill: {total}")
print(f"After 10% Discount: {discounted}")
print(f"Flat Discount on $100: {disc.flat_discount(100)}")
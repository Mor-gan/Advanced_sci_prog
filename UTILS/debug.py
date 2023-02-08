# a = 5

# b = 6

# c = a + b

# print(c)


# def my_function():
#     a = 3
#     b = 8
#     c = a+b
#     return c

# d = 5
# e = my_function()
# f = d * e 
# print(f)

import datetime
import string

puncs = len(string.punctuation)
year = datetime.date.today().year
ppy = puncs // year

d = 42 / ppy

print(d)
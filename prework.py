# Question 1
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function.
# The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"Hello_{user_name}")
hello_name("USERNAME")

# Question 2

# Write a python function, 
# first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range (1, 101):
        if number % 2 != 0:
            print(number)
first_odds()

# Question 3

# Please write a Python function, max_num_in_list to return the
# max number of a given list.
# The first line of the code has been defined as below.
 

def max_number_in_list(a_list):
    max = a_list[0]
    for num in a_list:
        if num < max:
            max = num
        return max
my_list = [1,10000, 129342, 192304, 9342202, 101010101]
max_number = max(my_list)
print(max_number)

# Question 4

# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_a_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0): 
        return True
    else:
        return False
year= is_a_leap_year(1500)
year = is_a_leap_year(1600)
year = is_a_leap_year(1996)
print(year)

# Question 5

# Write a function to check to see if all numbers in list
# are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(a_list):
    first_num = a_list[0]
    for num in a_list[1:]: # to include index 1 and everything after
        if num != first_num + 1:
            return False
        first_num = num
    return True

crazy_list = [1,2,3,4,5,6,7, 9]
correct_list = [1,0,1,]
correct = is_consecutive(correct_list)
crazy = is_consecutive(crazy_list)
print(crazy)
print(correct)

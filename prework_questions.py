# Question 1;
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Prints message with entered username in uppercase formatting"""
    print('hello_' + user_name.upper())

hello_name('troy')


# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Prints odd numbers within range 1 through 100"""
    for oddNum in range(1, 100, 2):
        print(oddNum)
    
print(first_odds())


# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Returns the highest number in a given list"""
    maxNum = max(a_list)
    return maxNum

max_num_in_list([101, 5, 4, 33, 1023, 55])
max_num_in_list([3, 8, 4 2])


# Question 4:
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Determines if entered year can be divided evenly by 4, as well as 100 and 400, to identify if leap year"""
    if (a_year / 4) % 2 == 0:
        return True
    elif (a_year / 100) % 2 == 0 and (a_year / 400) % 2 == 0:
        return True
    else:
        return False 

print(is_leap_year(2024))
print(is_leap_year(1933))


# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive_list(a_list):
    """Checks if the next number in list is equal to current number plus one. If so, returns true, otherwise returns false."""
    for num in a_list:
        if a_list[num] + 1 == a_list[num + 1]:
            return True
        else:
            return False
    
is_consecutive_list([1, 2, 3, 4, 5, 6])
is_consecutive_list([4, 5, 8, 9, 10])

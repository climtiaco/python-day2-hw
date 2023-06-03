from math import factorial

#1. Write a Python function called max_num()to find the maximum of three numbers.

def max_num(*nums):
    return max(nums)


#2 Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(*list):
    result = 1
    for i in list:
        result = result * i
    return result


#3 Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    return str[::-1]

# Notes:
#   "[start:stop:step]" is the slicing method for python. the "::" part tells it to start and stop and the -1 actually makes it reverse.

#4 Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(number, start, finish):
    if number >= start and number <= finish:
        return True
    else:
        return False


#7 Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(numRows):
    for i in range(numRows):
        # Loop to get leading spaces
        for j in range(numRows-i+1):
            print(end="")
        #loop to get elements of row i
        for j in range(i+1):
        # nCr = n!/((n-r)!*r)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end="")
        print("\n")



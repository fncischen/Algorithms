#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# cookie monster can eat 

# 0 cookie
# 1 cookie
# 2 cookies
# 3 cookies // constraint

# count how many ways to eat N cookies inside a jar  
# mouth c

# n number of cookies
# 5 

# 5,4,3,2,1,0


# zero = 0
# one = 1
# two = 2
# three = 3 

# n = 1 cookies
  # return 1
 # 1 []

# n = 2 cookies
  # return 2

 # 1 1 # old
 # 2 0 # new 
# n = 3 cookies
  # return 4 

 # 1 1 1 # old 
 # 1 2  # ne
 # 2 1  # new 
 # 3 # new  

# [3] -> depending on the size of n, we can place 1 or 2 or 3 here
# [2] -> depending on the size of n, we can place 1 or 2 here
# [1] -> depending on the size of n, we can place all 1s here 

# let the size of n drive the combinations of 1s and 2s that add up to n. 
# for each amount of cookies to be eaten

# 5 - 2 = 3 -> use recursion to get eating_cookies(3)
# 5 - 3 = 2 -> use recursions to get eating_cookies(2)
# 5 - 1 = 4 -> use recursion to get eating cookies(1)

#[2 1 2]
#[2 2 1]
#[2 1 1 1]

def eating_cookies(n, cache=None):
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  elif n > 3:
    three = eating_cookies(n-3)
    two = eating_cookies(n-2)
    one = eating_cookies(n-1)
    total_cookies = three + two + one
    return total_cookies

print(eating_cookies(5))

# 5 cookies 

# category 3
# [3 1 1]
# [1 3 1]
# [1 1 3]
# [3 2]
# [2 3]

# category 2

# [2 1 1 1]
# [1 2 1]
# [2 1 2]
# [2 2 1]
# [1 2 1 1]
# [1 1 2 1]
# [1 1 1 2]

# category 1

# [1 1 1 1 1]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
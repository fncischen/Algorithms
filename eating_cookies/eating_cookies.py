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


# 5 = 5

# 5 = 3 + 2
# 5 = 2 + 2 + 1
# 5 = 1 + 1 + 3
# 5 = 1 + 1 + 1 + 2
# 5 = 1 + 1 + 1 + 1 + 1

# zero = 0
# one = 1
# two = 2
# three = 3 

# way 1
    # 12pm: eat 1 cookie, 3pm: eat 1 cookie, 6pm: eat 1 cookie 
        (1,1,1)
# way 2:
    # 12pm: eat 1 cookie, 3pm: eat 2 cookies
        (1,2,0)
# way 3:
    # 12pm: eat 2 cookies, 3pm: eat 1 cookie
        (2,1,0)
# way 4:
    # 12pm: eat 3 cookies, all at once
        (3,0,0)
def eating_cookies(n, cache=None):


  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
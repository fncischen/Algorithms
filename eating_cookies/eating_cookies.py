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

# 

# i.e. [2, ]
# 4 - 2 = 2 

# 5 - 2 = 3 -> use recursion to get eating_cookies(3)

#[2 1 2]
#[2 2 1]
#[2 1 1 1]

# let's figure out how many ways to break down 2 cookies
# # we know that n = 2 cookies gives us 1 1 or 2  

# 10 - 2 = 8

# lets figure out how many ways to break down 8 cookies



## after base case
# n = 4 
  # return 7 

 

  # 4
  # 4 = 3 + 1 + 0 + 0 [ add 1]
  # 4 = 1 + 3 [ add 1, new since 3 ]
  # 4 = 2 + 2 [ add 2 ]
  # 4 = 1 + 1 + 1 + 1 [ add 1, but same ]
 
 
  # 4 = 1 + 1 + 2 + 0 [add 1, but same ]
  # 4 = 1 + 2 + 1 + 0 [ same ]
  # 4 = 2 + 1 + 1 + 0 [ same ]

# n = 5
  # return 12 

  # 5 = 3 + 2
  # 5 = 2 + 3
  # 5 = 2 + 2 + 1
  # 5 = 1 + 2 + 2 
  # 5 = 1 + 1 + 3
  # 5 = 3 + 1 + 1 
  # 5 = 1 + 3 + 1 
  # 5 = 1 + 1 + 1 + 2
  # 5 = 1 + 1 + 2 + 1
  # 5 = 1 + 2 + 1 + 1 
  # 5 = 2 + 1 + 1 + 1 
  # 5 = 1 + 1 + 1 + 1 + 1

# n = 6
  # return 20

  # 6 = 3 + 3
  # 6 = 1 + 2 + 1 + 2
  # 6 = 2 + 2 + 1 + 1
  # 6 = 1 + 1 + 2 + 2
  # 6 = 2 + 1 + 2 + 1
  # 6 = 1 + 2 + 2 + 1
  # 6 = 1 + 1 + 1 + 3
  # 6 = 1 + 1 + 3 + 1
  # 6 = 1 + 3 + 1 + 1
  # 6 = 3 + 1 + 1 + 1
  # 6 = 3 + 2 + 1
  # 6 = 2 + 3 + 1
  # 6 = 1 + 2 + 3
  # 6 = 


## have array of length n

# determine how many ways you can add up to n 
# 1 1 1 1 1 1 
# 1 2 1 2 1
# 2,1,2,1,2


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
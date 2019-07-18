#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# n = 1 cookies
  # return 1
 # 1

# n = 2 cookies
  # 1 1
  # 2 0
  # return 2

# n = 3 cookies
  # return 4 

 # 1 1 1  
 # 1 2  
 # 2 1  
 # 3   


# for 4: how did I come up with recursion pattern:

# we know that the cookie can either eat 0, 1, 2, or 3 cookies at a time

# step 1) set up three categories
 
    # eating 3 cookies at a time 
    # [3 ... ]

    # eating 2 cookies at a time
    # [2 ...]

    # eating 1 cookie at a time
    # [1 ...]

    # [3] -> depending on the size of n, we can place 1 or 2 or 3 here
    # [2] -> depending on the size of n, we can place 1 or 2 here
    # [1] -> depending on the size of n, we can place all 1s here

# step 2) subtract x cookies from n. i.e. 

  # 5 - 3 = 2 
  # 5 - 2 = 3 
  # 5 - 1 = 4

# step 3) for the cookies on set 3, use recursion to find the remaining amount of cookies eating at each time to get n cookies eaten
# and count how many times

# i.e. 
    # 4 cookies

      # category 3 (4 - 1 = 3)
      
      # [2 ,1] -> [3 1]
      # [1,2] -> [1 3]
      # [3] -> [1 2 1]
      # [1 1 1] -> [1 1 1 1]

      # category 2 (4 - 2 = 2)
      # [1,1] -> [1 1 2]
      # [2] -> [2 2]

      # category 1 (4 - 3 = 1)
      # [1] -> [1 2 1]

    # 5 cookies  #### recrusion mode

    # category 3 (5 - 2 = 3)
      # [this category has all 3s]

      # [3 1 1]
      # [1 1 3]
      # [3 2]
      # [2 3]

    # category 4 (5 - 1 = 4)
   
    # [4 -> 2,2 -> this category has lots of 2,2s]

    # [1 2 1]
    # [2 1 2]
    # [2 2 1]
    # [2 1 1 1]
    # [1 2 1 1]
    # [1 1 2 1]
    # [1 1 1 2]

    # category 2 (5 - 3 = 2)
    # [ 2s can be 1,1s]

    # [1 1 1 1 1]
    # [1 3 1]


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

print(eating_cookies(4))
print(eating_cookies(5))
print(eating_cookies(10))
# print(eating_cookies(100))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
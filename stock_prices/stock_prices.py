#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass

# assume low price at buy, sell high. 

# find differences between big and small 
# loop through each item and compare the other items

# generate a for loop for all the other items to compare // subtract differences

# compare the possible differences

    # [ create an array of differences ]
    # [ [ difference btwn a1 and a2 .......]] 
    # [ [ differnece btwn a2 and a1, a3...]]
    
    # use sort 

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
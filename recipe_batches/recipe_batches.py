#!/usr/bin/python

import math

# loop through each ingredient to check if 
  # the batch amount on recipie[key] is less than the ingredients[key]

  # if less than, automatically return zero and end loop
  # else calculate the modulus for this ingredient and insert into array of modulus

  # after calculating all the modului of each recipe
  # search for the minimum modului in the array, and then return that number. 

def recipe_batches(recipe, ingredients):

  batchModuli = []

  for key in recipe: 
      if ingredients[key] < recipe[key]:
        return 0 
      else:
        batchModuli.append(math.floor(ingredients[key]))

  
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
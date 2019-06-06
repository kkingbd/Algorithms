#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
  batches = []
  for item in recipe:
    if item not in ingredients:
      return 0
    elif recipe[item] > ingredients[item]:
      return 0
    else:
      batches.append(math.floor(ingredients[item]/recipe[item]))
  return min(batches)
    

  

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 232, 'butter': 408, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
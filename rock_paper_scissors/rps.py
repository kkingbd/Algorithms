#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  outcome = []
  def find_outcome(n, result):
    if n == 0:
      outcome.append(result)
      return

    for i in options:
      find_outcome(n - 1, result + [i])


  find_outcome(n, [])
  return outcome

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
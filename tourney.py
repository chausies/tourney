<<<<<<< HEAD
def tourney_in_order(k):
  """
  Tells you the bracket for a tourney with n=2^k competitors 1-n, where 1
  is the best. The bracket is such that competitors lose in the order of
  their skill to the person with a level of skill as close to theirs as
  possible.

  >>> bracket = tourney_in_order(4)
  >>> print bracket
  [16, 8, 15, 4, 14, 7, 13, 2, 12, 6, 11, 3, 10, 5, 9, 1]
  """
  n = 2**k
  bracket = [None]*n
  i = n
  for r in range(k+1):
    m1 = 2**(r+1)
    m2 = 0 if r==0 else (2**r -1)
    j = m2
    while j < n:
      bracket[j] = i
      j += m1
      i -= 1
  return bracket

def tourney_fair(k):
  """
  Tells you the bracket for a tourney with n=2^k competitors 1-n, where 1
  is the best. The bracket is optimally fair subject to making competitors
  lose in the correct round.
  >>> bracket = tourney_fair(4)
  >>> print bracket
  [16, 8, 12, 4, 14, 6, 10, 2, 15, 7, 11, 3, 13, 5, 9, 1]
  """
  n = 2**k
  bracket = [n]
  s = n/2
  for _ in range(k):
    bracket += [ i - s for i in bracket ]
    s /= 2
  return bracket

from math import log, ceil
def next_2exp(n):
  """
  Returns the exponent of the next largest power of 2. I.e. returns
  ceil(log2(n)). Helpful for switching from n=2^k to k.
  >>> next_2exp(19)
  5
  """
  if n <= 0:
    return -float("inf")
  return int(ceil(log(n, 2)))
=======
""" Initial empty file """
>>>>>>> 6f3aaec05b72af04d4cddd5bac0f4ce4a84e4838

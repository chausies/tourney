def bitonic_comps(k):
  """Returns the matches to play for a Bitnoic Tourney (An effecient
  tourney that completely sorts competitors)

  Given `2^k` competitors, returns `R` rounds with `n/2` matches each to
  play in order to not only find 1st place, but assign places to everyone.
  The number of rounds `R` is `k*(k-1)/2`, which is insanely effecient. 

  For every match `(i, j)`, competitors `i` and `j` fight. If `j` wins, then
  `j` and `i` swap ranks (competitor `i` will now be `j`, competitor `j`
  will now be `i`).

  Parameters
  ----------
  k : positive int
    `2^k` is the number of competitors in the tourney.

  Returns
  -------
  comps : list of lists of tuples
    `comps` is a list of `round`'s
    `round`'s are a lists of `match`'s
    `match`'s are tuples of the form (i, j), where `i` and `j` are the
        current ranks of the competitors to fight.

  Example
  -------
  Hold a bitonic tourney with 8 competitors
  >>> comps = bitonic_comps(3)
  >>> competitors = [0, 7, 3, 6, 5, 1, 2, 4]
  >>> for rnd in comps:
  ...   for match in rnd:
  ...     i, j = match[0], match[1]
  ...     if competitors[i] > competitors[j]:
  ...       # swap the places (current ranks) of the competitors if 
  ...       # they are in the incorrect order
  ...       competitors[i], competitors[j] = competitors[j], competitors[i]
  >>> print competitors
  [0, 1, 2, 3, 4, 5, 6, 7]
  """

  if k == 0:
    return []
  comps = []
  c = bitonic_comps(k-1)
  for r in c:
    curr_r = list(r)
    for g in r:
      curr_r.append((g[0]+2**(k-1), g[1]+2**(k-1)))
    comps.append(curr_r)
  curr_r = []
  for i in xrange(2**(k-1)):
    curr_r.append((i, 2**k - i - 1))
  comps.append(curr_r)
  s = 2**(k-1)
  while s > 1:
    curr_r = []
    for l in xrange(2**k/s):
      for i in xrange(0, s/2):
        j = i + l*s
        curr_r.append((j, j+s/2))
    comps.append(curr_r)
    s /= 2
  return comps

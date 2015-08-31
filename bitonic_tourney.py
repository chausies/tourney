def bitonic_comps(k):
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

from pprint import pprint
from pylab import permutation
perm = lambda n : list(permutation(n))
k = 4
a = perm(range(2**k))
comps = bitonic_comps(k)
pprint(comps)
for r in comps:
  for g in r:
    if a[g[0]] > a[g[1]]:
      a[g[0]], a[g[1]] = a[g[1]], a[g[0]]
print a

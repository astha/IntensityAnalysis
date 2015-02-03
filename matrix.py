from numpy import *
import sys
import operator
from operator import itemgetter

# run as python pagerank.py positiveAdjectivesFile negativeAdjectivesFile

def cosine_func(a, b):
  return dot(a, b) / (apply_along_axis(linalg.norm, 0, a) * apply_along_axis(linalg.norm, 0, b))

f = open(sys.argv[1], 'r')

pos_points = f.readlines();
f.close()
words = [s.split(' ', 1)[0] for s in pos_points]

pos_points = [ [float(x) for x in s.split()[1:]] for s in pos_points]
points = array(pos_points)
count = points.shape[0]

print "WORDS ",
for word in words:
  print ", " + word,
print

for i in range(count):
  print words[i],
  for j in range(count):
    print ", ", cosine_func(points[i], points[j]),
  print

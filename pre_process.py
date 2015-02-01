from numpy import *
import sys
import operator
from operator import itemgetter

# run as python pagerank.py positiveAdjectivesFile negativeAdjectivesFile

f = open(sys.argv[1], 'r')

line = f.readline()
while line.strip()!="":
  line = f.readline()
line = f.readline()

words = line.split(' ')

for i in range(len(words)):
  words[i] = words[i].split('.')[0]

for word in words:
  print word


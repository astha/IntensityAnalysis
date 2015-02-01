from numpy import *
import sys
import operator
from operator import itemgetter

# run as python pagerank.py positiveAdjectivesFile negativeAdjectivesFile

f = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'r')
out = open(sys.argv[3], 'w')

line = f.readline()
line = f.readline()
while line.strip()!="":
  line = f.readline()
line = f.readline()

words = line.split(',')


for i in range(len(words)):
  vector = f2.readline()
  split_word = words[i].strip().split('.')
  while (split_word[0].lower() != vector.split(' ', 1)[0].lower() and i+1 < len(words)):
    i = i+1
    split_word = words[i].strip().split('.')
  
  if (split_word[1] == "a"):
    out.write(vector)

f.close()
f2.close()
out.close()

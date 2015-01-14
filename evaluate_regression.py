from numpy import *
import sys
import operator
from operator import itemgetter

# run as python pagerank.py positiveAdjectivesFile negativeAdjectivesFile

f = open(sys.argv[1], 'r')
pos_points = f.readlines();

f.close()

words = []
ratings = []
for i in range(len(pos_points)):

	word = pos_points[i].split()[0]
	rating = float(pos_points[i].split()[1])

	if(rating > 0):
		words+=[word]
		ratings+=[rating]


words = array(words)
ratings = array(ratings)
print words
print ratings
dict_pos = {}
count = words.shape[0]

print count
for i in range(count):
	dict_pos[words[i]] = i

all_adj = zip(words, ratings)
all_adj = sorted(all_adj, key=itemgetter(1), reverse=bool(int(sys.argv[2]) == 1))

print "\n"
for j, k in all_adj:
	print j + ":\t\t " + str(k)

print "\n"

num_concordant = 0
num_discordant = 0

for i in range(count):
	for j in range(i+1,count):
		if dict_pos[all_adj[i][0]] < dict_pos[all_adj[j][0]]:
			num_concordant+=1
		else:
			num_discordant+=1
if(num_discordant + num_concordant >0 ):
	print "tau = ",float(num_concordant - num_discordant)/(num_concordant + num_discordant)
else:
	print "tau = 0"

summation = 0
for i in range(count):
	d = dict_pos[all_adj[i][0]] - i
	summation += d*d

summation*=6

if(count > 1):
	summation/= float(count**3 - count)
else:
	summation = 1

print "spear = ",1 - summation


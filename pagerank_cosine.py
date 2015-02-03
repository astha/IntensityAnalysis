from numpy import *
import sys
import operator
from operator import itemgetter

# run as python pagerank.py positiveAdjectivesFile negativeAdjectivesFile

f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'r')

pos_points = f.readlines();
neg_points = g.readlines();
f.close()
g.close()

words = [s.split(' ', 1)[0] for s in pos_points] + [s.split(' ', 1)[0] for s in neg_points]

pos_points = [ [float(x) for x in s.split()[1:]] for s in pos_points]
neg_points = [ [float(x) for x in s.split()[1:]] for s in neg_points]

points1 = array(pos_points)
points2 = array(neg_points)

for i in range(len(points1)):	
 	points1[i] = (points1[i] - mean(points1[i]))/std(points1[i])
for i in range(len(points2)):	
 	points2[i] = (points2[i] - mean(points2[i]))/std(points2[i])

dict_pos = {}
dict_neg = {}
count1 = points1.shape[0]
count2 = points2.shape[0]

for i in range(count1):
	dict_pos[words[i]] = i
for i in range(count2):
	dict_neg[words[count1+i]] = i

print dict_pos
print dict_neg


distances = zeros((count1 + count2, count1 + count2))

for i in range(count1):
	for j in range(count2):
		norm1 = apply_along_axis(linalg.norm, 0, points1[i])
		norm2 = apply_along_axis(linalg.norm, 0, points2[j])
		dotp = dot(points1[i],points2[j])
		dotp/=norm1
		dotp/=norm2
		
		distances[i][count1 + j] = 1-dotp
		distances[count1 + j][i] = 1-dotp

# for i in range(count1+count2):
# 	for j in range(count1+count2):
# 		diff = points[i] - points[j]
# 		norm = apply_along_axis(linalg.norm, 0, diff)
# 		distances[i][j] = norm
# 		distances[j][i] = norm
# print distances

for i in range(count1 + count2):
	total = sum(distances[i])
	distances[i] /= total

# initial = random.randn(count1+count2,1)
# for i in range(initial.shape[0]):
# 	initial[i] = abs(initial[i])
# norms = apply_along_axis(linalg.norm, 0, initial)
# initial/=norm

# print distances
for i in range(10):
	distances = dot(distances, distances)
	# initial = dot(distances,initial)
	# norms = apply_along_axis(linalg.norm, 0, initial)
	# initial/=norms

distances_norm = map(sum,zip(*distances)) #sum along columns
maximum = max(distances_norm)
distances_norm /= (maximum / 100)

all_adj = zip(words, distances_norm)
# print distances_norm 
all_adj = sorted(all_adj[:count1], key=itemgetter(1), reverse=True) + sorted(all_adj[count1:], key=itemgetter(1))

print "\n"
for j, k in all_adj:
	print j + ":\t\t " + str(k)

print "\n"
# Kendall tau rank correlation coefficient

num_concordant = 0
num_discordant = 0

for i in range(count1):
	for j in range(i+1,count1):
		if dict_pos[all_adj[i][0]] < dict_pos[all_adj[j][0]]:
			num_concordant+=1
		else:
			num_discordant+=1
print "tau_positive_class = ",float(num_concordant - num_discordant)/(num_concordant + num_discordant)

num_concordant = 0
num_discordant = 0

for i in range(count2):
	for j in range(i+1,count2):
		if dict_neg[all_adj[i+count1][0]] < dict_neg[all_adj[j+count1][0]]:
			num_concordant+=1
		else:
			num_discordant+=1
print "tau_negative_class = ",float(num_concordant - num_discordant)/(num_concordant + num_discordant)

#Spearman's rank correlation coefficient
summation = 0
for i in range(count1):
	d = dict_pos[all_adj[i][0]] - i
	summation += d*d

summation*=6

summation/= float(count1**3 - count1)

print "spear_positive_class = ",1 - summation

summation = 0
for i in range(count2):
	d = dict_neg[all_adj[i+count1][0]] - i
	summation += d*d

summation*=6

summation/= float(count2**3 - count2)

print "spear_negative_class = ",1 - summation,"\n"

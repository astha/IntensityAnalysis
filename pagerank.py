from numpy import *
import sys
import operator
from operator import itemgetter

f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'r')

pos_points = f.readlines();
neg_points = g.readlines();

words = [s.split(' ', 1)[0] for s in pos_points] + [s.split(' ', 1)[0] for s in neg_points]

pos_points = [ [float(x) for x in s.split()[1:]] for s in pos_points]
neg_points = [ [float(x) for x in s.split()[1:]] for s in neg_points]

points1 = array(pos_points)
points2 = array(neg_points)

count1 = points1.shape[0]
count2 = points2.shape[0]

distances = zeros((count1 + count2, count1 + count2))

for i in range(count1):
	for j in range(count2):
		diff = points1[i] - points2[j]
		norm = apply_along_axis(linalg.norm, 0, diff)
		distances[i][count1 + j] = norm
		distances[count1 + j][i] = norm

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

for j, k in all_adj:
	print j + ":\t\t " + str(k)
# initial = dot(distances,initial)
# norms = apply_along_axis(linalg.norm, 0, initial)
# initial/=norms

# print initial
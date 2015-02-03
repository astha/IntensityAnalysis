from numpy import *
import sys
import operator
from operator import itemgetter

# run as python pagerank.py positiveAdjectivesFile negativeAdjectivesFile

def cosine(points1,points2):
	norm1 = apply_along_axis(linalg.norm, 0, points1)
	norm2 = apply_along_axis(linalg.norm, 0, points2)
	dotp = dot(points1,points2)
	dotp/=norm1
	dotp/=norm2
	return dotp

def dist(points1,points2):
	diff = points1 - points2
	norm = apply_along_axis(linalg.norm, 0, diff)
	return norm

f = open(sys.argv[1], 'r')
pos_points = f.readlines();
f.close()
pos_points = [ [float(x) for x in s.split()[1:]] for s in pos_points]

points = array(pos_points)

points = transpose(points)
for i in range(len(points)):	
	#print mean(points[i]), std(points[i])
 	points[i] = (points[i] - mean(points[i]))/std(points[i])
points = transpose(points)
midpoint = (points[0] + points[len(points)-1])/2
for i in range(len(points)):
	# print points[i], midpoint
	print cosine(points[i],midpoint), dist(points[i],midpoint), apply_along_axis(linalg.norm, 0, points[i])






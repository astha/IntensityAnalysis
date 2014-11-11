import sys, re

#run as python regression.py reviewFile ratingFile

from sklearn import linear_model
from numpy import *
adjectives = {}
k = 0
f = open('adjectivelist', 'r')
line = f.readline()
while line:
	adjectives[line.rstrip('\n')] = k
	line = f.readline()
	k += 1
f.close()

size = len(adjectives)

ratingToIntensity = {0: 2, 1: 1, 2: 1, 3: 2} #intensity only
# ratingToIntensity = {0: 0, 1: 1, 2: 2, 3: 3} #normal values
# ratingToIntensity = {0: -2, 1: -1, 2: 1, 3: 2} #signed values

def replaceThreeOrMore(word):
  pattern = re.compile(r"(.)\1\1+", re.DOTALL) #re.DOTALL means . represents any character including '\n'
  return pattern.sub(r"\1", word)

def process(line):
	featureVector = [0] * size
	line = line.replace('\\', ' ')
	words = re.split('[?,.;:~"* !/#]+', line)
	for w in words:
		w = replaceThreeOrMore(w)
		w = w.lower()
		#ignore if it is a stop word
		if(adjectives.has_key(w)):
			featureVector[adjectives[w]] = 1.0
	return featureVector


features = []
rating = []
testFeatures = []
testRating = []
fp = open(sys.argv[1], 'r')
rp = open(sys.argv[2], 'r')
line = fp.readline()
k = 0
print("Reading reviews and ratings ...")
while line:
	if (k % 5 == 0):
		testFeatures.append(process(line))
		testRating.append([float(ratingToIntensity[int(rp.readline())])])
	else:
		features.append(process(line))
		rating.append([float(ratingToIntensity[int(rp.readline())])])
	line = fp.readline()
	k += 1
fp.close()
rp.close()

print("Learning regression values ...")

clf = linear_model.LinearRegression()
clf.fit(features, rating)
for i in range(len(clf.coef_[0])):
	if (abs(clf.coef_[0][i]) > 100000): #removing arbitrary values
		clf.coef_[0][i] = 0
	
obtainedRating = clf.predict(testFeatures)
diff = array(testRating) - array(obtainedRating)
error = sum(abs(diff))

print "Total Error for " + str(len(testRating)) + " reviews = " + str(error)
# print(clf.coef_)

for x,y in zip(sorted(adjectives.keys()), clf.coef_[0]):
	print x + " " + str(y)




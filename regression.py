import sys, re

# presence feature vector
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
while line:
	if (k % 5 == 0):
		testFeatures.append(process(line))
		testRating.append([float(rp.readline())])
	else:
		features.append(process(line))
		rating.append([float(rp.readline())])
	line = fp.readline()
	k += 1
fp.close()
rp.close()

print("Learning regression values")

clf = linear_model.LinearRegression()
clf.fit(features, rating)
for i in range(len(clf.coef_[0])):
	if (clf.coef_[0][i] > 100000 or clf.coef_[0][i] < -100000):
		clf.coef_[0][i] = 0
	
obtainedRating = clf.predict(testFeatures)
diff = array(testRating) - array(obtainedRating)
error = sum(abs(diff))

# print(clf.predict([[1]]))
print "Total Error for " + str(len(testRating)) + " reviews = " + str(error)
# print(clf.coef_)





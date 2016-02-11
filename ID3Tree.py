import math

trainingData = []
attributes = []



class Node:
	def __init__(self, parent=None):
		self.parent = parent
		self.left = None
		self.right = None
		self.attribute = None
		self.label = None

def getMajority(data):
	count = [0,0,0]
	for d in data:
		if(d[4] == 1):
			count[0] += 1
		elif(d[4] == 2):
			count[1] += 1
		else:
			count[2] += 1

	return max(count)

def chooseBestAttr(data, attributes):
	best = None
	minEntropy = 1.7976931348623157e+308
	for attr in attributes:
		newEntropy = totalEntropy(data, attr)
		if newEntropy < minEntropy:
			minEntropy = newEntropy
			best = attr
	return best

def splitData(data, attribute):
	index = attribute[0]
	value = attribute[1]
	result = [[],[]]
	for d in data:
		if(d[index]<=value):
			result[0].append(d)
		else:
			result[1].append(d)
	return result

def buildID3Tree(data, attributes, root):
	data = data[:]
	vals = [cur[4] for cur in data]

	#if it runs out of splitting attributes
	#return the most popular label in the node
	if not data or (len(attributes)-1)<=0:
		root.label = getMajority(data)
		return 
	elif vals.count(vals[0]) == len(vals):
		root.label = vals[0]
		return 
	else:
		best = chooseBestAttr(data, attributes)
		subData = splitData(data, best)
		newAttr = attributes[:]
		newAttr.remove(best)
		root.attribute = best 
		root.left = Node(root)
		root.right = Node(root)
		buildID3Tree(subData[0],newAttr,root.left)
		buildID3Tree(subData[1],newAttr,root.right)
	return


def ID3Tree(data, attributes):
	root = Node()
	buildID3Tree(data, attributes, root)
	return root

def loadData():
    f = open('hw3train.txt', 'r')
    global trainingData, attributes
    trainingData = [map(float, line.split()) for line in f]
    lists = [list() for _ in xrange(4)]

    for data in trainingData:
    	for i in range(len(lists)):
    		lists[i].append(data[i])
	for i in range(len(lists)):
		lists[i].sort()
    for i in range(len(lists[0])-1):
    	for j in range(len(lists)):
    		attributes.append([j, (lists[j][i]+lists[j][i+1])/2])

def entropy(a, b, c):
    sum = float(a+b+c)
    if(sum == 0):
    	return 0
    a = float(a/sum)
    b = float(b/sum)
    c = float(c/sum)
    entro = 0
    if(a!=0):
    	entro += - (a) * math.log(a, 2)
    if(b!=0):
    	entro += - (b) * math.log(b, 2)
    if(c!=0):
    	entro += - (c) * math.log(c, 2)
    return entro

def totalEntropy(rawdata, attr):
    intlist = [0] * 6
    total = 0
    for data in rawdata:
        label = data[4]
        if data[attr[0]] > attr[1]:
        	intlist[int(label)-1] += 1
        else:
        	intlist[int(label)+2] += 1

    for i in intlist:
        total+=i
    ProbGre =  float((intlist[0]+intlist[1]+intlist[2])/total)
    ProbLeq =  float((intlist[3]+intlist[4]+intlist[5])/total)
    return ProbGre*entropy(intlist[0],intlist[1],intlist[2]) \
            + ProbLeq*entropy(intlist[3],intlist[4],intlist[5])

def printTree(root):

    return


def main():
	loadData()
	print totalEntropy(trainingData, [0, 4.35])
	root = ID3Tree(trainingData, attributes)

	#printTree(root)

main()





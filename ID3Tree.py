import math

trainingData = []
attributesData = []



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
	minEntropy = 1
	for attr in attributes:
		newEntropy = totalEntropy(data, attributes)
		if newEntropy > minEntropy:
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
		newAttr = attribute[:]
		newAttr.remove(best)
		root.attribute = best 
		root.left = Node(root)
		root.right = Node(root)
		buildID3Tree(subData[0],newAttr,root.left)
		buildID3Tree(subData[0],newAttr,root.right)

	return


def ID3Tree(data, attributes):
	return (data, attributes, Node())



def loadData():
    f = open('hw3train.txt', 'r')
    trainingData = [map(float, line.split()) for line in f]
    listx1 = []
    listx2 = []
    listx3 = []
    listx4 = []
    length = len(listx1)
    for data in trainingData:
        listx1.append(data[0])
        listx2.append(data[1])
        listx3.append(data[2])
        listx4.append(data[3])
    for i in range(length-1):
        trainingData.append([1, ((listx1[i]+listx1[i+1])/2)])
        trainingData.append([2, ((listx2[i]+listx2[i+1])/2)])
        trainingData.append([3, ((listx3[i]+listx3[i+1])/2)])
        trainingData.append([4, ((listx4[i]+listx4[i+1])/2)])



def entropy(a, b, c):
    sum = float(a+b+c)
    a = float(a/sum)
    b = float(b/sum)
    c = float(c/sum)
    entro = - (a) * math.log(a, 2) \
            - (b) * math.log(b, 2) - (c) * math.log(c, 2)
    return entro

def totalentropy(rawdata, attr):
    intlist = [0] * 6
    sum = 0
    for data in rawdata:
        label = data[:-1]
        if data[attr[0]] > attr[1]:
            if label == 1:
                intlist[0] +=1
            elif label == 2:
                intlist[1] +=1
            else:
                intlist[2] +=1
        else:
            if label == 1:
                intlist[3] +=1
            elif label == 2:
                intlist[4] +=1
            else:
                intlist[5] +=1
    for int in intlist:
        sum+=int
    ProbGre =  float((intlist[0]+intlist[1]+intlist[2])/sum)
    ProbLeq =  float((intlist[3]+intlist[4]+intlist[5])/sum)
    return ProbGre*entropy(intlist[0],intlist[1],intlist[2]) \
            + ProbLeq*entropy(intlist[3],intlist[4],intlist[5])

def printTree(root):
    return


def main():
    root = ID3Tree()
    printTree()






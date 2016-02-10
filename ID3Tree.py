import math

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
		else
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

def printTree(root):

def main():
	root = ID3Tree()
	printTree()






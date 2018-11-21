import math
import time

tree = [4]
factorialQueque = []
reach = 9
stop = False
cache = [4]

def factorial(n):
	return math.sqrt(2*math.pi*n)*(n/math.e)*n

def isStackable(value,tree,stop):

	root = math.sqrt(value)

	if(math.floor(root) == reach):
		print('llegada 1')
		tree.insert(1,root)
		cache.append(root)
		stop = True

	elif (root == reach):
		print('llegada 2')
		tree.insert(1,root)
		cache.append(root)
		stop = True

	else:
		print(value,root,math.floor(root))

		if (math.floor(root) not in cache ):
			#print(value,root,math.floor(root))
			tree.append(math.floor(root))
			cache.append(math.floor(root))
			tree.append(root)

		if (value - math.trunc(value) == 0 ):
			try:
				temp = math.factorial(value)

				if(temp not in cache and math.floor(temp) not in cache):
					factorialQueque.append(temp)
			except:
				print('overflow')
	

while( tree != [] or stop == False):

	if (len(tree) == 1 and factorialQueque !=[]):
		tree.append(factorialQueque.pop(0))

	current = tree[0]

	isStackable(current,tree,stop)

	if(current == reach):
		stop = True
		break

	#print(tree)
	tree.pop(0)

	print(tree)
	print(factorialQueque)
	print(cache)
	print('-----------')



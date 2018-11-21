import math
import time

tree = [4]
reach = 3
stop = False
cache = [4]

def isStackable(value,tree):

	root = math.sqrt(value)


	if(math.floor(root) == reach):
		print('error1')
		tree.insert(1,root)
		cache.append(root)

	elif (root == reach):
		print('error2')
		tree.insert(1,root)
		cache.append(root)

	else:
		
		if (math.floor(root) not in cache ):
			print(value,root,math.floor(root))
			if(math.floor(root) > reach):
				tree.insert(1,math.floor(root))
			else:
				tree.append(math.floor(root))
			cache.append(math.floor(root))

		if (value - math.trunc(value) == 0):
			try:
				temp = math.factorial(value)

				if(temp not in cache):
					print(temp)
					tree.append(temp)
					cache.append(temp)
			except:
				print('overflow')
	
	tree = sorted(tree, reverse = True)

	print(tree)
	print(cache)

while( tree != [] or stop == False):
	current = tree[0]

	isStackable(current,tree)

	if(current == reach):
		stop = True
		break

	tree.pop(0)



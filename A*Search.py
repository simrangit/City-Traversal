import math
import random
import string

# import networkx as nx
# import matplotlib.pyplot as plt

for i in range(100):
	def random1():
		x = random.randint(1,100)
		return x

Places = {"A":[random1(),random1()],"B":[random1(),random1()],"C":[random1(),random1()],"D":[random1(),random1()],
"E":[random1(),random1()],"F":[random1(),random1()],"G":[random1(),random1()],"H":[random1(),random1()],
"I":[random1(),random1()],"J":[random1(),random1()],"K":[random1(),random1()],"L":[random1(),random1()],
"M":[random1(),random1()],"N":[random1(),random1()],"O":[random1(),random1()],"P":[random1(),random1()],
"Q":[random1(),random1()],"R":[random1(),random1()],"S":[random1(),random1()],"T":[random1(),random1()],
"U":[random1(),random1()],"V":[random1(),random1()],"W":[random1(),random1()],"X":[random1(),random1()],
"Y":[random1(),random1()],"Z":[random1(),random1()]}

print(Places)

BigDict = {}

for k1, value1 in Places.items():
	d = {}
	Big = list()
	for k2, value2 in Places.items():
		if k1 !=k2:
			a = math.pow(value2[0]-value1[0],2)
			b = math.pow(value2[1]-value1[1],2)
			euclid = math.sqrt(a+b)
			euclid = round(euclid,2)
			d[euclid] = k2
	print(k1,d)
	sorted_keys=sorted(d)
	print(k1,sorted_keys)
	top_keys=0
	for key in sorted_keys:
		print(d[key])
		Big.append(key)
		top_keys = top_keys+1
		if(top_keys>4):
			break
		r = random.randint(1,4)
	print(Big)
	sampled_values=random.sample(Big,r)
	temp = {}
	for val in sampled_values:
		node = d[val]
		value = val
		temp[node] = value
		BigDict[k1]= temp

print(BigDict)

list1 = list(BigDict.keys())

print(list1)

counter = 0

for i in range(50):
	start_city = random.choice(list1)
	end_city = random.choice(list1)
	mnodes = []
	nvisited = []

	print(start_city)
	print(end_city)

	alreadyseen_city = []
	path_dict = {}

	current_city = None
	parent_city = None

	explored_city = []

	indexSG = list1.index(start_city)
	indexEG = list1.index(end_city)

	print(indexSG)
	print(indexEG)

	list1[indexSG]

	del list1[indexEG]
	print(list1)

	dicGS = {}
	for node in list1:
		dicGS[node] = random.choice(range(1,100)) # random.sample(range(1,50),1) [0] --> this can also be used
	print(dicGS)
	dicGS[end_city] = 0

	print("Start City ",start_city)
	print("End City ",end_city)


##.............A* SEARCH...............##


print("\n")
print("Implementing A* Search")

priority_queue = []
exploredGS = []
pathG = {}

priority_queue.append(start_city)

print(priority_queue) # this will print the start element

nested_Dict = BigDict[start_city]

while(len(priority_queue)!=0):
	current_node = priority_queue.pop(0)
	exploredGS.append(current_node)
		if(current_node==end_city):
			print("Solution Found")
			counter+=1
			mnodes.append(len(priority_queue))
			mnodes.append(len(exploredGS))
			nvisited.append(len(exploredGS))
			break
	nested = BigDict[current_node]
	print(nested)

	temp_dic = {}

	g_distance=0
	for key,value in nested.items():
		if(key in exploredGS or key in priority_queue):
			pass
		else:
			h_distance=dicGS[key]
			pathG[key] = current_node
			node=key
			while(node!=start_city):
				parent=pathG[node]
				g_distance=g_distance+BigDict[parent][node]
				node=parent
			distance=g_distance+h_distance
			temp_dic[distance] = key
	sorted(temp_dic)

	print(temp_dic)
	
	temp_arr = []
	for keys in sorted(temp_dic):
		temp_arr.append(temp_dic[keys])
	priority_queue = temp_arr + priority_queue
	print(priority_queue)
	print(pathG)

for i in range(len(mnodes)):
	maxnodes = maxnodes + mnodes[i]

for i in range(len(nvisited)):
	nodesvisited = nodesvisited + nvisited[i]

print("The maximum number of nodes generated ",maxnodes)

print("The number of nodes visited ",nodesvisited)

print("A* implemented for ",counter)

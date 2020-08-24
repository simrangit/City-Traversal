import math
import random
import string

# import networkx as nx
# import matplotlib.pyplot as plt

counter = 0
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
# u
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

##.............GREEDY SEARCH...............##


list1 = list(BigDict.keys())
print(list1)

start_city = random.choice(list1)
end_city = random.choice(list1)

mnodes = []
nvisited = []

indexSG = list1.index(start_city)
indexEG = list1.index(end_city)

print(indexSG)
print(indexEG)

del list1[indexSG]
del list1[indexEG]

print(list1)
dicGS = {}

for node in list1:
	dicGS[node] = random.choice(range(1,100)) # random.sample(range(1,100),1) [0] --> this can also be used

print(dicGS)
dicGS[end_city] = 0

print("Start City ",start_city)
print("End City ",end_city)

print(" Implementing GREEDY Best First Search")

# The code below is for Greedy Best First Search
##dicGS --> Contains the cities distance to the Final Destination
##BigDict --> Original nested dictionary

priority_queue = []
exploredGS = []

pathG = {}

priority_queue.append(start_city)
print(priority_queue)

nested_Dict = BigDict[start_city]
while(len(priority_queue)!=0):
	current_node = priority_queue.pop(0)
	parent_node = current_node

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
		for key,value in nested.items():
			if(key in exploredGS or key in priority_queue):
				pass
			else:
				temp_dic[dicGS[key]] = key
				pathG[key] = parent_node
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

print("Number of problems solved by Greedy Best First Search ",counter)



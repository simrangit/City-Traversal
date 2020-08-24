import math
import random
import string

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

start_city = random.choice(list1)
end_city = random.choice(list1)

alreadyseen_city = []
path_dict = {}

current_city = None
parent_city = None

explored_city = []


##..................DEPTH FIRST SEARCH............##
# Code for DFS is from 81 to 118 lines


print(" Implementing DFS")
print("Start City ",start_city)
print("End city ",end_city)

path_dict = {}
current_city = None
parent_city = None
explored_city = []
dfs_queue = []

dfs_queue.append(start_city)

while(len(dfs_queue)!=0):
	parent_city = current_city
	current_city = dfs_queue.pop(0)
	explored_city.append(current_city)
	path_dict[current_city] = parent_city
	if(current_city == end_city):
		print("Path is found by DEPTH FIRST SEARCH")
		break
	temp_array = []

	node_dictionary = BigDict[current_city]

	for key, value in node_dictionary.items():
		if(key in explored_city or key in dfs_queue):
			pass
		else:
			temp_array.append(key)
	temp_array = temp_array + dfs_queue

	dfs_queue = temp_array

	print("Explored Cities are "+str(explored_city))
	rint(" DFS Queue is",dfs_queue)


print(path_dict)
# City-Traversal

The problem at hand, consists of 26 cities named from A – Z, placed in a discrete two dimensional 100 X 100 grid. The objective is to reach a specified goal city from a specified start city only traversing through the paths that exist among the various cities ‘A’-‘Z’.

The following are the steps I followed to create the described situation (the initial phase) as expected in the assignment introduction.

1. I created a dictionary to store all the cities labeled ‘A’-‘Z’ in the places dictionary using a random function, for randomly assigning the coordinates to each city in a grid of 100X100.

2. Following the first step, for every city:

   a. For every city, Euclidean distance to every other city (25) was calculated using the coordinates of the Places dictionary which was created in the first step.
   b. A temporary dictionary was created with key as distances and value as cities and was sorted. Sorted dictionary was randomized in the range of 1-4.
   c. Following the (b) step, for every city, the randomized cities of first five sorted distances were added to the Big Dict with key as cities and value as distances.

This then created a nested dictionary which contains for every city, the key as cities – to which each city is connected to and the values as distances – a distance to each city for a particular city.

Refer BigDictionary.py

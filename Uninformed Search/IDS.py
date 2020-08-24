#returns true if target is reachable from start city within max_depth

Boolean IDS(start_city, end_city, max_depth)

for limit from 0 to max_depth
	if DLS(src, target, limit) == true
		return true
	return false

bool DLS(start_city,end_city, limit)

if (start_city ==end_city)
	return true;

#If reached the maximum depth,
# stop recursing.

if (limit <= 0)
	return false;

for each adjacent i of start_city
	if DLS(i, end_city, limit)
		return true
return false

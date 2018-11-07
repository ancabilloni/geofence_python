#!/usr/bin/env python

def orientation(p, q, r):
	val = (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1])

	if val == 0:
		return 0 # collinear
	elif val > 0:
		return 1
	else:
		return 2

def doIntersect(v1, v2, p1, p2):
	o1 = orientation(v1,v2,p1)
	o2 = orientation(v1,v2,p2)
	o3 = orientation(p1,p2,v1)
	o4 = orientation(p1,p2,v2)
	# print o1, o2, o3, o4

	# Only consider General case, ignore on collinear check
	if (o1 != o2) and (o3 != o4):
		return True
	return False

def isInside(polygon, point_p):
	n = len(polygon)
	if n < 3:
		return False # there must be at least 3 vertices in polygon

	point_extreme = [99999, point_p[1]]
	count_inter = 0
	i = 0
	while i < n:
		i_next = (i+1)%n
		if doIntersect(polygon[i], polygon[i_next], point_p, point_extreme):
			count_inter += 1
		i += 1
	return count_inter&1

if __name__ == '__main__':
	polygon = [[1,2], [2,4], [4,6], [8,5], [6,4], [4,3], [3,2]]
	point_p = [0,2]
	inGeofence = None
	if isInside(polygon, point_p):
		inGeofence = "Yes"
	else:
		inGeofence = "No"
	print "Is point {0} inside polygon? {1}".format(point_p, inGeofence)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
from matplotlib.colors import ListedColormap

def start(x0,y0,x1,y1):
	"""
	Starts the algorithm (...)
	
	Parameters
	-------------
	x0 : int
		x coordinate of first point
	y0 : int
		y coordinate of first point

	x1 : int
		x coordinate of second point
	y1 : int
		y coordinate of second point
	 """

	coord_x =[]
	coord_y =[]
	if abs(x1-x0) >= abs(y1-y0) :
		if x0>x1 :
			x0,y0,x1,y1 =swap(x0,y0,x1,y1)
		y = y0
		dy = (y1-y0)/(x1-x0)
		for x in range (x0,x1+1):
			print_point(x,round(y))
			coord_x.append(x)
			coord_y.append(int(round(y)))
			y += dy
	else :
		if y0>y1:
			x0,y0,x1,y1=swap(x0,y0,x1,y1)
		x=x0
		dx = (x1-x0)/(y1-y0)
		for y in range(y0,y1+1):
			print_point(round(x),y)
			coord_x.append(int(round(x)))
			coord_y.append(y)
			x +=dx
	plot_graph(coord_x,coord_y,"interpolation")


def swap(x0,y0,x1,y1):
	"""
	Swaps x0 with x1 and y0 with y1 
	"""
	temp_x1 = x1
	temp_y1 = y1
	x1 = x0
	y1 = y0
	x0 = temp_x1
	y0 = temp_y1
	return x0,y0,x1,y1

def print_point(x,y):
	print("({},{})".format(x,y))

def plot_graph(coord_x,coord_y,title):
	"""
	Graph plotting wiht matplotlib.
	To reduce the window size the maximum distance among
	the points is used to generated a square matrix.
	Coordinates are normalized to fit new represention.
	"""

	min_x,max_x = np.amin(coord_x),np.amax(coord_x)
	min_y,max_y = np.amin(coord_y),np.amax(coord_y)
	dx = (max_x-min_x)+1
	dy = (max_y-min_y)+1
	size = max(dx,dy)
	matrix = np.ones((size,size))
	coord_y_norm = [i-min_y for i in coord_y]
	coord_x_norm = [i-min_x for i in coord_x] 
	values = [coord_y_norm,coord_x_norm]
	matrix[values]= 0.
	col_labels = range(min_x,min_x+size)
	row_labels = range(min_y,min_y+size)
	
	cmap = ListedColormap(['r', 'w'])
	plt.matshow(matrix,cmap=cmap)
	plt.xticks(range(size), col_labels)
	plt.yticks(range(size), row_labels)
	plt.gca().set_xticks([x - 0.5 for x in plt.gca().get_xticks()][1:], minor='true')
	plt.gca().set_yticks([y - 0.5 for y in plt.gca().get_yticks()][1:], minor='true')
	plt.grid(which='minor')
	for x_val, y_val in zip(coord_x_norm, coord_y_norm):
		c = "("+str(x_val+min_x)+","+str(y_val+min_y)+")"
		plt.gca().text(x_val, y_val, c, va='center', ha='center',fontsize=round(50/size))
	plt.show()


start(int(sys.argv[1]) ,int(sys.argv[2]) ,int(sys.argv[3]) ,int(sys.argv[4]))


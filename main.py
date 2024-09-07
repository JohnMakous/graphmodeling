import matplotlib.pyplot as plt
import numpy as np
from pyweb import pydom
from pyscript import display

# Check if input value is a number. This enables blank input boxes in the html data table to be ignored.
def is_float(string):
	c= remove(string.replace(".", ""))   # 'remove' removes the whitespace in string
	if c.replace("-", "").isnumeric():
		return True
	else:
		return False

# Remove whitespace from string
def remove(string): 
	return string.replace(" ", "")

def update_graph(event):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 0
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max= float(x_max)
	else:
		x_max = 10

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 10

	if pydom["input#xlabel"][0].value != "":
		x_label = pydom["input#xlabel"][0].value
	else:
		x_label = "x"

	if pydom["input#ylabel"][0].value != "":
		y_label = pydom["input#ylabel"][0].value
	else:
		y_label = "y"

	if pydom["input#graphscale"][0].value != "":
		graph_scale = pydom["input#graphscale"][0].value
		graph_scale= float(graph_scale)
	else:
		graph_scale = 1.0
	
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value
	x5 = pydom["input#x5"][0].value
	x6 = pydom["input#x6"][0].value
	x7 = pydom["input#x7"][0].value
	x8 = pydom["input#x8"][0].value
	x9 = pydom["input#x9"][0].value
	x10 = pydom["input#x10"][0].value
	x11 = pydom["input#x11"][0].value
	x12 = pydom["input#x12"][0].value
	x13 = pydom["input#x13"][0].value
	x14 = pydom["input#x14"][0].value
	x15 = pydom["input#x15"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value
	y5 = pydom["input#y5"][0].value
	y6 = pydom["input#y6"][0].value
	y7 = pydom["input#y7"][0].value
	y8 = pydom["input#y8"][0].value
	y9 = pydom["input#y9"][0].value
	y10 = pydom["input#y10"][0].value
	y11 = pydom["input#y11"][0].value
	y12 = pydom["input#y12"][0].value
	y13 = pydom["input#y13"][0].value
	y14 = pydom["input#y14"][0].value
	y15 = pydom["input#y15"][0].value

	listx = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
	listy = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
	
	# Identify x input elements from data table that are numeric; store in an array
	x_list=[]
	i=0
	while (i<len(listx)):
		if is_float(listx[i])== False:
			i=i+1
		else:
			a = remove(listx[i])
			x_list.append(float(a))
			i=i+1

	# Identify y input elements from data table that are numeric; store in an array
	y_list=[]
	i=0
	while (i<len(listy)):
		if is_float(listy[i])== False:
			i=i+1
		else:
			a = remove(listy[i])
			y_list.append(float(a))
			i=i+1
	
	#store float values from data table lists into arrays
	xfloat = np.array(x_list)
	yfloat = np.array(y_list)
	
	#xfloat = x		# [float(i) for i in x]
	#yfloat = y		# [float(i) for i in y]

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(graph_scale*3.8,3.8))
	ax1.scatter(xfloat,yfloat, 15, color = 'black', zorder=2)
	# fig.suptitle(graph_note, fontsize=6)
	ax1.set_xlabel(x_label, fontsize=8, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=8, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=6)
	ax1.tick_params(axis='y', labelsize=6)
	ax1.margins(1)
	ax1.grid(linewidth=0.4, zorder=1)
	fig1.suptitle(y_label + " vs. "+ x_label, fontsize=8)

	plt.close('all')
	
	display(fig1, target='graph', append=False)

def linear_model(event):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 0
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max = float(x_max)
	else:
		x_max = 10

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 10

	if pydom["input#xlabel"][0].value != "":
		x_label = pydom["input#xlabel"][0].value
	else:
		x_label = "x"

	if pydom["input#ylabel"][0].value != "":
		y_label = pydom["input#ylabel"][0].value
	else:
		y_label = "y"

	if pydom["input#graphscale"][0].value != "":
		graph_scale = pydom["input#graphscale"][0].value
		graph_scale= float(graph_scale)
	else:
		graph_scale = 1.0
	
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value
	x5 = pydom["input#x5"][0].value
	x6 = pydom["input#x6"][0].value
	x7 = pydom["input#x7"][0].value
	x8 = pydom["input#x8"][0].value
	x9 = pydom["input#x9"][0].value
	x10 = pydom["input#x10"][0].value
	x11 = pydom["input#x11"][0].value
	x12 = pydom["input#x12"][0].value
	x13 = pydom["input#x13"][0].value
	x14 = pydom["input#x14"][0].value
	x15 = pydom["input#x15"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value
	y5 = pydom["input#y5"][0].value
	y6 = pydom["input#y6"][0].value
	y7 = pydom["input#y7"][0].value
	y8 = pydom["input#y8"][0].value
	y9 = pydom["input#y9"][0].value
	y10 = pydom["input#y10"][0].value
	y11 = pydom["input#y11"][0].value
	y12 = pydom["input#y12"][0].value
	y13 = pydom["input#y13"][0].value
	y14 = pydom["input#y14"][0].value
	y15 = pydom["input#y15"][0].value

	listx = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
	listy = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
	
	# Identify x input elements from data table that are numeric; store in an array
	x_list=[]
	i=0
	while (i<len(listx)):
		if is_float(listx[i])== False:
			i=i+1
		else:
			a = remove(listx[i])
			x_list.append(float(a))
			i=i+1

	# Identify y input elements from data table that are numeric; store in an array
	y_list=[]
	i=0
	while (i<len(listy)):
		if is_float(listy[i])== False:
			i=i+1
		else:
			a = remove(listy[i])
			y_list.append(float(a))
			i=i+1
	
	#store float values from data table into arrays
	xfloat = np.array(x_list)
	yfloat = np.array(y_list)

	if pydom["input#lin_c0"][0].value != "":
		c0 = pydom["input#lin_c0"][0].value
		c0 = float(c0)
	else:
		c0 = 0
	
	if pydom["input#lin_c1"][0].value != "":
		c1 = pydom["input#lin_c1"][0].value
		c1 = float(c1)
	else:
		c1 = 0

	c0float=float(c0)
	c1float=float(c1)
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(graph_scale*3.8,3.8))
	ax1.scatter(xfloat,yfloat, 15, color = 'black', zorder=2)
	plt.plot(x_model, y_model, linewidth=1.0)
	ax1.set_xlabel(x_label, fontsize=8, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=8, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=6)
	ax1.tick_params(axis='y', labelsize=6)
	ax1.margins(1)
	ax1.grid(linewidth=0.4, zorder=1)
	# place a text box in upper middle in axes coords
	textstr1 = "Math Model: " + r'$y = %.3f x + %.3f$' % (c1float, c0float)
	plt.title(textstr1, fontsize=7)
	fig1.suptitle(y_label + " vs. "+ x_label, fontsize=8)
	# props = dict(boxstyle='square', facecolor='wheat', alpha=0.5)
	# ax1.text(0.1, 0.95, textstr1, transform=ax1.transAxes, fontsize=6,
	#     	verticalalignment='top', bbox=props)

	plt.close('all')
	display(fig1, target='graph', append=False)

def quadratic_model(event):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 0
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max = float(x_max)
	else:
		x_max = 10

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 10

	if pydom["input#xlabel"][0].value != "":
		x_label = pydom["input#xlabel"][0].value
	else:
		x_label = "x"

	if pydom["input#ylabel"][0].value != "":
		y_label = pydom["input#ylabel"][0].value
	else:
		y_label = "y"

	if pydom["input#graphscale"][0].value != "":
		graph_scale = pydom["input#graphscale"][0].value
		graph_scale= float(graph_scale)
	else:
		graph_scale = 1.0
	
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value
	x5 = pydom["input#x5"][0].value
	x6 = pydom["input#x6"][0].value
	x7 = pydom["input#x7"][0].value
	x8 = pydom["input#x8"][0].value
	x9 = pydom["input#x9"][0].value
	x10 = pydom["input#x10"][0].value
	x11 = pydom["input#x11"][0].value
	x12 = pydom["input#x12"][0].value
	x13 = pydom["input#x13"][0].value
	x14 = pydom["input#x14"][0].value
	x15 = pydom["input#x15"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value
	y5 = pydom["input#y5"][0].value
	y6 = pydom["input#y6"][0].value
	y7 = pydom["input#y7"][0].value
	y8 = pydom["input#y8"][0].value
	y9 = pydom["input#y9"][0].value
	y10 = pydom["input#y10"][0].value
	y11 = pydom["input#y11"][0].value
	y12 = pydom["input#y12"][0].value
	y13 = pydom["input#y13"][0].value
	y14 = pydom["input#y14"][0].value
	y15 = pydom["input#y15"][0].value

	listx = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
	listy = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
	
	# Identify x input elements from data table that are numeric; store in an array
	x_list=[]
	i=0
	while (i<len(listx)):
		if is_float(listx[i])== False:
			i=i+1
		else:
			a = remove(listx[i])
			x_list.append(float(a))
			i=i+1

	# Identify y input elements from data table that are numeric; store in an array
	y_list=[]
	i=0
	while (i<len(listy)):
		if is_float(listy[i])== False:
			i=i+1
		else:
			a = remove(listy[i])
			y_list.append(float(a))
			i=i+1
	
	#store float values from data table into arrays
	xfloat = np.array(x_list)
	yfloat = np.array(y_list)

	if pydom["input#q0"][0].value != "":
		c0 = pydom["input#q0"][0].value
	else:
		c0 = 0
	
	if pydom["input#q1"][0].value != "":
		c1 = pydom["input#q1"][0].value
	else:
		c1 = 0

	if pydom["input#q2"][0].value != "":
		c2 = pydom["input#q2"][0].value
	else:
		c2 = 0
		
	c0float=float(c0)
	c1float=float(c1)
	c2float=float(c2)
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c2float*x_model*x_model + c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(graph_scale*3.8,3.8))
	ax1.scatter(xfloat,yfloat, 15, color = 'black', zorder=2)
	plt.plot(x_model, y_model, linewidth=1.0)
	ax1.set_xlabel(x_label, fontsize=8, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=8, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=6)
	ax1.tick_params(axis='y', labelsize=6)
	ax1.margins(1)
	ax1.grid(linewidth=0.4, zorder=1)

	# place a text box in upper middle in axes coords
	textstr1 = "Math Model: " +r'$y = %.3f x^{2} + %.3f x + %.3f$' % (c2float, c1float, c0float)
	plt.title(textstr1, fontsize=7)
	fig1.suptitle(y_label + " vs. "+ x_label, fontsize=8)
	# props = dict(boxstyle='square', facecolor='wheat', alpha=0.5)
	# ax1.text(0.1, 0.95, textstr1, transform=ax1.transAxes, fontsize=6,
	#     	verticalalignment='top', bbox=props)

	plt.close('all')
	display(fig1, target='graph', append=False)

def inverse_model(event):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 0
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max = float(x_max)
	else:
		x_max = 10

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 10

	if pydom["input#xlabel"][0].value != "":
		x_label = pydom["input#xlabel"][0].value
	else:
		x_label = "x"

	if pydom["input#ylabel"][0].value != "":
		y_label = pydom["input#ylabel"][0].value
	else:
		y_label = "y"

	if pydom["input#graphscale"][0].value != "":
		graph_scale = pydom["input#graphscale"][0].value
		graph_scale= float(graph_scale)
	else:
		graph_scale = 1.0
	
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value
	x5 = pydom["input#x5"][0].value
	x6 = pydom["input#x6"][0].value
	x7 = pydom["input#x7"][0].value
	x8 = pydom["input#x8"][0].value
	x9 = pydom["input#x9"][0].value
	x10 = pydom["input#x10"][0].value
	x11 = pydom["input#x11"][0].value
	x12 = pydom["input#x12"][0].value
	x13 = pydom["input#x13"][0].value
	x14 = pydom["input#x14"][0].value
	x15 = pydom["input#x15"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value
	y5 = pydom["input#y5"][0].value
	y6 = pydom["input#y6"][0].value
	y7 = pydom["input#y7"][0].value
	y8 = pydom["input#y8"][0].value
	y9 = pydom["input#y9"][0].value
	y10 = pydom["input#y10"][0].value
	y11 = pydom["input#y11"][0].value
	y12 = pydom["input#y12"][0].value
	y13 = pydom["input#y13"][0].value
	y14 = pydom["input#y14"][0].value
	y15 = pydom["input#y15"][0].value

	listx = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
	listy = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
	
	# Identify x input elements from data table that are numeric; store in an array
	x_list=[]
	i=0
	while (i<len(listx)):
		if is_float(listx[i])== False:
			i=i+1
		else:
			a = remove(listx[i])
			x_list.append(float(a))
			i=i+1

	# Identify y input elements from data table that are numeric; store in an array
	y_list=[]
	i=0
	while (i<len(listy)):
		if is_float(listy[i])== False:
			i=i+1
		else:
			a = remove(listy[i])
			y_list.append(float(a))
			i=i+1
	
	#store float values from data table into arrays
	xfloat = np.array(x_list)
	yfloat = np.array(y_list)
	
	if pydom["input#ic"][0].value != "":
		c0 = pydom["input#ic"][0].value
		c0 = float(c0)
	else:
		c0 = 0

	c0float=float(c0)
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c0float/x_model

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(graph_scale*3.8,3.8))
	ax1.scatter(xfloat,yfloat, 15, color = 'black', zorder=2)
	plt.plot(x_model, y_model, linewidth=1.0)
	ax1.set_xlabel(x_label, fontsize=8, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=8, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=6)
	ax1.tick_params(axis='y', labelsize=6)
	ax1.margins(1)
	ax1.grid(linewidth=0.4, zorder=1)

	# place a text box in upper middle in axes coords
	textstr1 = "Math Model: " +r'$y = %.3f/x $' % (c0float)
	plt.title(textstr1, fontsize=7)
	fig1.suptitle(y_label + " vs. "+ x_label, fontsize=8)
	# props = dict(boxstyle='square', facecolor='wheat', alpha=0.5)
	# ax1.text(0.1, 0.95, textstr1, transform=ax1.transAxes, fontsize=6,
	#     	verticalalignment='top', bbox=props)

	plt.close('all')
	display(fig1, target='graph', append=False)

def sqrt_model(event):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 0
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max= float(x_max)
	else:
		x_max = 10

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 10

	if pydom["input#xlabel"][0].value != "":
		x_label = pydom["input#xlabel"][0].value
	else:
		x_label = "x"

	if pydom["input#ylabel"][0].value != "":
		y_label = pydom["input#ylabel"][0].value
	else:
		y_label = "y"
	
	if pydom["input#graphscale"][0].value != "":
		graph_scale = pydom["input#graphscale"][0].value
		graph_scale= float(graph_scale)
	else:
		graph_scale = 1.0

	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value
	x5 = pydom["input#x5"][0].value
	x6 = pydom["input#x6"][0].value
	x7 = pydom["input#x7"][0].value
	x8 = pydom["input#x8"][0].value
	x9 = pydom["input#x9"][0].value
	x10 = pydom["input#x10"][0].value
	x11 = pydom["input#x11"][0].value
	x12 = pydom["input#x12"][0].value
	x13 = pydom["input#x13"][0].value
	x14 = pydom["input#x14"][0].value
	x15 = pydom["input#x15"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value
	y5 = pydom["input#y5"][0].value
	y6 = pydom["input#y6"][0].value
	y7 = pydom["input#y7"][0].value
	y8 = pydom["input#y8"][0].value
	y9 = pydom["input#y9"][0].value
	y10 = pydom["input#y10"][0].value
	y11 = pydom["input#y11"][0].value
	y12 = pydom["input#y12"][0].value
	y13 = pydom["input#y13"][0].value
	y14 = pydom["input#y14"][0].value
	y15 = pydom["input#y15"][0].value

	listx = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
	listy = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
	
	# Identify x input elements from data table that are numeric; store in an array
	x_list=[]
	i=0
	while (i<len(listx)):
		if is_float(listx[i])== False:
			i=i+1
		else:
			a = remove(listx[i])
			x_list.append(float(a))
			i=i+1

	# Identify y input elements from data table that are numeric; store in an array
	y_list=[]
	i=0
	while (i<len(listy)):
		if is_float(listy[i])== False:
			i=i+1
		else:
			a = remove(listy[i])
			y_list.append(float(a))
			i=i+1
	
	#store float values from data table into arrays
	xfloat = np.array(x_list)
	yfloat = np.array(y_list)
	
	if pydom["input#sqrt_c0"][0].value != "":
		c0 = pydom["input#sqrt_c0"][0].value
		c0 = float(c0)
	else:
		c0 = 0
	
	if pydom["input#sqrt_c1"][0].value != "":
		c1 = pydom["input#sqrt_c1"][0].value
		c1 = float(c1)
	else:
		c1 = 0
	
	c0float=float(c0)
	c1float=float(c1)
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c1float*np.sqrt(x_model) + c0float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(graph_scale*3.8,3.8))
	ax1.scatter(xfloat,yfloat, 15, color = 'black', zorder=2)
	plt.plot(x_model, y_model, linewidth=1.0)
	ax1.set_xlabel(x_label, fontsize=8, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=8, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=6)
	ax1.tick_params(axis='y', labelsize=6)
	ax1.margins(1)
	ax1.grid(linewidth=0.4, zorder=1)

	# place a text box in upper middle in axes coords
	textstr1 = "Math Model: " +r'$y = %.3f \sqrt{x} + %.3f$' % (c1float, c0float)
	plt.title(textstr1, fontsize=7)
	fig1.suptitle(y_label + " vs. "+ x_label, fontsize=8)
	# props = dict(boxstyle='square', facecolor='wheat', alpha=0.5)
	# ax1.text(0.1, 0.95, textstr1, transform=ax1.transAxes, fontsize=6,
	#     	verticalalignment='top', bbox=props)

	plt.close('all')
	display(fig1, target='graph', append=False)

def power_model(event):
	if pydom["input#xmin"][0].value != "":
		x_min = pydom["input#xmin"][0].value
		x_min = float(x_min)
	else:
		x_min = 0
	
	if pydom["input#xmax"][0].value != "":
		x_max = pydom["input#xmax"][0].value
		x_max = float(x_max)
	else:
		x_max = 10

	if pydom["input#ymin"][0].value != "":
		y_min = pydom["input#ymin"][0].value
		y_min = float(y_min)
	else:
		y_min = 0
	
	if pydom["input#ymax"][0].value != "":
		y_max = pydom["input#ymax"][0].value
		y_max= float(y_max)
	else:
		y_max = 10

	if pydom["input#xlabel"][0].value != "":
		x_label = pydom["input#xlabel"][0].value
	else:
		x_label = "x"

	if pydom["input#ylabel"][0].value != "":
		y_label = pydom["input#ylabel"][0].value
	else:
		y_label = "y"
	
	if pydom["input#graphscale"][0].value != "":
		graph_scale = pydom["input#graphscale"][0].value
		graph_scale= float(graph_scale)
	else:
		graph_scale = 1.0
	
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value
	x5 = pydom["input#x5"][0].value
	x6 = pydom["input#x6"][0].value
	x7 = pydom["input#x7"][0].value
	x8 = pydom["input#x8"][0].value
	x9 = pydom["input#x9"][0].value
	x10 = pydom["input#x10"][0].value
	x11 = pydom["input#x11"][0].value
	x12 = pydom["input#x12"][0].value
	x13 = pydom["input#x13"][0].value
	x14 = pydom["input#x14"][0].value
	x15 = pydom["input#x15"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value
	y5 = pydom["input#y5"][0].value
	y6 = pydom["input#y6"][0].value
	y7 = pydom["input#y7"][0].value
	y8 = pydom["input#y8"][0].value
	y9 = pydom["input#y9"][0].value
	y10 = pydom["input#y10"][0].value
	y11 = pydom["input#y11"][0].value
	y12 = pydom["input#y12"][0].value
	y13 = pydom["input#y13"][0].value
	y14 = pydom["input#y14"][0].value
	y15 = pydom["input#y15"][0].value

	listx = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15]
	listy = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
	
	# Identify x input elements from data table that are numeric; store in an array
	x_list=[]
	i=0
	while (i<len(listx)):
		if is_float(listx[i])== False:
			i=i+1
		else:
			a = remove(listx[i])
			x_list.append(float(a))
			i=i+1

	# Identify y input elements from data table that are numeric; store in an array
	y_list=[]
	i=0
	while (i<len(listy)):
		if is_float(listy[i])== False:
			i=i+1
		else:
			a = remove(listy[i])
			y_list.append(float(a))
			i=i+1
	
	#store float values from data table lists into arrays
	xfloat = np.array(x_list)
	yfloat = np.array(y_list)
	
	if pydom["input#powerc"][0].value != "":
		c0 = pydom["input#powerc"][0].value
	else:
		c0 = 0

	if pydom["input#powern"][0].value != "":
		power_n = pydom["input#powern"][0].value
	else:
		power_n = 0

	if pydom["input#powerb"][0].value != "":
		power_b = pydom["input#powerb"][0].value
	else:
		power_b = 0

	c0float=float(c0)
	power_n_float = float(power_n)
	power_b_float = float(power_b)
	
	x_model = np.arange(0.0,x_max,.001)
	y_model = c0float*x_model**power_n_float + power_b_float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(graph_scale*3.8,3.8))
	ax1.scatter(xfloat,yfloat, 15, color = 'black', zorder=2)
	plt.plot(x_model, y_model, linewidth=1.0)
	ax1.set_xlabel(x_label, fontsize=8, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=8, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=6)
	ax1.tick_params(axis='y', labelsize=6)
	ax1.margins(1)
	ax1.grid(linewidth=0.4, zorder=1)

	# place a text box in upper middle in axes coords
	textstr1 = "Math Model: " +r'$y = %.3f x^{%.3f} + %.3f$' % (c0float, power_n_float, power_b_float)
	plt.title(textstr1, fontsize=7)
	fig1.suptitle(y_label + " vs. "+ x_label, fontsize=8)
	# props = dict(boxstyle='square', facecolor='wheat', alpha=0.5)
	# ax1.text(0.1, 0.95, textstr1, transform=ax1.transAxes, fontsize=6,
	#     	verticalalignment='top', bbox=props)

	plt.close('all')
	display(fig1, target='graph', append=False)


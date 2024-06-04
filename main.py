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

	x_label = pydom["input#xlabel"][0].value
	y_label = pydom["input#ylabel"][0].value
	
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

	listx = [x1,x2,x3,x4]
	listy = [y1,y2,y3,y4]
	
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
	x = np.array(x_list)
	y = np.array(y_list)
	
	xfloat = x		# [float(i) for i in x]
	yfloat = y		# [float(i) for i in y]

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(3,2.5))
	ax1.scatter(xfloat,yfloat, 10)
	plt.title(y_label + " vs. "+ x_label, fontsize=6)
	#plt.xlabel(x_label, fontsize=6)  
	#plt.ylabel(y_label, fontsize=6)
	ax1.set_xlabel(x_label, fontsize=6, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	ax1.margins(1)
	ax1.grid()

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

	x_label = pydom["input#xlabel"][0].value
	y_label = pydom["input#ylabel"][0].value
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

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
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(3,2.5))
	ax1.scatter(xfloat,yfloat, 10)
	plt.plot(x_model, y_model)
	plt.title(y_label + " vs. "+ x_label, fontsize=6)
	ax1.set_xlabel(x_label, fontsize=6, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	ax1.margins(1)
	ax1.grid()

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
	
	x_label = pydom["input#xlabel"][0].value
	y_label = pydom["input#ylabel"][0].value
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

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
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c2float*x_model*x_model + c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(3,2.5))
	ax1.scatter(xfloat,yfloat, 10)
	plt.plot(x_model, y_model)
	plt.title(y_label + " vs. "+ x_label, fontsize=6)
	ax1.set_xlabel(x_label, fontsize=6, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	ax1.margins(1)
	ax1.grid()

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
	
	x_label = pydom["input#xlabel"][0].value
	y_label = pydom["input#ylabel"][0].value
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

	if pydom["input#ic"][0].value != "":
		c0 = pydom["input#ic"][0].value
		c0 = float(c0)
	else:
		c0 = 0

	c0float=float(c0)
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c0float/x_model

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(3,2.5))
	ax1.scatter(xfloat,yfloat, 10)
	plt.plot(x_model, y_model)
	plt.title(y_label + " vs. "+ x_label, fontsize=6)
	ax1.set_xlabel(x_label, fontsize=6, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	ax1.margins(1)
	ax1.grid()

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

	x_label = pydom["input#xlabel"][0].value
	y_label = pydom["input#ylabel"][0].value
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

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
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c1float*np.sqrt(x_model) + c0float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(3,2.5))
	ax1.scatter(xfloat,yfloat, 10)
	plt.plot(x_model, y_model)
	plt.title(y_label + " vs. "+ x_label, fontsize=6)
	ax1.set_xlabel(x_label, fontsize=6, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	ax1.margins(1)
	ax1.grid()

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
	
	x_label = pydom["input#xlabel"][0].value
	y_label = pydom["input#ylabel"][0].value
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

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
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
		
	x_model = np.arange(0.0,x_max,.001)
	y_model = c0float*x_model**power_n_float + power_b_float

	fig1, ax1 = plt.subplots(1, dpi=150, figsize=(3,2.5))
	ax1.scatter(xfloat,yfloat, 10)
	plt.plot(x_model, y_model)
	plt.title(y_label + " vs. "+ x_label, fontsize=6)
	ax1.set_xlabel(x_label, fontsize=6, labelpad=1)
	ax1.set_ylabel(y_label, fontsize=6, labelpad=1)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.tick_params(axis='x', labelsize=4)
	ax1.tick_params(axis='y', labelsize=4)
	ax1.margins(1)
	ax1.grid()

	plt.close('all')
	display(fig1, target='graph', append=False)


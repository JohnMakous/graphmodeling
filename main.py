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

	fig1 = plt.figure(1,dpi=150, figsize=(4,2.5))
	ax1 = plt.add_subplot()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data")   #fontsize=6
	ax1.set_xlabel(x_label, fontsize=6)  
	ax1.set_ylabel(y_label)  #fontsize=6
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.margins(y=0)
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

	c0 = pydom["input#lin_c0"][0].value
	c1 = pydom["input#lin_c1"][0].value
	c0float=float(c0)
	c1float=float(c1)
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
		
	x_model = np.arange(0.0,x_max,.01)
	y_model = c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(5,3))
	#fig1, ax1 = plt.subplots()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.margins(y=0)
	ax1.grid()

	plt.close('all')
	display(fig1, target='graph', append=False)

def parabola_model(event):
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

	c0 = pydom["input#p0"][0].value
	c1 = pydom["input#p1"][0].value
	c2 = pydom["input#p2"][0].value
	c0float=float(c0)
	c1float=float(c1)
	c2float=float(c2)
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
		
	x_model = np.arange(0.0,x_max,.01)
	y_model = c2float*x_model*x_model + c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(5,3))
	#fig1, ax1 = plt.subplots()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_xlim(x_min, x_max)
	ax1.set_ylim(y_min, y_max)
	ax1.margins(y=0)
	ax1.grid()

	plt.close('all')
	display(fig1, target='graph', append=False)

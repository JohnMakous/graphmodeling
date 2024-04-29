import matplotlib.pyplot as plt
import numpy as np
from pyweb import pydom
from pyscript import display

def update_graph(event):
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]

	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(4,3))
	fig1, ax1 = plt.subplots()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	ax1.set_xlim(0, 20)
	ax1.set_ylim(0,30)
	ax1.margins(y=0)
	ax1.grid()
	
	display(fig1, target='graph', append=False)

def linear_model(event):
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
		
	x_model = np.arange(0.0,20.0,.01)
	y_model = c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(5,3))
	fig1, ax1 = plt.subplots()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_xlim(0, 20)
	ax1.set_ylim(0,30)
	ax1.margins(y=0)
	ax1.grid()
	
	display(fig1, target='graph', append=False)

def parabola_model(event):
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
		
	x_model = np.arange(0.0,20.0,.01)
	y_model = c2float*x_model*x_model + c1float*x_model + c0float

	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(5,3))
	fig1, ax1 = plt.subplots()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_xlim(0, 20)
	ax1.set_ylim(0,30)
	ax1.margins(y=0)
	ax1.grid()
	
	display(fig1, target='graph', append=False)

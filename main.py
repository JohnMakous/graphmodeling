import matplotlib.pyplot as plt
import numpy as np
from pyweb import pydom
from pyscript import display
c1=1
def update_graph(event):
	x1 = pydom["input#x1"][0].value
	x2 = pydom["input#x2"][0].value
	x3 = pydom["input#x3"][0].value
	x4 = pydom["input#x4"][0].value

	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

	c1 = pydom["input#c1"][0].value
	c1float=float(c1)
	
	x = np.array([x1,x2,x3,x4])
	y = np.array([y1,y2,y3,y4])
	
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
	
	x_model = np.arange(0.0,50.0,.01)
	y_model = c1float*x_model*x_model

	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(5,3))
	fig1, ax1 = plt.subplots()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_ylim(0,50)
	ax1.margins(y=0)
	ax1.grid()
	
	display(fig1, target='graph', append=False)

def update_model(event):
	c1 = pydom["input#c1"][0].value
	c1float=float(c1)
		
	x_model = np.arange(0.0,50.0,.01)
	y_model = c1float*x_model*x_model

	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(5,3))
	fig1, ax1 = plt.subplots()
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_ylim(0,50)
	ax1.margins(y=0)
	ax1.grid()
	
	display(fig1, target='graph', append=False)


import os
import numpy as np
import cv2
from pathlib import Path
import time

def linearize(Color):
	L = 0
	if Color<0.0405:
		L = Color/12.92
	else:
		L =((Color+0.055)/1.055)**2.4
	if L>1:
		L = 1
	if L<0:
		L = 0
	return L
	
def perceived(L):
	if L<(216/24389):
		return L*(24389/27)
	else:
		return L**(1/3)*116-16
		
def getLstar(dataR,dataG,dataB):
	
	vR = np.double( dataR/255.)
	vG = np.double( dataG/255.)
	vB = np.double( dataB/255.)
	
	#todo: may have to apply gamma correction
	norm = np.ones(vR.shape)
	#vlin = np.vectorize(linearize)
	#Rlin = vlin(vR)
	#Glin = vlin(vG)
	#Blin = vlin(vB)
	Rlin=(norm-vR)//(1-0.04045)*vR/12.92+((vR/0.04045)**0.00000001*100000//100000)*(((vR+0.055)/1.055)**2.4)
	Glin=(norm-vG)//(1-0.04045)*vG/12.92+((vG/0.04045)**0.00000001*100000//100000)*(((vG+0.055)/1.055)**2.4)
	Blin=(norm-vB)//(1-0.04045)*vB/12.92+((vB/0.04045)**0.00000001*100000//100000)*(((vB+0.055)/1.055)**2.4)
	L =Rlin*0.2126+Glin*0.7152+Blin*0.0722
	vperc = np.vectorize(perceived)
	Lstar = vperc(L)
	
	#Lstar = ((norm-L)//(1-216/24389))*L*903.3+((L//(216/24389))**0.000001)*(L**(1/3)*116-16)
	return L,Lstar


def preprocess():
	folder = 'images'

	# We get all the image files from the source folder
	files = list([os.path.join(folder, f) for f in os.listdir(folder)])
	# We compute the average by adding up the images
	# Start from an explicitly set as floating point, in order to force the
	# conversion of the 8-bit values from the images, which would otherwise overflow
	os.makedirs(os.path.dirname("out/"),exist_ok = True)
	for file in files[:]:
		name = Path(file).stem
		image = cv2.imread(file)
		#print("size:",image.shape)
		imgshape = image.shape
		imgR = np.zeros(imgshape)
		imgG = np.zeros(imgshape)
		imgB = np.zeros(imgshape)
		imgBright = np.zeros(imgshape)
		#extract RGB, R=2,G=1,B=0
		dataR = image[:,:,2]
		dataG = image[:,:,1]
		dataB = image[:,:,0]
		dataGray =  (image[:,:,0]/3+ image[:,:,1]/3+ image[:,:,2]/3)
		dataBright = (0.114*image[:,:,0]+0.587* image[:,:,1]+ 0.299*image[:,:,2])

		imgR[:,:,2] = image[:,:,2]
		imgG[:,:,1] = image[:,:,1]
		imgB[:,:,0] = image[:,:,0]
		cv2.imwrite("out/"+name+'_R.png', imgR)
		cv2.imwrite("out/"+name+'_G.png', imgG)
		cv2.imwrite("out/"+name+'_B.png', imgB)
		cv2.imwrite("out/"+name+'_gray.png',dataGray)
		
		L,Lstar = getLstar(dataR,dataG,dataB)
		cv2.imwrite("out/"+name+'_br1.png',L*255)
		cv2.imwrite("out/"+name+'_br2.png',Lstar/100*255)
t0 = time.clock()

preprocess()

print("finished, processed",time.clock()-t0,"seconds")
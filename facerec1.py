import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
fc= cv2.CascadeClassifier("C:/Users/Om/Desktop/javanerd/haarcascade_frontalface_default.xml")

def fae(img,s2,f):
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faer=fc.detectMultiScale(gray,1.3,5)
	if faer is():
		return img,[]
	for(x,y,w,h) in faer:
		if f==1:
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,s2,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
			r=img[y:y+h,x:x+w]
			r=cv2.resize(r,(200,200))
			return img,r
		else :
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"Unknown",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
			r=img[y:y+h,x:x+w]
			r=cv2.resize(r,(200,200))
			return img,r
			

def call2(s2):
	dat="C:/Users/Om/Desktop/Face recognition/face/"
	f=0
	yu=[f for f in listdir(dat) if isfile(join(dat,f))]

	dt,rt=[],[]

	for i,gtt in enumerate(yu):
		imp=dat+yu[i]
		impr=cv2.imread(imp,cv2.IMREAD_GRAYSCALE)
		dt.append(np.asarray(impr, dtype=np.uint8))
		rt.append(i)
	rt =np.asarray(rt,dtype=np.int32)
	model=cv2.face.LBPHFaceRecognizer_create()
	model.train(np.asarray(dt),np.asarray(rt))
	
	
	cap=cv2.VideoCapture(0)
	while True:
		ret,fframe=cap.read()
		image,face=fae(fframe,s2,f)
		
		try:
			face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
			resu=model.predict(face)
			#print(type(resu),resu)
	
			if resu[1] < 500:
				co=int(100*(1-resu[1]/300))
				#d=str(co)+'% Confidence it is user'		
			#cv2.putText(image,d,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),4)
	
			if co > 75:
				cv2.putText(image,"Unlocked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(10,255,0),2)
				cv2.imshow("Face recogniation",image)
				f=1
	
			else :
				cv2.putText(image,"locked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
				cv2.imshow("Face recogniation",image)
				f=0
				
		except:
				cv2.putText(image,"Face not found",(230,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,250,255),2)
				cv2.imshow("Face recogniation",image)
				pass
	
		if cv2.waitKey(1)==13:
			break
	cap.release()
	cv2.destroyAllWindows()
	
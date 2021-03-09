import cv2

fc= cv2.CascadeClassifier("C:/Users/Om/Desktop/Face recognition - Copy/haarcascade_frontalface_default.xml")


def facee(frame):

	gay=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	fra=fc.detectMultiScale(gay,1.3,5)
	
	if fra is():
		return None

	for(x,y,w,h) in fra:
		cro=frame[y:y+h+50,x:x+w+50]
		cv2.rectangle(cro,(x,y),(w+x,y+h),(255,0,0),3)
		
	return cro
def call():
	cp=cv2.VideoCapture(0)
	coun=0

	while True:
		_, Fte=cp.read()
		fac=None
		if facee(Fte) is not None:
			coun+=1
			fac=cv2.resize(facee(Fte),(400,400))
			fac=cv2.cvtColor(fac,cv2.COLOR_BGR2GRAY)

			filen="C:/Users/Om/Desktop/Face recognition/face/"+"fa"+str(coun)+'.jpg'
			cv2.imwrite(filen,fac)

			cv2.putText(fac,str(coun),(346,400),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
			cv2.imshow("Sample",fac)
		
		else:
			print("Face not found")
			pass
		

		if cv2.waitKey(1)==13 or coun==100:
			break

	cp.release()
	cv2.destroyAllWindows()
	
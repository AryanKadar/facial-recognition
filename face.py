import tkinter as tt
import facerec as er
import facerec1 as ass
def her():
	#er.call()
	#l2 = tt.Label(r, text = "Model Complete")
	#l2.place(x=50,y=200)
	ass.call2(e.get())

def her1():
	er.call()
	l2 = tt.Label(r, text = "Model Complete")
	l2.place(x=50,y=200)
	
r=tt.Tk()
r.title("Face Recognition")
frame=tt.Frame(r,width=400,height=300)
frame.pack()
l1 = tt.Label(r, text = "Enter Name")
l1.place(x=50,y=70)
e=tt.Entry(r,bd=4)
e.place(x=180,y=70)

B = tt.Button(r, text =" UNLOCK ",width=6,height=1,command=her)
B.place(x=320,y=200)
B2=tt.Button(r,text=" FACE ",width=6,height=1,command=her1)
B2.place(x=240,y=200)

tt.mainloop()

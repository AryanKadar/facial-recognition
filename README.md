# facial-recognition
Facial recognition using python

Description__:
            @As we all know facial recognition has become a part of our life that has been include in every smart phone has basic requirement as to recognize the user of that product.
            @I have made my own alogorithm that take 100 sample face image from webcam that convert normal image into gray scale(black and white image,that make process easy)and store that image in specific folder and then take those sample image to train the mode using LBPHFaceRecognizer_create() to train those model that has predict method that return tuple that has value that convertrd into percentage that is use to detect face that is store is same face that is input from webcam has confidence number.
            @If the value is below 75 then that person is recognize by program and display "Unlocked" with rectangle around face with name that has been input at start or it is rejected by program for unknown face.
            @Also if the value of prediction is beyond 500 (That i have consider has standard value for face not found case) program will simple put text has "face not found".
            
            
How__to__excecute:
                1.First you have to save all file in one folder then you have to give path of "haarcascade_frontalface_default" in line 3 of facerec and line 5 of facerec1.
                3.Then create face folder in same folder or anywhere you like and give path of folder "face" in line 31 in facerec.Path must be of folder face in your system.
                5.Then execute it by typing "python face.py" in your environment it will execute and you will see a ui that has entry with label as name and with two button.
                6.Enter your name in that entry then click "face" button and you will see label appear as  "model complete"  then click "unlock" button and you will see your face has been recognize with rectangle draw on face and name that you have input in entry on top-left corner of rectangle.
            

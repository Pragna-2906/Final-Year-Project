import cv2
import os
import yaml

# distance from camera to object(face) measured
# centimeter
Known_distance = 76.2
  
# width of face in the real world or Object Plane
# centimeter
Known_width = 14.3

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)


font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type

# focal length finder function
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):
  
    # finding the focal length
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length
  
# distance estimation function
def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
  
    distance = (real_face_width * Focal_Length)/face_width_in_frame
  
    # return the distance
    return distance

def face_data(image):
  
    face_width = 0  # making face width to zero
  
    # converting color image to gray scale image
    converted_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    #converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  
    # detecting face in the image
    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
       )
  
    # looping through the faces detect in the image
    # getting coordinates x, y , width and height
    for(x,y,w,h) in faces:
  
        # draw the rectangle on the face
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image
  
        # getting face width in the pixels
        face_width = w
  
    # return the face width in pixel
    return face_width

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
ref_image=recognizer.read('trainer/trainer.yml')
ref_image_face_width=face_data(ref_image)  
"""

Focal_length_found = Focal_Length_Finder(
    Known_distance, Known_width, ref_image_face_width)
  
print(Focal_length_found)


id = 2 #number of persons you want to Recognize


names = ['','pragna']  #names, leave first empty bcz counter starts from 0


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning


# flag = True



while True:

    ret, img =cam.read() #read the frames using the above created object

    face_width_in_frame = face_data(img)
    if face_width_in_frame != 0:

        id, accuracy = ref_image.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
        
        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            Distance = Distance_finder(
            Focal_length_found, Known_width, face_width_in_frame)

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        cv2.putText(img, f"Distance: {round(Distance,2)} CM", (30, 35), fonts, 0.6, (0,255,0), 2)
        
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()
"""
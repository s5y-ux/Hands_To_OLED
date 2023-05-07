'''
********************************************************************************
*                                                                              *
* Project Start Date: 5/2/2023                                                 *
* Project End Date: 5/6/2023                                                   *
*                                                                              *
* License: https://opensource.org/license/mit/                                 *
*                                                                              *
* Programmed By: Joseph R. Shumaker                                            *
*                                                                              *
* Purpose: This project was made to appeal to a possible internship            *
* at JLP, This project is a comprehensive reflection of my                     *
* current abilities in C++ as it relates to possible technologies I may        *
* encounter later on in the field of computer science. This project features   *
* OOP, Data structures and algorithms, and cutting-edge open-source computer   *
* vision and artificial intelligence libraries and models as well as data      *
* conversion for readable data regarding integrated circuits.                  *
*                                                                              *
* All code seen below is my original work and all information regarding the    *
* use of library-specific methods and attributes were learned directly from    *
* the libraries' documentation.                                                *
*                                                                              *
* If you have any questions or would like to get in contact with me, my email  *
* and phone number is listed below...                                          *
*                                                                              *
* Phone: (805) 701 - 3171                                                      *
*                                                                              *
* Email: josephshumaker11@gmail.com                                            *
*                                                                              *
********************************************************************************
'''


'''
cv2: used for video capture and rendering
Documentation : https://docs.opencv.org/4.x/index.html

mediapipe: made by google for real time image recignoition
Documentation : https://developers.google.com/mediapipe/solutions/guide

serial: used for serial interaction on Microcontroller
Documentation : https://pyserial.readthedocs.io/en/latest/pyserial.html
'''
import cv2, mediapipe, serial

#Used to set Webcam ID for Video Capture (0 = default webcam, 1 = second webcam)
Video_Capture = cv2.VideoCapture(0)

#Used to set dimensions for Video capture
Video_Capture.set(3, 640)
Video_Capture.set(4, 480)

#Variable used to store model for Hand_Recognition (Tensorflow)
AI_Hand_Model = mediapipe.solutions.hands

#Variable used to store data for hand landmarks
Hand_Recognition = AI_Hand_Model.Hands()

#Variable used to store the drawling utilities for rendering our hand mesh
Edge_Utilities = mediapipe.solutions.drawing_utils

#Variable for referencing Microcontroller (Using linux /dev/ directory)
#If you are running this on a different operating system, please use COM ports
MicroController = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

#Program wont run unless MicroController is detected
if(MicroController.isOpen()):

    #Used as a little heads up for which Microcontroller you connected too
    print("Found {0}".format(MicroController.port))

    #Used for detection by frames
    while True:

    	#Used to store referable data for the video capture
    	success, Video_Capture_Data = Video_Capture.read()

    	#Used to render the video capture in RGB
    	Capture_In_RGB = cv2.cvtColor(Video_Capture_Data, cv2.COLOR_BGR2RGB)

    	#Uses RGB values in the mediapipe pre-trained model to recognize hands
    	results = Hand_Recognition.process(Capture_In_RGB)

    	#If statement for checking if hands have been detected
    	if results.multi_hand_landmarks:

            #Uses handpoints to refer to each landmark in detection
            for Hand_Points in results.multi_hand_landmarks:

                #Used to not surpass the colum width standard
                VCD = Video_Capture_Data

                #Uses variable to reference data for Hand Connection landmarks
                Model_Render = AI_Hand_Model.HAND_CONNECTIONS

                #Uses the drawing utilities from mediapipe to render hand graph
                Edge_Utilities.draw_landmarks(VCD, Hand_Points, Model_Render)

                #Rounds the floating point coordinates for usable integer value
                Hand_X_Coordinate = round(Hand_Points.landmark[0].x*100)
                Hand_Y_Coordinate = round(Hand_Points.landmark[0].y*100)

                #Stores values in an array
                values = [Hand_X_Coordinate, Hand_Y_Coordinate]

                OLED = "X={0}, Y={1}".format(values[0], values[1])

                #Encodes our data so that it can used by serial monitor
                MicroController.write(bytes(OLED, 'utf-8'))


    	#Displays the video
    	cv2.imshow('Video', Video_Capture_Data)

    	#Listener event for "quit" key
    	if(cv2.waitKey(1) & 0xFF == ord('q')):
    		break

#If the loop breaks as per exit, we destroy the capture process
Video_Capture.release()
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:42:08 2023

@author: karun
"""

import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()


    
def reg_voice(duration1,language1):
    
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("recording")
        audio_data = r.record(source, duration=duration1)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data,language=language1)
        print(text)

    return text 


from googletrans import Translator as te

###import googletrans.Translator as te




from cv2 import VideoCapture as vc
from cv2 import imshow
from cv2 import destroyAllWindows,waitKey

def cap_img():

    cam = vc(0)
    result, image = cam.read()
    imshow("myphoto",image)
    
    waitKey(0)
    destroyAllWindows()

    pass



def run():

    
    text1= reg_voice(5,'ta-IN')
    
    T2= te().translate(text1,dest='te')
    T3= te().translate(text1,dest='en')
    print(T2.text)
    print(T3.text)
    
    if 'photo' in T3.text:
        
        cap_img()

    pass  

run()
    
    






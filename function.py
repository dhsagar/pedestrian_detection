#all the helper function here
#import libraries
import cv2
from datetime import datetime
import time
from pedestrian import fullbody_cascade
import xml.etree.ElementTree as ET #import elementtree to work with xml
from dbconnect import mydb         #database connectior from dbconnect

#1 function to detect pedestrians
def detect(gray, frame):
    pedestrians = fullbody_cascade.detectMultiScale(gray, 1.3, 2)
    pd_count=0
    for (x, y, w, h) in pedestrians: # For each detected face:
        pd_count+=1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        cv2.rectangle(frame, (x, y - 20), (x+30,y), (255, 255, 0), -1)
        cv2.putText(frame, f'P{pd_count}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    return frame, pd_count
#2 resize each frame to reduce complexity
def frameresize(frame):
    resized_frame = cv2.resize(frame, (600, 400), interpolation=cv2.INTER_AREA)
    return resized_frame

#3 convert each frame into grayscale
def grayscale(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

#4 count FPS
def fpscount(prev_time, new_time):
    fps=round((1/(new_time-prev_time)),2)
    return fps

#5 generate/update the text file according to pedestrian info extracted from video
def txtFile(ssid, time, fps, pd_count, counter):
    if (counter % 10 == 0 and counter>0):
        file = open("output.txt","a")
        timestamp = datetime.fromtimestamp(time)
        file.write('\n'+str(ssid)+' '+str(timestamp)+' '+' '+str(fps)+' '+str(pd_count))
        file.close()

#6 function for pedestrian detection pipeline
def videopipeline(inputvideo):
    video_capture = cv2.VideoCapture(inputvideo)
    counter = 0
    prev_time = 0
    while (video_capture.isOpened()):
        ret, frame = video_capture.read()
        if ret == True:
            if (counter % 2 == 0):
                frame = frameresize(frame)
                gray = grayscale(frame)
                output, pd_count = detect(gray, frame)
                #show frame after pedestrians are detected
                cv2.imshow('Pedestrian', frame)
                # get current time to calculate fps
                new_time = time.time()
                fps = fpscount(prev_time, new_time)
                prev_time = new_time
                txtFile(int(counter / 10), new_time, fps, pd_count, counter)
                # close the window if 'x' is pressed
                if cv2.waitKey(1) & 0xFF == ord('x'):
                    break
            counter += 1
        else:
            break
    #release videocapture and destroy output window
    video_capture.release()
    cv2.destroyAllWindows()


### update the database and xml after pedetrian detection is done ###

#7 add element to xml under root
def addElementXML(filename, params):
    tree = ET.parse(filename)
    root = tree.getroot()
    #add element session as string
    session = ET.fromstring("<session><ssid>"+params[0]+"</ssid><date>"+params[1]+"</date><timestamp>"+params[2]+"</timestamp><fps>"+params[3]+"</fps><pd_count>"+params[4]+"</pd_count></session>")
    root.append(session)
    #save the update session to the xml
    tree.write(filename)

#8 insert data to pedestrian_info table at pedestrian database
def dbupdate(a, b, c, d, e):
    mycursor = mydb.cursor()
    sql = "INSERT INTO pedestrian_info (ssid, date, timestamp, fps, pd_count) VALUES (%s, %s, %s, %s, %s)"
    val = (a, b, c, d, e)
    mycursor.execute(sql, val)
    mydb.commit()


#define a function to read text file and extract data
def dbfromtxt(filename, mode):
    with open(filename, mode) as myfile:
        counter = 0
        for myline in myfile:
            if (counter > 0):
                ssid = myline.split()[0]
                date = myline.split()[1]
                timestamp = myline.split()[2]
                fps = myline.split()[3]
                pd_count = myline.split()[4]

                #dbupdate
                dbupdate(ssid, date, timestamp, fps, pd_count)

                #add data as session element to xml
                addElementXML('output.xml', [ssid, date, timestamp, fps, pd_count])

            counter += 1




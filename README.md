## Pedestrian Detection
This is a short summary of the pedestrian detection project. This project is done as a task for master thesis entrance test.
## Objectives
- Detect and count pedestrian in each frame from an input video file.
- Create .txt file according to the information from retrieved from video. Session ID, date, timestamp, number of pedestrians are data that will be written to the .txt file
- Update the database table with the same information.
- Generate an .xml file from the .txt file which will contain same dataset.
- Visualize the data on nicely formatted table using data visualization library.
##Necessary Import
- OpenCV for image processing and lot more
- Matplotlib for visualization
- Cascadeclassifier to detect pedestrian
- xml.etree.ElementTree to work with xml data
-datetime to get timestamp
  
##Coding Explanation
Whole project contains four Python(.py) files.
- pedestrian.py: It takes video file as input and detect and count pedestrians in each frame. It creates ‘output.txt’ to write pedestrian info in it. In every 10 frames programs calculates and write the timestamp, a session id (SSID), FPS and Number of pedestrians to the text file that has been created.
- update.py: This program takes ‘output.txt’ as input and update the pedestrian database according to the information retrieved from the .txt file. It also writes the information to the ‘output.xml’ file.
- visualize.py: In this program ‘output.xml’ is fed as input to plot the data on a nicely formatted table and visualize them.
- dbconnect.py: This file is for connecting MySQL server to our project.
- function.py: This file contains all the helper functions required for this project. Keeping all the functions away from the main program helps to keep the code clean and simple.
This project folder also includes
- Input video (‘input.avi’)
- ‘haarcascade_fullbody.xml’ and ‘output.xml’
- ‘output.txt’
- ‘pedestrian_pedestrian_info.sql’
To run and test this project, follow these simple steps:
- import .sql file to to MySQL server
- keep the Python files, input video and ‘output.xml’ in the same folder.
- install all the dependencies listed in necessary import section above.
- run pedestrian.py, update.py and visualize.py respectively to see the desired output sequentially.
A short literature research report (‘literature.pdf’), this technical report and a demonstration video (‘video_demonstration.mp4’) are also included with project folder.

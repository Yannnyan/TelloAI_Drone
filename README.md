# TelloAI_Drone
Drones competition in uni where I won second place

# Overview
This project was using CV for python library called CV2, create an algorithm for flying a drone in space in real time using image processing, and computer vision to detect aruco makers, estimate thier distances and angles from the drone, and then fly the drone using the markers as a guidance helper, to navigate through the room and through challenges set across it, such as flying inside a passage, and flying upwards the stairs, and rotating and mantaining balance in the room. 
</br> Using small edu drones, and thier SDK(Software Developement Kit) for giving them commands to follow such as, go forward turn clockwise, etc... 

# Stuggles
- Using windows as operating system might slow real time communication with the drone, use linux instead, since the packet transfer is done with UDP, windows tends to hold on to the packets and result in packet loss to the drone.
- Creating a multithreaded algorithm for recieving images in real time and processing them on another thread, and sending commands to the drone on another thread.
- Navigate the drone across the room using different markers, by calculating thier distances and angles from the drone, was a headache using CV arucodetect module, and using mathematical equations to calculate the distance using the optical focal length of the pinhole camera of the drone.
- Not crushing the drone and resulting in failure of it's propelors and damaging it's stability measurements.
- The drone battery was really not enough for running tests on the drone, it only lasts for about 15 minutes or less. So to solve this I used around 4 batteries I borrowed from friends and usb-c chargers meanwhile coding and running tests.
# Extra Project Documentations and summary
Link for event summary and description : https://docs.google.com/document/d/1xSagBC9Kp3lFaz0BnJAtK0Gy1gmYUMocNU_cYfQpZbs/edit </br>
link for the git that is extension to the description : https://github.com/AlonBarak-dev/Tello-Semi-Autonomous

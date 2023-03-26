# TelloAI_Drone
- Drones - using the 100 gram 100$ Tello Drones. </br>
- Drones competition in uni where I won second place </br>
- Video of the Competition: [Click me](https://www.youtube.com/watch?v=LKo4dLLlFnk) </br>
![image](https://user-images.githubusercontent.com/82415308/227801174-a12611f7-bb79-43f5-a299-70488acc5429.png)

# Overview
Project Details: Using CV for python library called CV2, create an algorithm for flying a drone in space in real time using image processing, and computer vision to detect aruco makers, estimate thier distances and angles from the drone, and then fly the drone using the markers as a guidance helper, to navigate through the room and through challenges set across it, such as flying inside a passage, and flying upwards the stairs, and rotating and mantaining balance in the room. 
</br> Using small edu drones, and thier SDK(Software Developement Kit) for giving them commands to follow such as, go forward turn clockwise, etc... 
</br> ![image](https://user-images.githubusercontent.com/82415308/227801293-6b391bec-8f8a-450f-94c9-29ba152bf870.png)

</br> [Ryze Tello Sdk](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)
# Challenges/Struggles
- Using windows as operating system might slow real time communication with the drone, use linux instead, since the packet transfer is done with UDP, windows tends to hold on to the packets and result in packet loss to the drone. It's a problem because a packet contains a command for the drone to do, so if it goes to waste then the drone might be waiting for commands but not recieving any.
- Creating a multithreaded algorithm for recieving images in real time and processing them on another thread, and sending commands to the drone on another thread.
- Navigate the drone across the room using different markers, by calculating thier distances and angles from the drone, was a headache using CV arucodetect module, and using mathematical equations to calculate the distance using the optical focal length of the pinhole camera of the drone.
- Not crushing the drone and resulting in failure of it's propelors and damaging it's stability measurements.
- The drone battery was really not enough for running tests on the drone, it only lasts for about 15 minutes or less. So to solve this I used around 4 batteries I borrowed from friends and usb-c chargers meanwhile coding and running tests.

# Images And Extra Visualization
### The Competition's Route
![image](https://user-images.githubusercontent.com/82415308/227801566-7448a8f0-43f6-451c-9e69-b6adbff0e26d.png)
![image](https://user-images.githubusercontent.com/82415308/227801663-143468c4-2484-4ca2-925f-85437a777c3f.png)
### Drone Size Comparison
![image](https://user-images.githubusercontent.com/82415308/227801687-0ea3364e-8b97-43ce-8520-b7fb120d4eeb.png)
### Group Picture
![image](https://user-images.githubusercontent.com/82415308/227801817-9f5352f4-572c-4edb-a043-29caae2cbe5f.png)

# Extra Project Documentations and summary
Link for event summary and description : https://docs.google.com/document/d/1xSagBC9Kp3lFaz0BnJAtK0Gy1gmYUMocNU_cYfQpZbs/edit </br>
link for the git that is extension to the description : https://github.com/AlonBarak-dev/Tello-Semi-Autonomous

import queue
import time
from queue import Queue
from threading import Thread
from time import sleep
import States
import cv2
import arucoDetectImage as ar
from arucoDetectImage import *

from control_drone import control_drone


class Drone:
    def __init__(self, controller: control_drone):
        self.aruco_detect = ar.ArucoDetection()
        self.controller = controller
        self.tello = controller.tello
        self.recent_image_queue = Queue()
        # self.video_capture =  self.tello.get_video_capture()
        self.expected_aruco = 0

    def start(self):
        # reader_thread = Thread(target=self.read_images)
        # reader_thread.start()
        algorithm_thread = Thread(target=self.algorithm)
        algorithm_thread.start()

    def algorithm(self):
        """
        Read a frame, then give it to the algorithm to process
        :return:
        """
        while True:
            frame = self.tello.get_frame_read().frame
            coords, ids = self.aruco_detect.find_arucos(frame)
            if len(ids) != 0:
                print(ids)
                distance = self.aruco_detect.calculate_distance_toAruco1(self.aruco_detect.arucoWidth(coords[0][0]))
                for i in range(len(ids)):
                    if ids[i][0] == self.expected_aruco:
                        self.state_machine(self.expected_aruco, coords[i], distance)
                        time.sleep(1)
                        break

    # def read_images(self):
    #     while True:
    #         image = self.tello.get_frame_read().frame
    #         cv2.imshow("Tello", image)
    #         cv2.waitKey(1)

    def state_machine(self, aruco_id, coords, distance):
        if aruco_id == 0:
            for i in range(2):
                self.controller.tello.move_forward(65)
            self.controller.tello.rotate_counter_clockwise(90)
            self.expected_aruco += 1
        elif aruco_id == 1:
            for i in range(3):
                self.controller.tello.move_forward(300)
            self.expected_aruco = 3
        elif aruco_id == 2:
            pass
        elif aruco_id == 3:
            self.controller.tello.move_forward(200)
            self.controller.tello.rotate_counter_clockwise(180)
            self.controller.tello.move_right(200)
            self.expected_aruco = 5
        elif aruco_id == 4:
            self.controller.tello.rotate_clockwise(90)
            for i in range(3):
                self.controller.tello.move_forward(270)
            self.expected_aruco = 6
        elif aruco_id == 5:
            for i in range(4):
                self.controller.tello.move_forward(280)
            self.controller.tello.move_left(100)
            self.expected_aruco = 4
        elif aruco_id == 6:
            self.controller.tello.move_left(30)
            for i in range(3):
                self.controller.tello.move_back(270)
            self.controller.tello.rotate_counter_clockwise(90)
            self.controller.tello.move_left(130)
            self.expected_aruco = 7
        elif aruco_id == 7:
            for i in range(2):
                self.controller.tello.move_forward(200)
            for i in range(2):
                self.controller.tello.move_up(70)
            self.controller.tello.move_forward(200)
            for i in range(2):
                self.controller.tello.move_up(70)
            self.controller.tello.move_forward(150)
            self.expected_aruco = 9
        elif aruco_id == 8:
            for i in range(3):
                self.controller.tello.move_forward(100)
            self.expected_aruco = 1
        elif aruco_id == 9:
            self.controller.send_ccw(180)
            self.controller.tello.move_forward(200)
            for i in range(2):
                self.controller.tello.move_down(70)
            self.controller.tello.move_forward(100)
            self.controller.tello.move_down(100)
            for i in range(2):
                self.controller.tello.move_forward(150)
            self.expected_aruco = 1
        elif aruco_id == 10:
            pass

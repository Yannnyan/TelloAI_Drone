import math
import sys
import cv2
import imutils as imutils
import fileGen as constants
import numpy as np


def floor_point(point):
    x = math.floor(point[0])
    y = math.floor(point[1])
    return (x, y)


def is_left_from_aruco(coords):
    print("coords: " + str(coords[1][0]) + " " + str(coords[0][0]))
    center_point_x = (coords[1][0] + coords[0][0]) / 2
    print(center_point_x)
    if 330 <= center_point_x <= 360:
        return None
    return center_point_x <= 330

def is_down_from_aruco(self, coords):
    center_point_y = (coords[0][0][1] - coords[0][0][2]) / 2
    return True if (center_point_y <= 360) else False


class ArucoDetection:
    def __init__(self):
        self.arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)
        self.arucoParams = cv2.aruco.DetectorParameters_create()
        self.focalLength = 541
        self.cameraMatrix = np.matrix([[constants.fx, 0, constants.cx], [0, constants.fy, constants.cy], [0, 0, 1]])
        self.distCoeffs = np.matrix([0.15167372260107306, 0.12119628585051517, 0, 0])
        self.real_ArucoWidth = 14  # in centimeters

    def find_arucos(self, image):
        """
        :return:
        """
        # # filter image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        ids_list = []
        corners_list = []
        (corners, ids, rejected) = cv2.aruco.detectMarkers(gray, self.arucoDict,
                                                           parameters=self.arucoParams)
        if ids is not None:
            for c, i in zip(corners, ids):
                ids_list.append(i)
                corners_list.append(c)
        return corners_list, ids_list

    def arucoWidth(self, arucoCoords):
        """
        :param image:
        :param arucoCoords:
        :return:
        """
        bottomLeftPoint = arucoCoords[0]
        # topRightPoint = arucoCoords[1]
        topLeftPoint = arucoCoords[3]
        arucoWidth = topLeftPoint[1] - bottomLeftPoint[1]
        return arucoWidth

    def calculate_distance_toAruco1(self, arucoWidthPixels):
        return (self.real_ArucoWidth * self.focalLength) / arucoWidthPixels
        # return tvec[arucoID][0][2]

    def calculate_distance_toAroco2(self, tvec, arucoID):
        return tvec[arucoID][0][2]

    def calculate_distance_toAroco3(self, tvec, arucoID):
        x = tvec[arucoID][0][0]
        y = tvec[arucoID][0][1]
        dist = x ** 2 + y ** 2
        return dist

    def calculate_angle_toAruco(self, tvec, arucoID, dist):
        """
        calculates angle in degrees
        :param tvec:
        :param arucoID:
        :return:
        """
        # print("X value: " + str(tvec[arucoID][0][0]))
        return math.asin(tvec[arucoID][0][0] / (dist * 10)) * 180 / math.pi

    def draw_arucos(self, image, coords):
        """
        :return: an image drawn with rectangles on the arucos
        """
        color = (0, 0, 255)
        for arr in coords:
            for cord in arr:
                topLeftPoint = floor_point([cord[0][0], cord[0][1]])
                bottomRightPoint = floor_point([cord[2][0], cord[2][1]])
                cv2.rectangle(image, topLeftPoint, bottomRightPoint, color, 2)

    def resizeImage(self, image):
        return imutils.resize(image, width=720, height= 720)

    def drawImage(self, image):
        cv2.imshow("arucoDetection", image)
        return cv2.waitKey(200)
        # return cv2.waitKey(0)

    def get_location_aruco(self, image):
        coords, ids = self.find_arucos(image)
        cameraMatrix = self.cameraMatrix
        distCoeffs = self.distCoeffs
        tvecs = []
        for i in range(len(coords)):
            width = self.arucoWidth(coords[i][0])
            rvec, tvec, objectPoints = cv2.aruco.estimatePoseSingleMarkers(corners=coords[i], cameraMatrix=cameraMatrix,
                                                                           markerLength=width,
                                                                           distCoeffs=distCoeffs)
            tvecs.append(tvec)
        return tvecs, ids

    def get_distance_and_angle(self, image):
        coords, ids = self.find_arucos(image)
        cameraMatrix = self.cameraMatrix
        distCoeffs = self.distCoeffs
        width = self.arucoWidth(coords[0][0])
        rvec, tvec, objectPoints = cv2.aruco.estimatePoseSingleMarkers(corners=coords[0], cameraMatrix=cameraMatrix,
                                                                       markerLength=width,
                                                                       distCoeffs=distCoeffs)
        distance = round(self.calculate_distance_toAruco1(self.arucoWidth(coords[0][0])), 3)
        angle = round(self.calculate_angle_toAruco(tvec, 0, distance), 2)
        return distance, angle

    def process_Image(self, image):
        """
        This function takes an image and processes it to provide
        the angle and the distance from the camera
        :return: an the processes image
        """
        im = self.resizeImage(image)
        coords, ids = self.find_arucos(im)
        if coords.__len__() == 0:
            return im
        self.draw_arucos(image, coords)
        for i in range(len(ids)):
            width = self.arucoWidth(coords[i][0])
            cameraMatrix = self.cameraMatrix
            distCoeffs = self.distCoeffs
            rvec, tvec, objectPoints = cv2.aruco.estimatePoseSingleMarkers(corners=coords[i], cameraMatrix=cameraMatrix,
                                                                           markerLength=width,
                                                                           distCoeffs=distCoeffs)
            distance, angle = self.get_distance_and_angle(im)
            im = cv2.drawFrameAxes(im, cameraMatrix=cameraMatrix, distCoeffs=distCoeffs, rvec=rvec[0], tvec=tvec[0],
                                   thickness=4, length=100)
            im = cv2.putText(im,
                             'd: ' + str(distance) +
                             # 'd: ' + str(arDet.calculate_distance_toAroco2(tvec, 0)) +
                             # 'd: ' + str(arDet.calculate_distance_toAroco3(tvec, 0)) +
                             '\n a: ' + str(angle),
                             (round(coords[i][0][2][0]), round(coords[i][0][2][1])),
                             5,
                             0.7,  # font size
                             (22, 22, 245),  # color
                             1
                             )
        return im


    def get_aruco_positions(self, ids, coords):
        tvecs = []
        for i in range(len(ids)):
            width = self.arucoWidth(coords[i][0])
            cameraMatrix = self.cameraMatrix
            distCoeffs = self.distCoeffs
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners=coords[i], cameraMatrix=cameraMatrix,
                                                                markerLength=width,
                                                                distCoeffs=distCoeffs)
            tvecs.append(tvec)
        return tvecs

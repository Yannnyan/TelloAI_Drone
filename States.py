from control_drone import control_drone


class states:
    def __init__(self, controller: control_drone):
        self.controller = controller

    def aruco_0(self):

        for i in range(2):
            self.controller.send_go_forward(65)
        self.controller.send_ccw(90)

    def aruco_1(self):
        # distance_to_go_first = distance - 200
        # self.controller.send_go_forward()
        for i in range(3):
            self.controller.send_go_forward(380)
            # self.controller.send_go_left(30)
        # self.controller.send_go_left(40)

    def aruco_3(self):
        self.controller.send_ccw(90)
        for i in range(2):
            self.controller.send_go_forward(100)
        self.controller.send_ccw(90)
        self.controller.send_go_forward(100)

    def aruco_5(self, distance):
        distance_to_fly = distance + 100
        for i in range(3):
            self.controller.send_go_forward(int(distance_to_fly / 3))

    def aruco_4(self, distance):
        distance_to_fly = distance - 90
        for i in range(2):
            self.controller.send_go_forward(int(distance_to_fly / 2))
        self.controller.send_cw(90)
        self.controller.send_go_left(35)
        for i in range(3):
            self.controller.send_go_forward(270)

    def aruco_6(self):
        self.controller.send_ccw(90)
        self.controller.send_go_forward(30)
        self.controller.send_ccw(90)
        # for i in range(2):
        # self.controller.send_go_forward(50)
        # self.controller.send_ccw(180)
        # self.controller.send_go_left(50)
        for i in range(3):
            self.controller.send_go_forward(290)

    def aruco_00(self):
        for i in range(2):
            self.controller.send_go_forward(105)
        self.controller.send_cw(90)

    def aruco_7(self):
        # self.controller.send_go_left(60)
        for i in range(3):
            self.controller.send_go_forward(120)
        self.controller.send_cw(180)

    def aruco_8(self):
        self.controller.send_ccw(180)
        for i in range(4):
            self.controller.send_go_up(50)
        for i in range(2):
            self.controller.send_go_forward(100)

    def aruco_9(self, distance):
        distance_to_go_to = distance - 170
        for i in range(3):
            self.controller.send_go_forward(int(distance_to_go_to / 3))
        self.controller.send_ccw(90)
        # for i in range(2):
        #     self.controller.send_go_forward(30)
        self.controller.send_ccw(90)
        self.controller.send_go_forward(100)

    def aruco_88(self, distance):
        distance_to_go_to = distance - 150
        for i in range(2):
            self.controller.send_go_down(70)
        for i in range(3):
            self.controller.send_go_forward(int(distance_to_go_to / 3))
        for i in range(2):
            self.controller.send_go_down(50)
        for i in range(2):
            self.controller.send_go_forward(100)
        for i in range(2):
            self.controller.send_go_forward(200)

    # def align_with_aruco(self, ):

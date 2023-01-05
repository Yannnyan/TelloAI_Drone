import control_drone

LOOKING_FOR_ARUCO = 0  # IF THE DRONE DID NOT FIND AN ARUCO FOR 5 SECONDS AND IS NOT ON_TASK
ON_TASK = 1  # IF THE DRONE READ A BARCODE AND KNOWS THAT WHAT IT'S DIRECTIONS ARE


class Directions:
    def __init__(self, cw, dx, dy, dz):
        self.cw = cw
        self.dx = dx
        self.dy = dy
        self.dz = dz

    def make_move_by_directions(self, controller: control_drone.control_drone):
        if self.dx != 0:
            if self.dx < 0:
                controller.send_go_right(-self.dx)
            else:
                controller.send_go_left(self.dx)
        if self.dz != 0:
            if self.dz < 0:
                controller.send_go_back(-self.dz)
            else:
                while self.dz > 500:
                    controller.send_go_forward(500)
                    self.dz -= 500
                if self.dz > 0:
                    controller.send_go_forward(self.dz)
        if self.dy != 0:
            if self.dy < 0:
                controller.send_go_down(-self.dy)
            else:
                controller.send_go_up(self.dy)
        if self.cw != 0:
            if self.cw < 0:
                # controller.send_ccw(-self.cw)
                controller.tello.rotate_counter_clockwise(-self.cw)
            else:
                controller.tello.rotate_clockwise(self.cw)
                # controller.send_cw(self.cw)


class State_Machine:

    # THIS IS A STATE MACHINE CLASS THAT GIVEN ARUCO ID DEFINES THE POSITION RELATIVE TO THE ARUCO TO GO TO
    def __init__(self):
        self.barcode_id = 0
        self.state = LOOKING_FOR_ARUCO

    def finish_move(self):
        self.state = LOOKING_FOR_ARUCO

    def next_move(self, ids: list, aruco_positions: list):
        # print(ids, aruco_positions)
        # print(ids[0])
        print('barcode id ' + str(self.barcode_id))
        for _id, position in zip(ids[0], aruco_positions):
            print(_id, position)
            if _id == self.barcode_id and self.state == LOOKING_FOR_ARUCO:
                # self.state = ON_TASK
                return self.move_by_id(_id, position)

    def move_by_id(self, _id, aruco_position) -> Directions:
        print(_id)
        if _id == 0:
            angle = -90
            x = 0
            y = 0
            z = 150
            self.barcode_id = 1
            return Directions(angle, x, y, z)

        elif _id == 1:
            angle = 1
            x = 0
            y = 0
            z = 1000
            self.barcode_id = 3
            return Directions(angle, x, y, z)

        elif _id == 3:
            x = 0
            y = 0
            z = 100
            return Directions(1, x, y, z)


        elif _id == 6:
            # print(aruco_position)
            x = aruco_position[0][0][0]
            y = aruco_position[0][0][1]
            z = aruco_position[0][0][2]
            posX = 0
            posY = 0
            posZ = 0
            epsilon = 100
            if not (epsilon > x > -epsilon):
                posX = x - epsilon
            if not (epsilon > y > -epsilon):
                posY = y - epsilon
            if not (epsilon > z > -epsilon):
                posZ = z - epsilon
            return Directions(40, posX, posY, posZ)

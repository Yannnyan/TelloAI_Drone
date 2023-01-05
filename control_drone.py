import socket
import time
import djitellopy


class control_drone:
    def __init__(self):
        # host = ''
        # port = 9000
        # locaddr = (host, port)

        # print("creating socket")
        # Create a UDP socket
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # print("binding")
        # self.tello_address = ('192.168.10.1', 8889)
        # self.sock.bind(locaddr)
        self.took_off = False
        self.streamon = False
        self.tello = djitellopy.Tello()

    def send_msg(self, msg):
        # msgback = ''
        # while msgback != 'ok':
        #     print('sending message: ' + msg)
        #     msgback = self.send_msg_to_drone(msg)
        #     msgback = msgback.decode(encoding='utf-8')
        #     print(msgback)
        #     if msgback.startswith('error'):
        #         break
        msgback = 'error'
        while msgback.startswith('error'):
            msgback = self.tello.send_command_with_return(msg, 1)
            print(msgback)


    def send_msg_to_drone(self, msg):
        msg = msg.encode(encoding="utf-8")
        sent = self.sock.sendto(msg, self.tello_address)
        print('sent message: ' + str(sent))
        answer, server = self.sock.recvfrom(1518)
        return answer

    def send_command(self):
        self.send_msg('command')

    def send_streamon(self):
        if not self.streamon:
            self.send_msg('streamon')
            self.streamon = True

    def send_streamoff(self):
        if self.streamon:
            self.send_msg('streamoff')
            self.streamon = False

    def send_takeoff(self):
        if not self.took_off:
            # self.send_msg('takeoff')
            self.tello.takeoff()
            self.took_off = True
            # self.send_go_up(100)
            self.tello.move_up(110)


    def send_land(self):
        if self.took_off:
            # self.send_msg('land')
            self.tello.land()
            self.took_off = False

    def send_go_forward(self, forward_centi):
        # self.send_msg('forward ' + str(forward_centi))
        self.tello.move_forward(forward_centi)

    def send_go_left(self, left_centi):
        # self.send_msg('left ' + str(left_centi))
        self.tello.move_left(left_centi)

    def send_go_right(self, right_centi):
        # self.send_msg('right ' + str(right_centi))
        self.tello.move_right(right_centi)

    def send_go_back(self, back_centi):
        # self.send_msg('back ' + str(back_centi))
        self.tello.move_back(back_centi)

    def send_go_up(self, up_centi):
        # self.send_msg('up ' + str(up_centi))
        self.tello.move_up(up_centi)

    def send_go_down(self, down_centi):
        # self.send_msg('down ' + str(down_centi))
        self.tello.move_down(down_centi)

    def send_stop(self):
        self.send_msg('stop')


    def send_emergency(self):
        self.tello.emergency()
        # self.send_msg('emergency')

    def send_cw(self, cw_angle):
        # self.send_msg('cw ' + str(cw_angle))
        self.tello.rotate_clockwise(cw_angle)

    def send_ccw(self, ccw_angle):
        # self.send_msg('ccw ' + str(ccw_angle))
        self.tello.rotate_counter_clockwise(ccw_angle)

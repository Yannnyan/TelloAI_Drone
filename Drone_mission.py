import threading
from control_drone import control_drone
import keyboard_listener
from Drone import Drone

controller = control_drone()
controller.send_command()
controller.send_streamon()
thread_listen = threading.Thread(target=keyboard_listener.listener, args=[controller])
thread_listen.start()

Drone(controller).start()





from pynput import keyboard
from control_drone import control_drone
import threading


def listener(controller: control_drone):
    with keyboard.Events() as events:
        print("start listening")
        while True:
            try:
                event = events.get()
                print("got key")
                if event is None:
                    continue
                elif event and isinstance(event, keyboard.Events.Press):
                    if event.key == keyboard.Key.space:
                        # tello.land()
                        controller.send_land()
                    elif event.key == keyboard.Key.up:
                        # tello.takeoff()
                        controller.send_takeoff()
                    elif event.key == keyboard.Key.left:
                        # tello.move_left(20)
                        controller.send_go_left(20)
                    elif event.key == keyboard.Key.right:
                        # tello.move_right(20)
                        controller.send_go_right(20)
                    elif event.key == keyboard.Key.tab:
                        # tello.rotate_clockwise(60)
                        controller.send_cw(60)
                    elif event.key == keyboard.Key.backspace:
                        controller.send_emergency()


            except Exception as e:
                print(e)

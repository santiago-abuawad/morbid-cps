
#LIBRARIES
import time
import threading
import os
from os import system
from colorama import Fore as Color
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

system("title " + "Morbid Autoclicker By[Github @santiagoabol]")
#INPUT CPS VALUES
delay_left = int(input(f"{Color.WHITE}LEFT{Color.WHITE}--> "))
delay_right = int(input(f"{Color.WHITE}RIGHT{Color.WHITE}--> "))
button_left = Button.left
button_right = Button.right
start_stop_key_left = KeyCode(char='z')
start_stop_key_right = KeyCode(char='y')
exit_key = KeyCode(char='x')
#CLEAR CONSOLE
system("cls")

#MAIN PRINTS
print(f"""{Color.RED}


                                                    ▄▀▀▄ ▄▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀█▄▄  
                                                   █  █ ▀  █ █      █ █   █   █ ▐ ▄▀   █ █   █  █  █ ▄▀   █ 
                                                   ▐  █    █ █      █ ▐  █▀▀█▀    █▄▄▄▀  ▐   █  ▐  ▐ █    █ 
                                                     █    █  ▀▄    ▄▀  ▄▀    █    █   █      █       █    █ 
                                                   ▄▀   ▄▀     ▀▀▀▀   █     █    ▄▀▄▄▄▀   ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀ 
                                                   █    █             ▐     ▐   █    ▐   █       █ █     ▐  
                                                   ▐    ▐                       ▐        ▐       ▐ ▐        


                                        
                                                                      {Color.WHITE}LEFT Z || RIGHT Y
""")

#LEFT
class ClickMouse_left(threading.Thread):
    def __init__(self, delay_left, button_left):
        super(ClickMouse_left, self).__init__()
        self.delay = delay_left
        self.button = button_left
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(0.9/self.delay)
            time.sleep(0.1)
#RIGHT
class ClickMouse_right(threading.Thread):
    def __init__(self, delay_right, button_right):
        super(ClickMouse_right, self).__init__()
        self.delay = delay_right
        self.button = button_right
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(0.9/self.delay)
            time.sleep(0.1)
#LEFT
mouse = Controller()
click_thread_left = ClickMouse_left(delay_left, button_left)
click_thread_left.start()
#RIGHT
mouse = Controller()
click_thread_right = ClickMouse_right(delay_right, button_right)
click_thread_right.start()

#STAR AND EXIT

def on_press_left(key):
    if key == start_stop_key_left:
        if click_thread_left.running:
            click_thread_left.stop_clicking()
        else:
            click_thread_left.start_clicking()            

def on_press_right(key2):
    if key2 == start_stop_key_right:
        if click_thread_right.running:
            click_thread_right.stop_clicking()
        else:
            click_thread_right.start_clicking()
         
#LISTENER CONSOLE
with Listener(on_press_left,on_press_right) as listener:
    listener.join()

#y==================================================
#CODE BY santiago-abuawad                              
#==================================================

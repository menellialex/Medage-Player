import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame.mixer as mx

mx.init()

PAUSE_KEY = "p"
RESUME_KEY = "r"
STOP_KEY = "s"
ADD_KEY = "a"
REMOVE_KEY = "x"
SKIP_FORWARD_KEY = "f"
SKIP_BACK_KEY = "b"

while True:
    print("Control (",PAUSE_KEY," to pause, ",RESUME_KEY," to resume, ",STOP_KEY," to stop, ", ADD_KEY," to add to queue, ", REMOVE_KEY," to remove from queue, ", SKIP_FORWARD_KEY," to skip forward, ", SKIP_BACK_KEY, " to skip back): ", end="", sep="")
    control = input()
    if control == PAUSE_KEY and playing == True:
        playing = False
        mx.pause()
    if control == RESUME_KEY and playing == False:
        playing = True
        mx.resume()
    if control == STOP_KEY:
        exit()
    if control.find(ADD_KEY) == 0:
        new_song = control[2:]
        mx.Sound
    if control == REMOVE_KEY:
        medagl.remove_song()

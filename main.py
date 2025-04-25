"""
Implement a program that :
- Generates a .exe file
- When the .exe is launched, it stays in the processes of the computer
- When the mouse is used, nothing happens
- When any key of the keyboard is pressed instead of the right keys combination :
1. The sound of crashing windows windows plays in a loop for a few seconds, displaying a lot of windows saying
"You didn't say the magic word !"
2. a clip of Dennis Nedry's program in Jurassic Park 1 starts to play, looping until the right keys are pressed. 
("Ah ah ah, you didn't say the magic word !")
- When the right keys are pressed, the end of the clip (Samuel Jackson saying "PLEASE ! GODDAMMIT, I HATE THIS HACKER CRAP !")
"""

import tkinter
import keyboard
import vlc
import time

def closing_sound() :
    sound = vlc.MediaPlayer("assets/hacker_crap.mp3")
    sound.play()
    time.sleep(5)

def close() :
    if keyboard.is_pressed("ctrl+n+o") :
        closing_sound()
        return True

while True :
    time.sleep(0.1)
    if close() :
        break
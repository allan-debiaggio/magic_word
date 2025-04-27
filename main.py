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

import customtkinter
import keyboard
import vlc
import time
import pygame
import threading

pygame.mixer.init()

def closing_sound() :
    pygame.mixer.music.load("assets/hacker_crap.mp3")
    pygame.mixer.music.play()
    time.sleep(5)



def error_sound() :
    error_channel = pygame.mixer.Channel(1)
    error_channel.play(pygame.mixer.Sound("assets/windows_xp_error.mp3"))
    # pygame.mixer.music.play(1)



def background_task() :
    while True :
        if keyboard.read_event() :
            error_sound()
            looping_sound()
            time.sleep(0.1)

        if keyboard.is_pressed("ctrl+n+o") :
            pygame.mixer.music.stop()
            closing_sound()
            break




def looping_sound() :
    pygame.mixer.music.load("assets/magic_word.mp3")
    pygame.mixer.music.play(-1)
    
def on_close(event = None) :
    print("Close button pressed !")

def on_minimize(event = None) :
    print("Minimized button pressed !")

def on_restore(event = None) :
    print("Restore pressed !")

def create_window() :
    window = customtkinter.CTk()
    window.title("Ah ah aaaaah !")
    window.geometry("300x150")

    label = customtkinter.CTkLabel(
        window,
        text = "You didn't say the magic word !",
        font = ("Arial", 14)
    )
    label.pack(pady = 20)

    window.protocol("WM_DELETE_WINDOW", on_close) # Action when closing button is pressed

    window.bind("<Unmap>", on_minimize) 
    window.bind("<Map>", on_restore)

    return window



def main() :
    window = create_window()

    thread = threading.Thread(target=background_task,daemon=True)
    thread.start()

    window.mainloop()



main()
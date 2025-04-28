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



def background_task() :
    window_positions = [] # Making a list to remember all windows positions
    x_offset, y_offset = 50, 50

    while True :
        if keyboard.read_event() : # If any key is pressed
            if not keyboard.is_pressed("ctrl+n+o") :
                x = 100 + len(window_positions) * x_offset
                y = 100 + len(window_positions) * y_offset

                
                threading.Thread(target=lambda: create_and_show_window(x,y), daemon=True).start()

                error_sound()
                looping_sound()

                window_positions.append((x,y)) # Adding some coordinates to move slightly the window

            time.sleep(0.1)        # Short reaction to listen to keyboard inputs

        if keyboard.is_pressed("ctrl+n+o") :
            pygame.mixer.music.stop()
            closing_sound()
            break


def create_and_show_window(x,y) :
    window = create_window()
    window.geometry(f"300x150+{x}+{y}") 
    window.mainloop()  # Run on main thread



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
    window.title("PERMISSION DENIED !")
    window.geometry("300x150")

    window.attributes("-topmost", True) # Makes the window popup in front of anything you're currently 

    label = customtkinter.CTkLabel(
        window,
        text = "YOU DIDN'T SAY THE MAGIC WORD !!!",
        font = ("Arial", 14)
    )
    label.pack(pady = 20)

    button = customtkinter.CTkButton(
        window,
        text = "GODDAMMIT !!!",
        command=lambda : button_action(window)
    )
    button.pack(pady=10)

    window.protocol("WM_DELETE_WINDOW", lambda : on_close(window)) # Action when closing button is pressed

    window.bind("<Unmap>", lambda event : on_minimize(window)) 
    window.bind("<Map>", lambda event : on_restore(window))

    return window

def button_action(window) :
    create_and_show_window(window.winfo_x() + 50, window.winfo_y() + 50)
    error_sound()
    looping_sound()

def main() :

    background_task()
    thread = threading.Thread(target=background_task, daemon=True)
    thread.start()

    

main()
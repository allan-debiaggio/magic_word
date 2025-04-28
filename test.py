import customtkinter
from PIL import Image, ImageTk

def main() :

    gif_path = "assets/magic_word.gif"
    gif = Image.open(gif_path)
    gif_width, gif_height = gif.size

    window = customtkinter.CTk()
    window.title("Permission denied !")
    window.geometry(f"{gif_width}x{gif_height}")


    label = customtkinter.CTkLabel(window, text="")
    label.pack()

    def update_frame(frame_index) :
        try :
            gif.seek(frame_index)
            gif_tk = ImageTk.PhotoImage(gif)
            label.configure(image = gif_tk)
            label.image = gif_tk
            window.after(gif.info["duration"], update_frame, frame_index + 1)
        except EOFError :
            update_frame(0)

    update_frame(0)

    window.mainloop()

main()
import tkinter
import pyglet
from tkinter.font import Font

from commands import change_engine,start_game

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

FRAME_WIDTH = WINDOW_WIDTH
FRAME_HEIGHT = WINDOW_HEIGHT - 100

SUBFRAME_WIDTH = WINDOW_WIDTH/2
SUBFRAME_HEIGHT = WINDOW_HEIGHT

ENGINE_BUTTON_WIDTH = 260
ENGINE_BUTTON_HEIGHT = 40

START_BUTTON_WIDTH = 205
START_BUTTON_HEIGHT = 40

## Custom fonts

# Look for font, throw error if not found
font_file = "basic/fonts/Silkscreen/slkscr.ttf"
try:
    pyglet.font.add_file(font_file)
    silk16 = ("Silkscreen", 16)
    silk20 = ("Silkscreen", 20)
    silk32 = ("Silkscreen", 32)
except Exception as e:
    print("Error: Font not found")
    print(e)
    exit()

## Main window
# Window : black background, title "Engine Sim Launcher"
root = tkinter.Tk()
root.title("Engine Sim Launcher")
root.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
root.resizable(False, False)
root.configure(background="black")

# Title label : centered, white text, font SilkScreen 32
title_label = tkinter.Label(root, text="Engine Sim Launcher", font=silk32, fg="white", bg="black")
title_label.pack(fill=tkinter.BOTH, expand=True, pady=30)

# Frame : 800x400, black background
frame = tkinter.Frame(root, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg="black")
frame.pack(fill=tkinter.BOTH, expand=True)

# subframes : 400x400, black background
left = tkinter.Frame(frame, width=SUBFRAME_WIDTH, height=SUBFRAME_HEIGHT, bg="black")
left.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
right = tkinter.Frame(frame, width=SUBFRAME_WIDTH, height=SUBFRAME_HEIGHT, bg="black")
right.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

# Buttons : 200x100, white text, font SilkScreen 20, white border, black background
# Buttons have a frame as border : 200x100 with a white border and black background, centered in each subframe
change_engine_border = tkinter.Frame(left, width=ENGINE_BUTTON_WIDTH+10, height=ENGINE_BUTTON_HEIGHT+10, bg="white")
change_engine_border.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
change_engine_button = tkinter.Button(change_engine_border, text="Change Engine", font=silk20, fg="white", bg="black",
                                        borderwidth=1, relief="solid", command=lambda: change_engine())
change_engine_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

start_game_border = tkinter.Frame(right, width=START_BUTTON_WIDTH+10, height=START_BUTTON_HEIGHT+10, bg="white")
start_game_border.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
start_game_button = tkinter.Button(start_game_border, text="Start Game", font=silk20, fg="white", bg="black",
                                        borderwidth=1, relief="solid", command=lambda: start_game())
start_game_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
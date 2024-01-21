import math
from tkinter import *
import os
import UI.verification as ver
from PIL import Image, ImageTk

import aslText
import speechASL


# from tkmacosx import Button


class Calculator:

    # initializes the screen
    def __init__(self):
        root = Tk()
        print(os.listdir(os.getcwd()))
        file_path = os.path.join(os.getcwd(), "UI", "asl.png")
        orig_image = Image.open(file_path)
        resizedImage = orig_image.resize((math.ceil(0.8 * root.winfo_screenwidth()),
                                          math.ceil(0.20 * 0.8 * root.winfo_screenheight())))
        tk_image = ImageTk.PhotoImage(resizedImage)
        tk_label = Label(root, image=tk_image)
        tk_label.grid(row=4, column=0, columnspan=2)
        set_frame(root)
        root.mainloop()


# sets up all necessary details associated with the current frame
def set_frame(root: Tk):
    set_frame_info(root)
    center_gui(root)
    # add_image(root, img)
    set_buttons(root)
    set_text_label(root)

def verification_handler(root):
    verifier, present  = ver.check_open_cv()
    popup_window = Tk()
    formatted_dim = f"{math.ceil(0.8*0.30*root.winfo_screenwidth())}x{math.ceil(0.8*0.20*root.winfo_screenwidth())}"
    popup_window.geometry(formatted_dim)
    text_label = Label(popup_window,text=f"The following dependencies {verifier} are "
                                         f"{'confirmed' if present else ' missing'}")
    center_gui(popup_window)
    # text_label2 = Label(popup_window, text="\n \n \n")
    # text_label2.grid(row=0, column=0)
    test_button = Button(popup_window, text= "Test your camera", command= lambda: ver.test_camera(), bg="#daf5f3",
                         fg="#000000", font=("Comic Sans", 15))
    test_button.grid(row=1, column=1, columnspan=2)
    text_label.grid(row=2, column=2)
    popup_window.wm_title("Verification")



# sets all base info of the frame
def set_frame_info(root: Tk):
    w, h = math.ceil(root.winfo_screenwidth() * 0.8), math.ceil(root.winfo_screenheight() * 0.8)
    geom = f"{w}x{h}"
    root.geometry(geom)
    root.title("Hand-Haven")
    # set_icon(root)
    root.resizable(False, False)  # this can be changed


def set_text_label(root: Tk):
    text1 = "About The Authors"
    text2 = "A rag tag team of misfits who occasionally commit the sin of touching grass\n" \
            "coming to you as the makers of famous 210 projects like Swim-Team Management, Course Management, " \
            "\n Quiz Builder and Prescriptify!"
    tk_label1 = Label(root, text=text1, fg="#000000",  bg="#daf5f3", font=("Comic Sans", 30))
    tk_label2 = Label(root, text=text2, fg="#000000", bg="#daf5f3", font=("Comic Sans", 20))
    tk_label1.grid(row=0, column=0, columnspan=3, sticky="nsew")
    tk_label2.grid(row=1, column=0, columnspan=3, sticky="nsew")


# sets the icon of the frame
def set_icon(root: Tk):
    # icon = PhotoImage(file="ui/icon.png")  # change to png we are using
    # root.iconphoto(True, icon)
    pass

def center_gui(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# sets all the buttons on the frame
def set_buttons(root: Tk):
    w, h = math.ceil(root.winfo_screenwidth() * 0.8), math.ceil(root.winfo_screenheight() * 0.8)
    try_one = Button(root, text="Try me! \n ASL to English", command=lambda: startaslText(root),
                     bg="#daf5f3", width=w//2, height=5, highlightbackground="#daf5f3", fg="#000000",
                     font=("Comic Sans", 20))

    try_two = Button(root, text="Try me! \n English to ASL", command=lambda: root.destroy(),
                     bg="#daf5f3", width=w//2, height=5, highlightbackground="#daf5f3", fg="#000000",
                     font=("Comic Sans", 20))

    sys_admin = Button(root, text="Check System", command=lambda: verification_handler(root),
                       bg="#daf5f3", width=5, height=5,
                       highlightbackground="#daf5f3", fg="#000000",
                       font=("Comic Sans", 20))

    try_one.grid(row=2, column=0, columnspan=1, sticky="nsew")
    try_two.grid(row=2, column=1, columnspan=1, sticky="nsew")
    sys_admin.grid(row=3, column=0, columnspan=2, sticky="nsew")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)


def startaslText(root):
    root.destroy()
    aslText.App()

# template code to create buttons
def create_button(root: Tk, **kwargs):
    # for handling errors
    valid_indexes = {'text', 'command', 'bg', 'size'}
    items = kwargs.items()
    assert items.__sizeof__() <= valid_indexes.__sizeof__(), "too many arguments"
    for key, value in items:
        assert key in valid_indexes, "not a valid index"

    # working function
    bg = kwargs['bg']  # background color of the button
    size = kwargs['size']  # size of the button
    fg = "#000000"
    button = Button(root,
                    text=kwargs['text'],
                    bg=bg,
                    width=size,
                    height=size,
                    highlightbackground=bg,
                    fg=fg,
                    font=("Comic Sans", 20),
                    command=kwargs['command'])
    return button

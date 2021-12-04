import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import time
from tkinter.ttk import Progressbar

window = tk.Tk()
window.title('AI Facial Recognition')
window.geometry('1120x720+700+200')

img = Image.open("assets/recogbg.png")
img = img.resize((1120, 720), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
label1 = tk.Label(window, image=img)
label1.place(x=0, y=0)

methods = [cv2.TM_CCOEFF_NORMED]
image, template, img2 = '', '', ''
h, w = '', ''


def base_img():
    global image
    file_path = filedialog.askopenfilename()
    image = cv2.resize(cv2.imread(file_path, 0), (0, 0), fx=0.8, fy=0.8)


def second_img():
    global template, h, w
    file_path = filedialog.askopenfilename()
    template = cv2.resize(cv2.imread(file_path, 0), (0, 0), fx=0.8, fy=0.8)
    h, w = template.shape


def step():
    for i in range(5):
        window.update_idletasks()
        pb['value'] += 20
        time.sleep(0.08)
        txt['text'] = pb['value'], '%'


def compare_img():
    global image, template, methods, img2, can

    if image == '' or template == '' or h == '' or w == '':
        return
    else:
        step()
    for method in methods:
        img2 = image.copy()
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        bottom_right = (location[0] + w, location[1] + h)
        cv2.rectangle(img2, location, bottom_right, 255, 5)

    if img2 != '':
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img2)
        im_pil = im_pil.resize((650, 420), Image.ANTIALIAS)
        im_pil = ImageTk.PhotoImage(im_pil)
        can.config(can.create_image(0, 0, anchor="nw", image=im_pil))


first_img = tk.Button(
    text="Import base image",
    width=25,
    height=5,
    bg="#131313",
    bd=1,
    fg="white",
    command=base_img
)
first_img.pack(pady=(200, 25), padx=25, anchor="w")

second_img = tk.Button(
    text="Import second image",
    width=25,
    height=5,
    bg="#131313",
    bd=1,
    fg="white",
    command=second_img
)

second_img.pack(padx=25, anchor="w")

compare = tk.Button(
    text="Compare Images",
    width=25,
    height=5,
    bg="#131313",
    bd=1,
    fg="white",
    command=compare_img
)

compare.pack(pady=25, padx=25, anchor="w")
can = tk.Canvas(window, bd=0, highlightthickness=0, bg="black", height=420, width=650)
can.place(x=350, y=130, anchor='nw')


pb = Progressbar(
    window,
    orient="horizontal",
    length=150,
    mode='determinate'
    )

pb.place(x=26, y=130)

txt = tk.Label(
    window,
    text='0%',
    bg='#345',
    fg='#fff'

)

txt.place(x=185, y=130)

window.mainloop()

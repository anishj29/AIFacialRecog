import cv2
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title('AI Facial Recognition')
window.geometry('800x600+700+200')
bg = tk.PhotoImage(file="assets/recogbg.png")
label1 = tk.Label(window, image=bg)
label1.place(x=0, y=0)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
image, template = '', ''
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


def compare_img():
    global image, template, methods
    if image == '' or template == '' or h == '' or w == '':
        return
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
        cv2.imshow('match', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


first_img = tk.Button(
    text="Import base image",
    width=25,
    height=5,
    bg="#131313",
    bd=1,
    fg="white",
    command=base_img
)
first_img.pack(pady=(150, 25), padx=25, anchor="w")

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

can = tk.Canvas(window, bg='black', height=300, width=450)
can.place(x=350, y=160, anchor='nw')

window.mainloop()

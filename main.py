import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

image = cv2.imread(file_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
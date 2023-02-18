import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
import pytesseract
import numpy as np
#from data_from_Inv import *

root = tk.Tk()
root.geometry('800x800')
highlightedtext = []

pytesseract.run_tesseract.tesseract_cmd = '/home/chitresh/.local/lib/python3.10/site-packages'


def Select_Image():
    browse_text.set("loading...")
    image = filedialog.askopenfilename(initialdir='/home', title="Select_Image",
                                       filetypes=(("image", "*.png"), ("all files", "*.")))
    img = cv2.imread(image)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_value = np.array([80, 165, 240])
    upper_value = np.array([100, 220, 255])
    mask = cv2.inRange(hsv, lower_value, upper_value)
    highlightedtext.append(pytesseract.image_to_string(mask))
    savetext(highlightedtext)
    browse_text.set('opening')
    #button_text = tk.StringVar()
    #button_text.set('extract the data')
    #Button(root, textvariable=button_text, command=extract_data_from_text_file).pack()
    open_text_file()


def open_text_file():
    open_file = open('Data_Testj.txt', 'r')
    file = open_file.readlines()
    text_box.insert(1.0, file)


def savetext(highlighted_text):
    with open('Data_Testj.txt', 'w') as f:
        for text in highlighted_text:
            f.writelines(f'{text}')


canvas = tk.Canvas(root, height=400, width=800, bg='#20bebe')
canvas.pack()

text_box = tk.Text(root, height=10, width=40)
text_box.pack()

browse_text = tk.StringVar()
Button(root, textvariable=browse_text, command=Select_Image).pack()
browse_text.set("Select Image")

root.mainloop()

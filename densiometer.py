import os
import numpy as np
import csv
from tkinter import Tk
from tkinter import filedialog
from PIL import Image
from numpy import asarray

root = Tk()
data_list = []
directory = filedialog.askdirectory()
os.chdir(directory)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".JPG"):  # sets path of .JPG images - may need to adjust to include other types
        image = Image.open(filename)  # loads image data from image path
        gray = image.convert('L')  # stores image in grayscale
        black_white = np.asarray(gray).copy()  # copies as array
        black_white[black_white < 128] = 0  # black designated pixels
        black_white[black_white >= 128] = 255  # Wwite designated pixels
        black_white_array = asarray(black_white)  # recreates array bilaterally
        white_pixels = np.sum(black_white_array == 255)  # number of white pixels in rendered image
        black_pixels = np.sum(black_white_array == 0)  # number of black pixels in rendered image
        canopy_density = (black_pixels/(white_pixels+black_pixels))
        data_list.append(canopy_density)
        root.withdraw()
        continue
    else:
        continue
with open("canopydensity.csv", 'w') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_ALL, delimiter='\n')
    wr.writerow(data_list)
    root.withdraw()

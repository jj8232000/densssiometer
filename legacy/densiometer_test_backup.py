import os
import numpy as np
import csv
from tkinter import filedialog
from numpy import asarray
from PIL import Image

# fullpath = os.path.dirname(os.path.abspath(__file__))  # designates location of script
# os.chdir(fullpath)  # sets working directory to fullpath
# print(os.getcwd()) #  tests path

data_list = []
directory = filedialog.askdirectory()
os.chdir(directory)
# filenames_and_paths = {}
# for file_name in os.listdir(directory):
#     if file_name.endswith(".JPG"):
#         file_path = os.path.join(dir, file_name)
#         filenames_and_paths[file_name] = file_path
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".JPG"):  # sets path of .JPG images
        image = Image.open(filename)  # loads image data from image path
        numpydata = asarray(image)  # builds array from image data
        image = Image.open(file)  # opens designated image
        gray = image.convert('L')  # stores image in grayscale
        bw = np.asarray(gray).copy()  # copies as array
        bw[bw < 128] = 0  # Black designated pixels
        bw[bw >= 128] = 255  # White designated pixels
        bw_array = asarray(bw)  # recreates array bilaterally
        white_pixels = np.sum(bw_array == 255)  # number of white pixels in rendered image
        black_pixels = np.sum(bw_array == 0)  # number of black pixels in rendered image
        canopy_density = (black_pixels/(white_pixels+black_pixels))
        data_list.append(canopy_density)
        continue
    else:
        continue
with open("canopydensity.csv", 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter='\n')
    wr.writerow(data_list)

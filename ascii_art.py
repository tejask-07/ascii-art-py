from PIL import Image 
import numpy as np

ASCII_CHARS = "@%#*+=-:. "
MAX_PIXEL_VALUE = 255

im = Image.open("car.jpeg")
im = im.convert("L")

resized_im = im.resize((480, 280))
resized_im.save("resized_img.jpeg")

pixel_matrix = np.array(resized_im)

intensity_matrix = pixel_matrix.tolist() 

def convert_to_ascii(intensity_matrix, ascii_chars):
    ascii_matrix = []
    for row in intensity_matrix:
        ascii_row = []
        for p in row:
                index = int(p / MAX_PIXEL_VALUE * (len(ascii_chars) - 1))
                ascii_row.append(ascii_chars[index])
        ascii_matrix.append(ascii_row)
    return ascii_matrix


print(convert_to_ascii(intensity_matrix, ASCII_CHARS))

def print_ascii_matrix(ascii_matrix):
    for row in ascii_matrix:
        line = [p*3 for p in row]
        print("".join(line))

print_ascii_matrix(convert_to_ascii(intensity_matrix, ASCII_CHARS))    
from PIL import Image 
import numpy as np

im = Image.open("car.jpeg")

resized_im = im.resize((640,480))
resized_im.save("resized_img.jpeg")

print(f"Image Size : {resized_im.size}")

pixel_matrix = np.array(resized_im)


def get_br_matrix(matrix) :
    intensity_matrix = []
    for row in matrix :
        intensity_row = []
        for p in row :
            intensity = (p[0] + p[1] + p[2])/3.0
            intensity_row.append(intensity)
        intensity_matrix.append(intensity_row)
    return intensity_matrix        

print(get_br_matrix(pixel_matrix))





    
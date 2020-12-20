import numpy as np
import cv2

# Python Programm, welches ein Bild horizontal spiegelt.-

image = cv2.imread('oilwagon.jpg', 0)

def mirroring(img):
    # set heigth and width as size of image
    height, width = img.shape
    size = (height, width)

    # create new image
    image_new = np.zeros(size, dtype=np.uint8)

    for i in range(0, height):
        for j in range(0, width):
            image_new[i, j] = img[(height - 1) - i, j]
    return image_new


image_mir = mirroring(image)
cv2.imshow('oilwagon', image)
cv2.waitKey(0)
cv2.imshow('oilwagon_mirrored', image_mir)
cv2.waitKey(0)

import numpy as np
import cv2


image = cv2.imread('oilwagon.jpg', 0)

def inversion(img):
    # set heigth and width as size of image
    height, width = img.shape
    size = (height, width)

    # create new image
    image_new = np.zeros(size, dtype=np.uint8)

    for i in range(0, height):
        for j in range(0, width):
            image_new[i, j] = 255 - img[i, j]
    return image_new


image_inv = inversion(image)
cv2.imwrite('oilwagon_inv.jpg', image_inv)
cv2.imshow('oilwagon', image)
cv2.waitKey(0)
cv2.imshow('oilwagon_inverted', image_inv)
cv2.waitKey(0)

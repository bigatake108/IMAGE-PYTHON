import numpy as np
import cv2

# Python Programm, welches einen 3 x 3 Median-Filter auf ein Bild anwendet.

image2 = cv2.imread('oilwagon_snp.jpg', 0)

def median(img):
    # create new image, set height and width as size of new image
    image_new = img.copy()
    height, width = image_new.shape
    size = (height, width)

    # Schleifen, die über alle Pixel außer die Randpixel gehen, da diese laut
    # Aufgabenstellung gleich bleiben
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Window 3 x 3 um den aktuellen Pixel erstellen
            window = image_new[i - 1:i + 2, j - 1:j + 2]
            # Window wird in ein 1D array ge-reshaped
            reshaped_window = window.reshape(-1)
            # Median im Window wird ermittelt
            median_val = np.median(reshaped_window)
            # Median wird dem Aktuellen Pixel zugewiesen
            image_new[i, j] = median_val
    return image_new


image2_median = median(image2)
cv2.imshow('oilwagon_snp', image2)
cv2.waitKey(0)
cv2.imshow('oilwagon_median', image2_median)
cv2.waitKey(0)

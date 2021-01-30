# Prototype stuff, not important

import cv2
import numpy as np
import gif2numpy
import glob, os

# Load color image
# img = cv2.imread("images/page-A-01-1024.jpg", 1)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def getImages(directorypath):
    os.chdir(directorypath)
    images = []
    # Gather the images in the file path
    for file in glob.glob("*"):
        # cv2 doesn't suppoer gif so we are converting all gifs to be numpy compatible
        if file.endswith(".gif"):
            frames, extensions, image_specs = gif2numpy.convert(file)
            image = frames[0]
        else:
            image = cv2.imread(file, 1)
        images.append(image)

    # Resize images to be the same size as the first
    width = int(0.6 * images[0].shape[1])
    height = int(0.6 * images[0].shape[0])
    dim = (width, height)
    for i, img in enumerate(images): 
        images[i] = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        
    return images

imgArray = getImages("images")

numpy_horizontal = np.hstack((imgArray[0], imgArray[1], imgArray[2]))

numpy_horizontal_concat = np.concatenate((imgArray[0], imgArray[1], imgArray[2]), axis=1)

cv2.imshow('test', numpy_horizontal_concat)
cv2.waitKey()
cv2.destroyAllWindows()

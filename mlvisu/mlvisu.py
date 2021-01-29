import cv2

def display(set):
    for image in set:
        cv2.imshow('test', image)
    return
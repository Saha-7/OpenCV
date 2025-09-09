import cv2
from numpy import imag

image = cv2.imread("Phase 1\Pedri.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("could not load image")
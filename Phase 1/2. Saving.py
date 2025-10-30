import cv2


image = cv2.imread("Phase 1\csk.jpg")

if image is not None:
    success = cv2.imwrite("output.png", image)
    if success:
        print("Imaged Saved Successfully")
    else:
        print("Failed to save image")
else:
    print("Could not load the image")
import cv2

image = cv2.imread("Phase 1\Pedri.jpg")

if image is not None:
    cv2.imshow("Image showing", image) # Displays the image in a pop-up window

    cv2.waitKey(5000) # Keep the window open for that time until the user presses a key.
    
    cv2.destroyAllWindows() # close all image windows
else:
    print("could not load the image")



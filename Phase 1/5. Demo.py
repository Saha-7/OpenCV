import cv2

image = cv2.imread("Phase 1\csk.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Scale Image", gray)
    cv2.waitKey()
    cv2.destroyAllWindows()
    save = cv2.imwrite("output.png", gray)

    if save:
        print("Imaged Saved Successfully")
    else:
        print("Failed to save image")
else:
    print("Could not load the image")
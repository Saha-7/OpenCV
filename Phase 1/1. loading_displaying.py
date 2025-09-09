import cv2

image = cv2.imread("Phase 1\Pedri.jpg")

if image is not None:
    cv2.imshow("Image showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not load the image")

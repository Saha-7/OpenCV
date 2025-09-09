import cv2


image = cv2.imread("Phase 1\Pedri.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image")
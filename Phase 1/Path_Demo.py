import cv2

input_path = input("Enter the path of the image: ").strip()
image = cv2.imread(input_path)

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ask user choice BEFORE showing image
    save_choice = input("Do you want to save the grayscale image? (y/n): ").strip().lower()

    if save_choice == 'y':
        output_path = input("Enter output file path (e.g., output.png): ").strip()
        save_status = cv2.imwrite(output_path, gray)
        if save_status:
            print("✅ Image saved successfully at:", output_path)
        else:
            print("❌ Failed to save image.")
    else:
        cv2.imshow("Gray Scale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("❌ Could not load image.")

import cv2

# Step 1: Take image location from user
image_location = input("Enter the path of your image: ").strip()

# Step 2: Read the image
image = cv2.imread(image_location)

if image is None:
    print("❌ Could not load the image. Please check the path.")
else:
    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 4: Ask what to do next
    print("Choose an option:")
    print("1️⃣ Show image")
    print("2️⃣ Save image")

    op = input("Enter your choice (1/2): ").strip()

    if op == "1":
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif op == "2":
        file_name = input("Enter the new file name (without extension): ").strip()
        save_path = f"{file_name}.jpg"
        success = cv2.imwrite(save_path, gray)

        if success:
            print(f"✅ Image saved successfully as {save_path}")
        else:
            print("❌ Failed to save image.")
    else:
        print("⚠️ Invalid choice.")

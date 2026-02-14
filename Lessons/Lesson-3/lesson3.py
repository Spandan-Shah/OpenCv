import cv2

# Load image
img = cv2.imread("spy.png")

if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Print shape comparison
    print("Original Shape:", img.shape)
    print("Grayscale Shape:", gray.shape)

    # Show both images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

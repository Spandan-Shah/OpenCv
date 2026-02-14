import cv2

img = cv2.imread("spy.png")

if img is None:
    print("Error: Image not found!")
else:
    # Step 1 – Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 2 – Reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3 to 5 – Apply Canny
    edges = cv2.Canny(blur, 100, 200)

    cv2.imshow("Original Image", img)
    cv2.imshow("Edge Detection Result", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

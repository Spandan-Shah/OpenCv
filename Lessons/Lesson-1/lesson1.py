import cv2

img = cv2.imread("spy.png")  # SAME folder, correct path

if img is None:
    print("Error: Image not found!")
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2

# Load the image (Make sure spy.png is in the same folder)
img = cv2.imread("spy.png")

# Check if image loaded properly
if img is None:
    print("Error: Image not found!")
else:
    
    print("Image Shape (Height, Width, Channels):", img.shape)

    
    pixel = img[50, 50]
    print("Pixel value at (50,50) [B, G, R]:", pixel)

   
    img[50, 50] = [0, 0, 255]   # BGR → Pure Red

  
    cv2.imshow("Modified Image", img)

    
    cv2.waitKey(0)

   
    cv2.destroyAllWindows()

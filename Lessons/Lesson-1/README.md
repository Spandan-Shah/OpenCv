# 🖼 Basic OpenCV Image Loading and Display

This document explains how a simple OpenCV program loads and displays an image step-by-step. Each line plays an essential role in image processing, visualization, and resource management.

---

## 📌 Complete Example Code

```python
import cv2

img = cv2.imread("spy.png")

if img is None:
    print("Error: Image not found!")
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

## 1️. Importing OpenCV
```
import cv2
```

This line imports the **OpenCV** library into your Python program.

> OpenCV stands for **Open Source Computer Vision Library**. It provides tools to work with:

- Images
- Videos
- Cameras
- Object detection
- Face recognition
- AI vision models

When you write:

```
import cv2
```

You are telling Python:

“Give me access to all OpenCV computer vision functions.”
Without this line, nothing related to image processing would work.

## 2️. Reading an Image from Disk
```
img = cv2.imread("spy.png")
```

This line reads an image file from your computer.

🔎 What Happens Internally?

- OpenCV searches for the file named "spy.png"
- It loads the image into memory
- It converts the image into a NumPy array
- That array is stored inside the variable img
- So img is not just a picture.

- It is actually a matrix structured as:

> Height × Width × Channels

Example:

800 × 600 × 3

Where:
800 → Height
600 → Width
3 → Color channels

⚠️ Important: OpenCV uses BGR format, not RGB.

## 3️. Safety Check for Image Loading
```
if img is None:
```

This is a defensive programming safety check.

If OpenCV cannot find "spy.png" due to:

- Wrong file name
- Incorrect file path
- Missing file
- Typographical error

Then cv2.imread() returns None.

This condition checks:

1. “Did the image load successfully?”
2. If not, it prevents your program from crashing.
3. This is considered professional coding practice.

## 4️. Error Message Handling
```
print("Error: Image not found!")
```

If the image fails to load, this line prints a clear error message.

Instead of seeing a confusing crash, you receive meaningful feedback that helps with debugging.

## 5️. Displaying the Image
```
cv2.imshow("Image", img)
```

This function displays the image in a new window.

Parameters:
- "Image" → Window title
- img → Image data to display
- OpenCV creates a pop-up window and renders the image matrix visually.

You can think of it as:

“Display this matrix as a visible image.”

## 6️. Waiting for User Input
```
cv2.waitKey(0)
```
This line is extremely important.

It tells OpenCV:

- “Wait until a key is pressed.”
- Without this line, the window would open and close instantly.

Meaning of **0**

0 means:
- **Wait indefinitely** until the user presses any key.

If you wrote:
```
cv2.waitKey(5000)
```
It would wait for 5 seconds (5000 milliseconds).

## 7️. Closing All Windows
```
cv2.destroyAllWindows()
```

After a key press, this line closes all OpenCV windows.

It:
- Cleans up memory
- Closes display windows properly
- Releases system resources

Professional programs always release resources after execution.
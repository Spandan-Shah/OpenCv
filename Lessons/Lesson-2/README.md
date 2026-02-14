# Lesson 2 – Understanding Image Shape & Pixels in OpenCV

When we load an image using:

```python
img = cv2.imread("spy.png")
```

OpenCV stores the image as a NumPy array (matrix).

An image is not just a picture —  
It is a 3D matrix of numbers.

Structure:
> (height, width, channels)

Example:
> (800, 600, 3)

This means:

• 800 → Number of rows (Height)  
• 600 → Number of columns (Width)  
• 3 → Number of color channels  



## 🎨 2️. Understanding Color Channels (BGR Format)

#### OpenCV uses BGR format, not RGB.

Each pixel contains:
- [Blue, Green, Red]

Example:
- [255, 0, 0]

Means:

• Blue = 255  
• Green = 0  
• Red = 0  

That is pure Blue in OpenCV.

⚠ Important: Many libraries use RGB, but OpenCV uses BGR.


## 📐 3️. Understanding img.shape

When we write:

```python
print(img.shape)
```

We get:
> (height, width, channels)

Example:
> (800, 600, 3)

We can also access individually:

```python
img.shape[0]  → Height
img.shape[1]  → Width
img.shape[2]  → Channels
```

This is important because:

• AI models require fixed image sizes  
• Bounding boxes depend on width and height  
• Cropping requires pixel positions  


## 🔍 4️. Accessing Pixel Values

We can access a pixel using:

```python
pixel = img[50, 50]
```

This means:

• Row = 50  
• Column = 50  

It returns:
[B, G, R]

Example:
[120, 45, 200]

Each value ranges from:
0 to 255

This is called an 8-bit image.


## ✏ 5️. Modifying Pixel Values

We can change a pixel manually:

```python
img[50, 50] = [0, 0, 255]
```

This sets that pixel to:

Pure Red (in BGR format)

After modification, displaying the image will show a small red dot.


## 🧮 6️. Total Pixel Values in an Image

If image shape is:
(800, 600, 3)

Total values inside image:
800 × 600 × 3 = 1,440,000 numbers

Each value ranges from 0–255.

That means an image is just a huge collection of numbers.

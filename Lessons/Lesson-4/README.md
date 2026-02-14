# Stage 4 – Canny Edge Detection

**Edge detection** is a fundamental image processing technique used to identify locations in an image where pixel intensity changes sharply.  
An **edge** represents a boundary between two different regions in an image.

For example:

If a black object is placed on a white background, the border where black meets white forms an edge.

Edge detection reduces the image to its **structural skeleton**.  
Instead of focusing on color and texture, we focus only on **geometry and form**.

 

## 1️. Understanding Intensity Change (Core Concept)

An image is a matrix of pixel values.

In grayscale, each pixel ranges from:

```
0 → 255
```

Consider the following row of pixel intensities:

```
10  12  11  15  200  205
```

Notice the sudden jump from **15 → 200**.

This sharp increase indicates a possible **edge**.

Edge detection algorithms mathematically measure this rate of change.

This rate of change is called the **gradient**.

- Large gradient → Strong edge  
- Small gradient → No significant edge  

 

## 2️. Introduction to the Canny Edge Detection Algorithm

**Canny Edge Detection** was developed by **John F. Canny in 1986**.

It is widely used because it satisfies three main criteria:

- **Good detection** → Finds real edges  
- **Good localization** → Edge location is accurate  
- **Minimal response** → One edge is detected only once  

It is considered one of the most reliable edge detection techniques in computer vision.

Canny works in **five major stages**.

 

## 3️. Internal Working of Canny (Step-by-Step Explanation)

 

### STEP 1 – Noise Reduction Using Gaussian Blur

Real-world images contain noise.

Noise causes random pixel intensity fluctuations.

If we directly detect edges on a noisy image, false edges will appear.

To prevent this, Canny first applies **Gaussian smoothing**.

Gaussian blur reduces high-frequency noise.

The Gaussian function is:

```
G(x,y) = (1 / 2πσ²) * e^(-(x² + y²) / 2σ²)
```

This smoothing operation averages neighboring pixels using a weighted distribution.

In OpenCV:

```python
blur = cv2.GaussianBlur(gray, (5,5), 0)
```

- `(5,5)` → Kernel size  
- Larger kernel → More smoothing  
- More smoothing → Less noise but possible loss of detail  



### STEP 2 – Gradient Calculation (Finding Intensity Change)

After smoothing, the algorithm calculates the **image gradient**.

It uses **Sobel operators** to calculate derivatives in X and Y directions.

- `Gx` → Change in horizontal direction  
- `Gy` → Change in vertical direction  

Gradient magnitude is calculated as:

```
Magnitude = √(Gx² + Gy²)
```

This magnitude represents **edge strength**.

Gradient direction is calculated as:

```
Direction = arctan(Gy / Gx)
```

Direction tells us edge orientation:

- Horizontal edge  
- Vertical edge  
- Diagonal edge  

Edges are strongest where magnitude is high.

 

### STEP 3 – Non-Maximum Suppression (Thinning Edges)

After gradient calculation, edges appear thick.

But real edges should be thin and precise.

**Non-maximum suppression** removes unnecessary pixels.

For each pixel:

- Compare it with neighboring pixels in the gradient direction  
- If it is not the strongest pixel in that direction, remove it  

This produces thin, sharp edges.

Now edges are only **one pixel wide**.

 

### STEP 4 – Double Thresholding

Not all detected edges are real.

Some may be weak due to noise or lighting variation.

Canny applies two thresholds:

- Lower threshold  
- Upper threshold  

Example in OpenCV:

```python
edges = cv2.Canny(blur, 100, 200)
```

If gradient magnitude is:

- Less than 100 → Discarded  
- Greater than 200 → Strong edge  
- Between 100 and 200 → Weak edge  

Weak edges are not immediately discarded.

They move to the next stage.

 

### STEP 5 – Edge Tracking by Hysteresis

Weak edges are evaluated.

If a weak edge is connected to a strong edge, it is kept.

If it is isolated, it is removed.

This ensures **continuity and reliability** in edge detection.

The final result contains **clean, connected, meaningful edges**.

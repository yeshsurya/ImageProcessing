import cv2

def edge_detection(image, threshold1, threshold2):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, threshold1, threshold2)

    return edges


# Load the image
image = cv2.imread('paris.jpg')

# Perform edge detection
edges = edge_detection(image, threshold1=100, threshold2=200)

# Display the original image and the detected edges
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
In the above code, the edge_detection function takes an image, threshold1, and threshold2 as input. 
The threshold1 and threshold2 parameters control the intensity gradient thresholds, determining which edges are detected.

The function first converts the input image to grayscale using cv2.cvtColor. 
Then, it applies the Canny edge detection algorithm using cv2.Canny, which calculates the intensity gradient of each pixel and detects edges based on the specified thresholds.

The resulting edges image will contain white pixels representing the detected edges and black pixels for the background.

You can adjust the threshold values according to your specific requirements. Smaller threshold values will detect more edges, 
including weaker ones, while larger threshold values will detect only stronger edges.

Feel free to modify the code and experiment with different threshold values to achieve the desired level of edge detection. 
Additionally, you can explore other edge detection algorithms provided by OpenCV, such as the Sobel operator or the Laplacian operator, depending on your specific needs.
____________________________________________________________________________________________________________________________________________________________________________________________________
Canny Edge detection algorithm : 
The Canny edge detection algorithm is a popular and widely used method for detecting edges in digital images. 
It was developed by John F. Canny in 1986 and is known for its effectiveness in detecting edges accurately while suppressing noise.

The Canny edge detection algorithm consists of the following steps:

1. Gaussian blurring: The first step is to apply a Gaussian filter to the input image. 
This is done to reduce noise and smooth out the image. 
The Gaussian filter is a low-pass filter that removes high-frequency noise while preserving the edges.

2. Gradient calculation: The next step involves calculating the intensity gradients of the image. 
The algorithm uses two filters, the Sobel operators, to compute the gradients in the horizontal and vertical directions. 
The gradient magnitude and orientation can be calculated as follows:

Gradient magnitude: magnitude = sqrt(Gx^2 + Gy^2)
Gradient orientation: orientation = arctan(Gy / Gx)
Here, Gx and Gy are the horizontal and vertical gradient responses, respectively.

3. Non-maximum suppression: In this step, the algorithm examines the gradient magnitude and orientation to thin out the edges. 
It goes through each pixel and checks if it is a local maximum along the gradient direction. If it is not, the pixel value is set to zero, 
effectively suppressing non-maximum points and preserving only the thin, prominent edges.

4. Double thresholding: This step aims to identify potential edges by setting two thresholds: a high threshold and a low threshold. 
Pixels with gradient magnitudes above the high threshold are considered strong edges, while those below the low threshold are considered non-edges. 
Pixels with magnitudes between the two thresholds are classified as weak edges.

5. Edge tracking by hysteresis: The final step involves determining the final edge map by analyzing the weak edges and their connectivity to strong edges. 
Starting from a strong edge pixel, the algorithm follows the weak edges that are connected to it. If a weak edge pixel is not connected to a strong edge pixel, it is discarded. 
This process helps to preserve only the continuous and significant edges, while eliminating spurious weak edges.

6.The Canny edge detection algorithm provides a robust and flexible approach to edge detection. 
It can handle a wide range of image types and noise levels while producing accurate and well-defined edges. 
The choice of threshold values greatly affects the results, and careful tuning is often required to achieve the desired edge detection outcome.
'''
'''
Strong and weak edges : 
In image processing, edges are regions of rapid intensity transitions or boundaries between different objects or textures in an image. 
During edge detection algorithms, edges are often classified as weak or strong based on their intensity gradients or response to edge detection filters.

Strong edges: Strong edges are the prominent and well-defined edges in an image. 
These edges typically correspond to significant boundaries between different objects or regions. Strong edges have high gradient magnitudes or strong responses to edge detection filters. They are considered reliable and accurate representations of the underlying image structure.

Weak edges: Weak edges, also known as faint or low-intensity edges, are less prominent or less well-defined compared to strong edges. 
These edges may correspond to weaker intensity transitions or less significant boundaries in the image. 
Weak edges have lower gradient magnitudes or weaker responses to edge detection filters. 
They are often associated with noise, texture, or subtle variations in the image.

The distinction between strong and weak edges is important in various image processing tasks. 
For example, in edge detection algorithms like the Canny edge detector, a double thresholding step is employed to classify edges into strong and weak categories. 
Strong edges are considered reliable and retained as part of the final edge map. Weak edges are retained if they are connected to strong edges, 
as they may contribute to the overall edge structure. However, isolated or unconnected weak edges are typically discarded to reduce noise or false detections.

The differentiation between strong and weak edges allows for better edge representation, noise suppression, and subsequent analysis or processing of 
the image's structural information.
'''
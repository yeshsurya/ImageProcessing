import cv2
import numpy as np

# Load the input image in grayscale
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the SVD of the image
U, s, V = np.linalg.svd(image, full_matrices=False)

# Get the first singular vector
eigen_vector = U[:, 0]

# Compute the eigenimage
eigen_image = np.outer(eigen_vector, eigen_vector)

# Normalize the eigenimage to the 0-255 range
eigen_image = cv2.normalize(eigen_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the eigenimage
cv2.imshow('Eigenimage', eigen_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

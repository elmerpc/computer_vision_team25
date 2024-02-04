import cv2
import numpy as np

# Load the image
image = cv2.imread('data/noisy.png', 0)
# Create a kernel for erosion
kernel = np.ones((5, 5), np.uint8)

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

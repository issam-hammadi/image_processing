import cv2
import numpy as np 

# Lecture de l'image 
image_brut = cv2.imread(r"C:\Users\issam.hammadi\OneDrive - IRT M2P\Bureau\Stage IRT M2P\code\autres_images\echantillon2_hasard_test_1moappro_small.jpg")

# Convertion au niveau de gris 
gray = cv2.cvtColor(image_brut, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray,50, 255) #check those parameters

# contours : liste des points de countours , hierarchy : représente la hiérarchie de contours 
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort the contours by area
#key could be perimeter, area or any other criteria (true for descending order)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# The approximation to a polygon is useless since we want to detect a big size edge with sharp edges
# Approximate each contour
for contour in contours:
    #epsilon = 0.01 * cv2.arcLength(contour, True)
    #approx = cv2.approxPolyDP(contour, epsilon, True)
    cv2.drawContours(image_brut,[contour], 0, (0, 255, 0), 3)
"""
Next: Index of the next contour at the same hierarchical level.
Previous: Index of the previous contour at the same hierarchical level.
First_Child: Index of the first child contour.
Parent: Index of the parent contour.
"""






# Display the image
cv2.imshow('Contours', image_brut)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img = cv2.imread('C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/image1.jpeg', 0)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Threshold Image', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
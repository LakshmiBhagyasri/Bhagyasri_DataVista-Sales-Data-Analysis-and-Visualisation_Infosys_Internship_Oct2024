import cv2

img = cv2.imread('C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/image1.jpeg', 0)
equalized = cv2.equalizeHist(img)

cv2.imshow('Equalized Image', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
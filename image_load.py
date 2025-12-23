import cv2

img = cv2.imread('walle.jpg',0)

cv2.imshow('walle',img)
cv2.waitKey(0)

cv2.destroyAllWindows()

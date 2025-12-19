import cv2

img = cv2.imread('/home/robotx/Downloads/walle.jpg')

cv2.imshow('walle',img)
cv2.waitKey(0)

cv2.destroyAllWindows()

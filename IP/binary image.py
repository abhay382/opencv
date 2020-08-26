import cv2
img = cv2.imread('lena.jpg', 0)

cv2.imshow('gray', img)



ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary',bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img_basic = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image basic',img_basic)
cv2.waitKey(0)

cv2.imwrite('result1.jpg',img_basic)

img_gray = cv2.cvtColor(img_basic,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gray',img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.jpg',img_gray)

# cv2.destroyAllWindows()


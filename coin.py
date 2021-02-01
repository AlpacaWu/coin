import cv2 as cv
import numpy as np
def contours_demo(image):
    dst = cv.GaussianBlur(image, (5, 5), 0) #高斯模糊去噪
    gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU) #用大律法、全局自適應閾值方法進行圖像二值化
    cloneTmage, contours, heriachy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        M = cv.moments(contour)
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        area = cv.contourArea(contour)
        if area > 100 and area < 10000:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(image, (cx,cy), 1, (0, 255, 0), 4)
            perimeter = cv.arcLength(contour,True)
            print(i,area,perimeter/3.14159)
            print(cx,cy)
    cv.imshow("contours", image)
src = cv.imread('coin.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #設置為WINDOW_NORMAL可以任意縮放
cv.imshow('input_image', src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
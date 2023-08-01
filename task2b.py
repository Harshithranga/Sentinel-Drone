import cv2
import numpy as np
img = cv2.imread('yellow_detect.jpeg',1)
list1 = []
for i in range(len(img)):
    for j in range(len(img[i])):
        if (([250] <= img[i][j][2] <= [255]) and ([200] <= img[i][j][1] <= [220])) and ([65] <= img[i][j][0] <= [95]):
            n = [j, i]
            list1.append(n)
        else:
            img[i][j] = [255, 255, 255]
print(f"{(list1[0][1]+list1[len(list1)-1][1])/2} {(list1[0][0]+list1[len(list1)-1][0])/2}")
print(list1)
cv2.imshow("Image", img)
cv2.waitKey(0)
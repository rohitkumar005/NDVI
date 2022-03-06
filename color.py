# IN this program i have find NDVI of NIR & RED images,
# After finding the NDVI i have to fill the color of each pix according to the NDVI COLOR SPECTRUM

import cv2
import os

#selecting RED spectrum image
img1= cv2.imread('RED_IMAGE')

#selecting NIR spectrum image
img2= cv2.imread('NIR_IMAGE')

#Addition of images
add= img2 + img1

#Subtraction of images
subtract= cv2.subtract(img2,img1)

#Applying NDVI method
ndvi= subtract/add

#showing the NDVI_image after applying NDVI method
#cv2.imshow("NDVI_image", ndvi)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Assigning the NDVI image to image_pop
image_pop= ndvi

#show the height, width and channel of image
print(image_pop.shape)

[x,y,c]= image_pop.shape
for x1 in range(0,x):
    for y1 in range(0,y):
        pix= image_pop[x1,y1]

        if ((pix[0] == 0)):
            pix[0] = 0
            pix[1] = 0
            pix[2] = 255
        elif ((pix[0] >= 0.0 and pix[0] <= 0.2)):
            pix[0] = 0
            pix[1] = 100
            pix[2] = 100
        elif ((pix[0] <= 0.4) and (pix[0] > 0.2)):
            pix[0] = 0
            pix[1] = 128
            pix[2] = 0
        elif ((pix[0] <= 0.6) and (pix[0] > 0.4)):
            pix[0] = 0
            pix[1] = 225
            pix[2] = 225
        elif ((pix[0] <= 0.8) and (pix[0] > 0.6)):
            pix[0] = 64
            pix[1] = 128
            pix[2] = 128
        elif ((pix[0] <= 1.0) and (pix[0] > 0.8)):
            pix[0] = 0
            pix[1] = 255
            pix[2] = 0
        else:
            pix[0] = 0
            pix[0] = 0 
            pix[0] = 0

#showing image after filling the color in each pixel according to the NDVI color spectrum
cv2.imshow("color",image_pop)


#Saving the image after coloring in png formate
#os.chdir('1')
cv2.imwrite("color_0.png",image_pop)
cv2.waitKey(0)
cv2.destroyAllWindows()

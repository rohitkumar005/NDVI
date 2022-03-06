#Here i taken image of NDVI image that is colored
#After coloring of image we are stitching the image to make a one image

import cv2
import os

#selcting the color folder
mainfolder= 'color'

#countering the number of folder in color_folder
myfolder=os.listdir(mainfolder)
print(myfolder)

#in For we are counting the number of images
for folder in myfolder:
    path= mainfolder +'/' +folder

    #creating the images variable to store the images
    images=[]

    #Reading the number of images
    mylist=os.listdir(path)
    print(f'Total no of images detected {len(mylist)}')

#Reading the images from the folder
    for imgn in mylist:

        #assigning the image to curlmg
        curlmg= cv2.imread(f'{path}/{imgn}')

        #Adding image in image folder
        images.append(curlmg)

#Assigning the stitcher function to stitcher variable
    stitcher= cv2.createStitcher()

#checking the status and result of stitcher process
    (status,result)=stitcher.stitch(images)

    if(status == cv2.STITCHER_OK):
        print('Panorama generated')
        cv2.imshow(folder,result)

#Here I choose the different locaiton to saving the image
        os.chdir("ortho\panorama_out")

#In this we are saving the image in tif format
        cv2.imwrite("panorama_image_100.tif",result)
        cv2.waitKey(1)
    else:
        print("panorama generation unsuccessful")

cv2.waitKey(0)

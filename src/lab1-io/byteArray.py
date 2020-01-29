import cv2
import numpy
import os

#grayImage = numpy.array(grayByteArray).reshape(height, width)
#bgrImage = numpy.array(bgrByteArray).reshape(height, width, 3)

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)

cv2.imshow('RandomGray.png', grayImage)

# Convert the array to make a 400x100 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imshow('RandomColor.png', bgrImage)

#After running this script, we should have a pair of randomly generated images, RandomGray.png and RandomColor.png

cv2.waitKey(0)
""" Created by Kevin Burgon
    This module performs some experimental image threshold filtering on
    images.  This is currently meant to be run as a stand alone application.
"""

import numpy as np
import cv2
import sys

def enhanceImage(filePath, fileOutput='output.jpg'):
    print(filePath)
    subjectImage = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    cv2.bitwise_not(subjectImage, subjectImage)

    thres = 155.0
    color = 254.0
    th, outputImage = cv2.threshold(subjectImage, thres, color, cv2.THRESH_BINARY_INV)

    # cv2.imwrite(fileOutput, outputImage)

    window_width = int(outputImage.shape[1])
    window_height = int(outputImage.shape[0])

    cv2.namedWindow('output', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('output', window_width, window_height)

    cv2.imshow('output', outputImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        enhanceImage(sys.argv[1])
    elif len(sys.argv) > 2:
        enhanceImage(sys.argv[1], sys.argv[2])

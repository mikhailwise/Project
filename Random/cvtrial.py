import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Help.jpg',0)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite('Help.jpg',img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

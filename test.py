import cv2
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.cm as cm
import numpy as np

# load image using OpenCV
img = cv2.imread('test.jpg')

plt.imshow(img)
plt.axis('off')
plt.savefig("output.jpg")

# load image using PIL
img2 = Image.open('test.jpg')

plt.imshow(img2, cmap=cm.Greys_r)
plt.show()

# saving using OpenCV
cv2.imwrite('new_image.jpg', img)

# saving using PIL
img2.save('new_image2.jpg')

# display array
print(img.shape)
print(img)
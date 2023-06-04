import cv2
from PIL import Image
import numpy as np
def rm_watermark(source_img, destination_img):
    image = cv2.imread(source_img, -1)
    #img = cv2.imread(image, -1)
    np_array = np.array(image)
    img = cv2.cvtColor(np_array, cv2.COLOR_BGR2GRAY)
  #  _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite(destination_img, new_img)
    #return cv2.imwrite(destination_img, new_img)

if __name__ == '__main__':
    source_img = r"img.png"
    dest_img = r"test3.png"
    rm_watermark(source_img, dest_img)
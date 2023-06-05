import cv2
from PIL import Image, ImageSequence
import numpy as np
import os

inputPath = "input/"
outputPath = "output/"
dir_list = os.listdir(inputPath)
inputFile = inputPath + dir_list[0]


def rm_watermark(source_img, destination_img):

    image = cv2.imread(source_img, -1)
    #img = cv2.imread(image, -1)
    np_array = np.array(image)
    img = cv2.cvtColor(np_array, cv2.COLOR_BGR2GRAY)
  #  _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite(destination_img, new_img)

    image_1 = Image.open(destination_img)
    im_1 = image_1.convert('RGB')
    im_1.save("output/outtt.pdf")
    #return cv2.imwrite(destination_img, new_img)


def checkIfTiffAndConvertToPdf(source_name):
    print("asdasd sad asdsa")
    print(source_name)
    if(source_name.rsplit('.', 1)[1].lower() == 'tiff'):
        pdf_path = source_name.replace('.tiff', '.pdf')
        outputPathPDF = inputPath + pdf_path
        print("found a tiff image converting it to PDF")
        image = Image.open(inputPath+source_name)
        images = []
        for i, page in enumerate(ImageSequence.Iterator(image)):
            page = page.convert("RGB")
            images.append(page)
        if len(images) == 1:
            images[0].save(outputPathPDF)
        else:
            images[0].save(outputPathPDF, save_all=True, append_images=images[1:])
        return pdf_path


if __name__ == '__main__':
    source_img = r"img.tiff"
    dest_img = r"test3.png"
    #pdf_path = checkIfTiffAndConvertToPdf(dir_list[0])
    #print("doneeeeee")
    #print(pdf_path)
    rm_watermark(inputPath+source_img, "output/ss.png")
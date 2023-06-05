import cv2
from PIL import Image, ImageSequence
import numpy as np
import os
from pdf2image import convert_from_path
from pytesseract import Output, pytesseract

inputPath = "input/"
outputPath = "output/"
outFile = "outFile.pdf"
dir_list = os.listdir(inputPath)
inputFile = inputPath + dir_list[0]



def convertPdfToImage(source_img):
    pages = convert_from_path(source_img)
    for pagenum in range(len(pages)):
        np_array = np.array(pages[pagenum])
        image = cv2.cvtColor(np_array, cv2.COLOR_BGR2GRAY)
        _, new_img = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
        pdf1 = pytesseract.image_to_pdf_or_hocr(new_img, extension='pdf')
        # rm_watermark()
    with open(outputPath+outFile, 'w+b') as f:
        f.write(pdf1)  # pdf type is bytes by default


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
    print(source_name)
    if(source_name.rsplit('.', 1)[1].lower() != 'tiff' and source_name.rsplit('.', 1)[1].lower() != "png" and source_name.rsplit('.', 1)[1].lower() != "pdf"):
       print("not valid input format file")
       exit(0)


if __name__ == '__main__':
    checkIfTiffAndConvertToPdf(inputFile)
    if(inputFile.rsplit('.', 1)[1].lower() != "pdf"):
        convertPdfToImage(inputFile)
    else:
        rm_watermark(inputFile, outputPath+outFile)
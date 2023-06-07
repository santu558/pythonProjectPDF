import traceback
from pathlib import Path

import cv2
import numpy
import numpy as np
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image, ImageDraw, ImageChops
import os
from fpdf import FPDF

from pdf2image import convert_from_path

inputPath = "input/"
outputPath = "output/"
outFile = "outFile.pdf"

def remove_watermark_from_pdf(pdf_path, output_path):
    try:
        # Read the PDF file
        pdf = PdfReader(pdf_path)

        # Create a new PDF writer
        writer = PdfWriter()

        # Store Pdf with convert_from_path function
        images = convert_from_path(pdf_path)

        #output images
        outPutImagesPDF = []
        pdf = FPDF(format='A4')
        pdf.set_auto_page_break(0)
        # opening or creating pdf file
        file = open(output_path, "wb")

        # Iterate over each page in the PDF
        for i in range(len(images)):
            print(images[i])
            open_cv_image = numpy.array(images[i])
            image = open_cv_image[:, :, ::-1].copy()
            img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
            pil_image = Image.fromarray(new_img)
            im_1 = pil_image.convert('P')
            print(im_1)
            outPutImagesPDF.append(im_1)
        outPutImagesPDF[0].save(output_path)

        print("Watermark removed from PDF:", output_path)

    except Exception as e:
        print("Error removing watermark from PDF:", e)
        traceback.print_exc()



def remove_watermark_from_tiff(tiff_path, output_path):
    try:
        image = cv2.imread(tiff_path, -1)
        # img = cv2.imread(image, -1)
        np_array = np.array(image)
        img = cv2.cvtColor(np_array, cv2.COLOR_BGR2GRAY)
        #  _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        cv2.imwrite(output_path, new_img)
        print("Watermark removed from TIFF:", output_path)

    except Exception as e:
        print("Error removing watermark from TIFF:", e)


# List of documents to remove watermark from
documents = [
    {
        'path': 'input/pdf-watermark-sample.pdf',
        'output_path': 'output/output1.pdf'
    },
    {
        'path': 'input/watermarksample.tiff',
        'output_path': 'output/output2.tiff'
    },
    # Add more documents as needed
]


if __name__ == '__main__':
    for document in documents:
        doc_path = document['path']
        output_path = document['output_path']
        file_ext = os.path.splitext(doc_path)[1]
        if file_ext.lower() == '.pdf':
            remove_watermark_from_pdf(doc_path, output_path)
        elif file_ext.lower() == '.tiff':
            remove_watermark_from_tiff(doc_path, output_path)
        else:
            print("Unsupported file format:", file_ext)
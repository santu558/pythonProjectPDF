import cv2
import numpy as np
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image, ImageDraw, ImageChops
from fpdf import FPDF
import os


inputPath = "input/"
outputPath = "output/"
outFile = "outFile.pdf"

def remove_watermark_from_pdf(pdf_path, output_path):
    try:
        # Read the PDF file
        pdf = PdfReader(pdf_path)

        # Create a new PDF writer
        writer = PdfWriter()

        # Iterate over each page in the PDF
        for page in pdf.pages:
            # Remove the watermark from the page
            # In this example, we're simply copying the page without modification

            print(page)
            writer.add_page(page)

        # Write the new PDF to the output path
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        print("Watermark removed from PDF:", output_path)

    except Exception as e:
        print("Error removing watermark from PDF:", e)


def remove_watermark_from_tiff(tiff_path, output_path):
    try:
        # Open the TIFF image
        image = Image.open(tiff_path)

        # Create a blank white image of the same size
        white_image = Image.new('RGB', image.size, (255, 255, 255))

        # Subtract the original image from the white image to remove the watermark
        #watermark_removed_image = ImageChops.subtract(white_image, image)

        image = cv2.imread(tiff_path, -1)
        # img = cv2.imread(image, -1)
        np_array = np.array(image)
        img = cv2.cvtColor(np_array, cv2.COLOR_BGR2GRAY)
        #  _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        _, new_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        cv2.imwrite(output_path, new_img)



        # Save the watermark-removed TIFF image
        #watermark_removed_image.save(output_path)

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
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pdf2image import convert_from_path
import numpy as np
import pytesseract
from pytesseract import Output
import pypdf


def checkOrientationPDF():
    outputDict = {}
    pdfList = []
    pages = convert_from_path('samplePdf10_removed.pdf')

    for pagenum in range(len(pages)):
        img = np.array(pages[pagenum])
        results = pytesseract.image_to_osd(img, output_type=Output.DICT, config='--psm 0 -c min_characters_to_try=5')
        print(results)
        if int(results['rotate']) > 0:
            print("has rotated text")
            outputDict[pagenum] = {"angle": results['rotate']}
        pdfList.append(pytesseract.image_to_pdf_or_hocr(img, extension='pdf'))
    return outputDict


# ## GET THE ANGLE OF PDF
# for pagenum in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(pagenum)
#     orientation = pdf_reader.getPage(pagenum).get('/Rotate')
#     print(orientation)

def rotatePDF(orients):
    pdf_in = open('samplePdf10_removed.pdf', 'rb')
    pdf_reader = pypdf.PdfReader(pdf_in)
    pdf_writer = pypdf.PdfWriter()
    print(orients)
    for pagenum in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[pagenum]
        if pagenum in orients:
            page.rotate(orients[pagenum]['angle'])
            print("rotated")
        page = pdf_reader.pages[pagenum]
        pdf_writer.add_page(page)
    pdf_out = open('LandscapeTestFileOut.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # copyPDF()
    orients = checkOrientationPDF()
    rotatePDF(orients)
    # print(orients)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

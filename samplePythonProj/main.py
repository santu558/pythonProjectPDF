# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import PyPDF2


def rotatePDF():
    pdf_in = open('215834730190.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        orientation = pdf_reader.getPage(pagenum).get('/Rotate')
        page.rotateClockwise(-orientation)
        pdf_writer.addPage(page)






    pdf_out = open('215834730190New1.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
# ## GET THE ANGLE OF PDF
# for pagenum in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(pagenum)
#     orientation = pdf_reader.getPage(pagenum).get('/Rotate')
#     print(orientation)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rotatePDF()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

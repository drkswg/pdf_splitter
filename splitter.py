from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog as fd

def openFile():
    global f
    file = fd.askopenfilename()
    f = PdfFileReader(open(file, 'rb'))

openFile()

for i in range(f.numPages):
    output = PdfFileWriter()
    output.addPage(f.getPage(i))
    with open("pages/document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
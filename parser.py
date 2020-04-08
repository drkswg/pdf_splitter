from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog as fd

def openFile():
    global f
    file = fd.askopenfilename()
    f = PdfFileReader(open(file, 'rb'))

openFile()

page = f.getPage(0)
print(page.extractText())


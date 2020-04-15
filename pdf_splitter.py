import io
import re
from tkinter import filedialog as fd
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from PyPDF2 import PdfFileWriter, PdfFileReader


def open_file():
    global file
    file = fd.askopenfilename()


def get_pages(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            yield text

            converter.close()
            fake_file_handle.close()


def get_npers(pdf_path):
    global s
    s = []

    for page in get_pages(pdf_path):
        npers = re.search('\d\d\d-\d\d\d-\d\d\d\s\d\d', page)
        try:
            s.append(npers.group(0))
        except:
            s.append('?')


def split():
    f = PdfFileReader(open(file, 'rb'))

    for i in range(f.numPages):
        output = PdfFileWriter()
        output.addPage(f.getPage(i))

        with open("pages/{0}) {1}.pdf".format(i, s[i]), "wb") as outputStream:
            output.write(outputStream)


if __name__ == '__main__':
    open_file()
    get_npers(file)
    split()

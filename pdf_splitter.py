import io
import re
from tkinter import filedialog as fd
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from PyPDF2 import PdfFileWriter, PdfFileReader


class PDFSplitter:
    def __init__(self):
        self.open_file()
        self.get_npers(file)
        self.split()

    def open_file(self):
        global file
        file = fd.askopenfilename()

    def get_pages(self, pdf_path):
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

    def get_npers(self, pdf_path):
        global s
        s = []

        for page in self.get_pages(pdf_path):
            npers = re.search('\d\d\d-\d\d\d-\d\d\d\s\d\d', page)
            try:
                s.append(npers.group(0))
            except:
                s.append('?')

    def split(self):
        f = PdfFileReader(open(file, 'rb'))

        for i in range(f.numPages):
            output = PdfFileWriter()
            output.addPage(f.getPage(i))

            with open(f"pages/{i}) {s[i]}.pdf", "wb") as outputStream:
                output.write(outputStream)


if __name__ == '__main__':
    PDFSplitter()

import os, glob
from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
pdf_dir = ("C:\\Smug\\CPA\\") #where you keep all your PDFs, change both here and in outputStream below

pdfs = [pdf for pdf in glob.glob(os.path.join(pdf_dir, "*.pdf"))]

for pdf in pdfs:
    outputStream = file("C:\\Smug\\CPA\\doc_out%d.pdf", "rb" % pdfs.index(pdf))
    for i in range(pdf.getNumPages()):
        if i%3 == 0:
            output.addPage(pdf.getPage(i))
            try: output.addPage(pdf.getPage(i+1))
            except KeyError:
                pass
            try: output.addPage(pdf.getPage(i+2))
            except KeyError:
                pass
    output.write(outputStream)

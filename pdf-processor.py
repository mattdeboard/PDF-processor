import os, glob
from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
pdf_dir = ("C:\\Smug\\Hipster\\") #where you keep all your PDFs, change both here and in outputStream below

pdfs = [pdf for pdf in glob.glob(os.path.join(pdf_dir, "*.pdf"))]

for pdf in pdfs:
    outputStream = file("C:\\Smug\\Hipster\\doc_out%d.pdf", "rb" % pdfs.index(pdf))
    for i in range(pdf.getNumPages()):
        if i%3 == 0:
            output.addPage(pdf.getPage(i))
            output.addPage(pdf.getPage(i+1))
            output.addPage(pdf.getPage(i+2))
    output.write(outputStream)
    
    
    
    
    

import PyPDF2
files = ["JavaChapter1.pdf","Chapter2.pdf"]
merger = PyPDF2.PdfMerger()
for file in files:
    pdf_on = open(file,"rb")
    reader = PyPDF2.PdfReader(pdf_on)
    merger.append(reader)
pdf_on.close()
merger.write("Notes.pdf")
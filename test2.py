import PyPDF2
from fpdf import FPDF
import fpdf
import os



class pdf_generator:
    def __init__(self):
        pass
    def create_empty_pdf(self,name, location=os.getcwd()):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.line(10,20,30,40)
        pdf.output(location + "/" + name + ".pdf")

    def rotate_page(self,name,rotate=90,location=os.getcwd()):
        pdf_in = open(location + "/" + name + '.pdf', 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_in)
        pdf_writer = PyPDF2.PdfFileWriter()
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            page.rotateClockwise(rotate)
            pdf_writer.addPage(page)

        pdf_out = open(location + "/" + name + '.pdf', 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()
    def draw_lines(self,name,rotate=90,location=os.getcwd()):
        pdf = fpdf.open(location + "/" + name + '.pdf')
        pdf.line(10, 30, 110, 30)
        pdf.output(location + "/" + name + ".pdf","wb")

if __name__ == "__main__":
    pdf = pdf_generator()
    pdf.create_empty_pdf("ercan")
    #pdf.rotate_page("ercan")
    pdf.draw_lines("ercan")

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def create_pdf(output_file, text_content, plot_image):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Add text content
    textobject = c.beginText()
    textobject.setTextOrigin(50, height - 50)
    for line in text_content.split('\n'):
        textobject.textLine(line)
    c.drawText(textobject)

    # Add plot
    plot_img = ImageReader(plot_image)
    c.drawImage(plot_img, 50, 50, width=500, height=300)

    c.showPage()
    c.save()
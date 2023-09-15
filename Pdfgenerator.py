

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Define the invoice data
customer_name = "John Doe"
order_number = "12345"
invoice_items = [
    ["Product Description", "Quantity", "Unit Price", "Total"],
    ["Product 1", 2, 10.0, 20.0],
    ["Product 2", 3, 15.0, 45.0],
]
total_amount = 65.0

# Create a PDF document
pdf_filename = "E:/backend/pdf/generated.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Create a list to hold the invoice content
elements = []

# Create a stylesheet for formatting
styles = getSampleStyleSheet()

# Add a title
elements.append(Paragraph("Invoice for: {}".format(customer_name), styles["Title"]))
elements.append(Paragraph("Order Number: {}".format(order_number), styles["Title"]))
elements.append(Paragraph("\n", styles["Normal"]))

# Create a table for the invoice items
data = invoice_items
table = Table(data, colWidths=[200, 80, 80, 80])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

elements.append(table)
elements.append(Paragraph("\n", styles["Normal"]))

# Add the total amount
elements.append(Paragraph("Total Amount: ${:.2f}".format(total_amount), styles["Normal"]))

# Build the PDF document
doc.build(elements)

print("Invoice PDF saved to "+ pdf_filename)



from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

# Create a list of text filepaths:
filepaths = glob.glob("Text+Files/*.txt")

# Create one PDF file
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Go through each text file
for filepath in filepaths:
    pdf.add_page()

    # Get filename without the extension
    # and convert it to title case
    filename = Path(filepath).stem
    name = filename.title()

    # Set the name to the PDF:
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=name, align="L", ln=1, border=0)

pdf.output('output_student.pdf')
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
# P=portrait or L=Landscape
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header:
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # Red Green Blue goes to 254
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    # w = cell expands until end of the page
    # h = height (altura), recommended same as size of font
    # align = Left or Right
    # ln = break line
    # border = border of the cell

    pdf.line(10, 21, 200, 21)
    # x1 10, y1 21= donde comienza el texto desde el margen izq en mm
    #          y desde arriba de la página hacia abajo
    # x2 200, y2 21 = desde el margen izq hacia la derecha

    # Set the footer:
    pdf.ln(260)  # Height of A4 is 298 mm
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        # range it´s kinda list, range(5): creates a range object with items 0, 1, 2, 3, and 4.
        # to create a range with items 2, 3, 4, and 5, you can do: range(2, 6)
        # the step of those ranges is 1, change the step by adding a third argument to the range class: range(2, 6, 3)
        # that range would produce a range with items 10, 13, 16, and 19, so at a step of three.
        pdf.add_page()

        # Set the footer:
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")

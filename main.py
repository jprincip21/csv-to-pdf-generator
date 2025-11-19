import pandas as pd
from fpdf import FPDF

df = pd.read_csv("assets/topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) # Pages will not be broken automatically

# Sets up header
for index, row in df.iterrows(): # Iterrows returns a dictionary (order......*name*, topic........*name*, pages.....*num*)
    for page in range(row["Pages"]):
        pdf.add_page() #Creates page

        if page == 0: # Only adds header on first page
            pdf.set_font(family="Times", style="B", size=24) #Sets font to 24pt bolded times new roman
            pdf.set_text_color(100, 100, 100) # Makes text gray
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0) # Creates cell for pdf
            pdf.line(10, 21, 200, 21)

            # Set up footer for header page
            pdf.ln(265)  # add 278 break lines to go to bottom of page

            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        else:
            # Set up footer for blank pages
            pdf.ln(277) # add 278 break lines to go to bottom of page

            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
# W = 0: entire page,
# h=12: height is 12mm, Should be same size as font
# txt is Text,
# align: Alignment of text,
# ln: break line. 1 means next cell will be added to new line 0 = add right at the end of the previous cell
# border: creates a border around the cell

pdf.output("output.pdf")

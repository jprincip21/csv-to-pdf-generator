import pandas as pd
from fpdf import FPDF

df = pd.read_csv("assets/topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows(): # Iterrows returns a dictionary (order......*name*, topic........*name*, pages.....*num*)
    for page in range(row["Pages"]):
        pdf.add_page() #Creates page
        if page == 0:
            pdf.set_font(family="Times", style="B", size=24) #Sets font to 24pt bolded times new roman
            pdf.set_text_color(100, 100, 100) # Makes text gray
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0) # Creates cell for pdf
            pdf.line(10, 21, 200, 21)

# W = 0: entire page,
# h=12: height is 12mm, Should be same size as font
# txt is Text,
# align: Alignment of text,
# ln: break line. 1 means next cell will be added to new line 0 = add right at the end of the previous cell
# border: creates a border around the cell

pdf.output("output.pdf")

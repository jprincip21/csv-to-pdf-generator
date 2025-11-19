# CSV to PDF Generator

This project generates a structured PDF document based on a list of topics and the number of pages each topic should occupy. It uses **pandas** to read topic data from a CSV file and **FPDF** to create a formatted PDF that includes headers, footers, and horizontal guide lines.

---

## 📄 Features

- Reads topic information from `assets/topics.csv`
- Creates a multi-page PDF with:
  - A bold header on the first page of each topic
  - A footer on every page
  - Horizontal lines every 10 mm for writing space
- Customizable fonts, colors, spacing, and layout
- Automatically generates all pages based on CSV data

## ▶️ How It Works

- The script loads topics.csv using pandas.
- For each topic (row), the number of pages is read from the Pages column.
- A new page is created for each page assigned to the topic.
- The first page of each topic includes:
- The topic header (large bold text)
- All pages include:
- A footer showing the topic name (small italic text)
- Horizontal lines spaced 10 mm apart
- The final compiled PDF is saved as output.pdf.

## 📝 CSV Format Example

Your topics.csv should look like this:

```
Order,Topic,Pages
1,Introduction,1
2,Data Types,2
3,Functions,3
```

## 📌 Notes

- Page breaks are disabled to keep layout positioning consistent.
- All measurements are in millimeters.
- You can easily customize fonts, colors, margins, and line spacing by modifying the script.

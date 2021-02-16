#install this before run this script
#pip install docx2pdf

from docx2pdf import convert

convert("Name_Of_Your_Doc_File.docx")
convert("Name_Of_Your_Doc_File.docx", "Output.pdf")
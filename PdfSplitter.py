from PyPDF2 import PdfWriter, PdfReader
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import os

documentPath = prompt("Enter the path of the PDF file: ", completer=PathCompleter(),)
outputName = input("Enter the name of the output file: ")
outputPath = prompt("Enter the path of the output file, defaults to current directory: ", completer=PathCompleter())
inputPdf = PdfReader(open(documentPath, "rb"))

for i in range(len(inputPdf.pages)):
    output = PdfWriter()
    output.add_page(inputPdf.pages[i])
    with open(os.path.join(outputPath, outputName+"-%s.pdf" % i), "wb") as outputStream:
        output.write(outputStream)
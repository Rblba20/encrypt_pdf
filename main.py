from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

print('Перенесите файл, с которым будет произведена работа, в папку с программой')
pdfwriter = PdfFileWriter()
name = input('Введите имя файла: ')
pdf = PdfFileReader(name)

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

name_ = input('Введите желаемое имя(с расширением pdf) для защищенного файла: ')
with open(name_, 'wb') as file:
    pdfwriter.write(file)
